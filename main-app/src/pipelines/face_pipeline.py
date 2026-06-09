import numpy as np
import streamlit as st
from sklearn.svm import SVC

# Try to import face recognition dependencies
FACE_RECOGNITION_AVAILABLE = False
try:
    import dlib
    import face_recognition_models
    FACE_RECOGNITION_AVAILABLE = True
except ImportError:
    pass

# Only import from db if we might use it
try:
    from src.database.db import get_all_students
except ImportError:
    get_all_students = None


@st.cache_resource
def load_dlib_models():
    """Load dlib models for face recognition. Returns None if not available."""
    if not FACE_RECOGNITION_AVAILABLE:
        return None, None, None
    
    try:
        detector = dlib.get_frontal_face_detector()
        sp = dlib.shape_predictor(
            face_recognition_models.pose_predictor_model_location()
        )
        facerec = dlib.face_recognition_model_v1(
            face_recognition_models.face_recognition_model_location()
        )
        return detector, sp, facerec
    except Exception as e:
        st.error(f"Failed to load face recognition models: {str(e)}")
        return None, None, None


def get_face_embeddings(image_np):
    """Get face embeddings from image. Returns empty list if not available."""
    if not FACE_RECOGNITION_AVAILABLE:
        st.error("⚠️ Face recognition is not available in this environment. Please use the local version for photo attendance.")
        return []
    
    try:
        detector, sp, facerec = load_dlib_models()
        if detector is None or sp is None or facerec is None:
            return []
        
        faces = detector(image_np, 1)
        encodings = []

        for face in faces:
            shape = sp(image_np, face)
            face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1)
            encodings.append(np.array(face_descriptor))
        
        return encodings
    except Exception as e:
        st.error(f"Error processing face embeddings: {str(e)}")
        return []


@st.cache_resource
def get_trained_model():
    """Get trained classifier model. Returns None if not available or no data."""
    if not FACE_RECOGNITION_AVAILABLE or get_all_students is None:
        return None
    
    try:
        X = []
        y = []
        student_db = get_all_students()

        if not student_db:
            return None
        
        for student in student_db:
            embedding = student.get('face_embedding')
            if embedding:
                X.append(np.array(embedding))
                y.append(student.get('student_id'))

        if len(X) == 0:
            return None
        
        clf = SVC(kernel='linear', probability=True, class_weight='balanced')
        try:
            clf.fit(X, y)
        except ValueError:
            return None

        return {'clf': clf, 'X': X, "y": y}
    except Exception as e:
        st.error(f"Error training classifier: {str(e)}")
        return None


def train_classifier():
    """Train the classifier. Returns False if not available."""
    if not FACE_RECOGNITION_AVAILABLE:
        return False
    
    try:
        st.cache_resource.clear()
        model_data = get_trained_model()
        return bool(model_data)
    except Exception as e:
        st.error(f"Error training classifier: {str(e)}")
        return False


def predict_attendance(class_image_np):
    """Predict attendance from image. Returns empty dict if not available."""
    if not FACE_RECOGNITION_AVAILABLE:
        st.error("⚠️ Face recognition is not available in this environment.")
        return {}, [], 0
    
    try:
        encodings = get_face_embeddings(class_image_np)
        
        if not encodings:
            return {}, [], len(encodings)

        detected_student = {}
        model_data = get_trained_model()

        if not model_data:
            return detected_student, [], len(encodings)
        
        clf = model_data['clf']
        X_train = model_data['X']
        y_train = model_data['y']

        all_students = sorted(list(set(y_train)))

        for encoding in encodings:
            if len(all_students) >= 2:
                predicted_id = int(clf.predict([encoding])[0])
            else:
                predicted_id = int(all_students[0])

            student_embedding = X_train[y_train.index(predicted_id)]
            best_match_score = np.linalg.norm(student_embedding - encoding)
            resemblance_threshold = 0.6

            if best_match_score <= resemblance_threshold:
                detected_student[predicted_id] = True
        
        return detected_student, all_students, len(encodings)
    except Exception as e:
        st.error(f"Error predicting attendance: {str(e)}")
        return {}, [], 0

