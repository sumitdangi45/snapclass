# SnapClass - Setup Guide

## Project Overview
AI Attendance Project - Face Recognition based attendance system with Streamlit frontend and Supabase backend.

---

## ✅ Setup Status

### Done:
- ✅ Project cloned from original repository
- ✅ Git configured with your name (Sumit Dangi) and email (sumitdangi8455@gmail.com)
- ✅ Remote changed to your GitHub: https://github.com/sumitdangi45/snapclass.git
- ✅ Virtual Environment created (venv/)
- ✅ .env files created (.env and .env.example)
- ✅ .gitignore configured

---

## 🚀 Quick Start

### 1. Activate Virtual Environment

**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows CMD:**
```cmd
venv\Scripts\activate.bat
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** The installation may take time due to face_recognition and dlib packages.

---

## 🔑 Environment Configuration

### Setup Supabase

1. Go to https://supabase.com and create an account
2. Create a new project
3. Copy your credentials:
   - Project URL
   - Anon Key (API Key)

4. Update `.env` file:

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_anon_key_here
```

---

## 📁 Project Structure

```
snapclass/
├── venv/                  # Virtual environment
├── src/                   # Source code
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (⚠️ Keep SECRET)
├── .env.example          # Example env file
├── .gitignore            # Git ignore rules
└── README.md             # Original README
```

---

## 🔄 Git Commands

### View Status:
```bash
git status
```

### Make Changes & Commit:
```bash
git add .
git commit -m "Your message here"
```

### Push to GitHub:
```bash
git push origin main
```

### Pull Latest Changes:
```bash
git pull origin main
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

This will open the app at `http://localhost:8501`

---

## 📝 Important Notes

1. **Never commit `.env`** - It contains sensitive keys
2. **Keep `.env.example`** - Share with team to show what variables are needed
3. **Use `venv`** - Always activate virtual environment before working
4. **Git workflow** - Always pull before starting work, commit regularly, push at day end

---

## ❓ Troubleshooting

### Virtual env not activating?
- Ensure you're using PowerShell or CMD correctly
- Try using full path: `C:\Users\sumit\OneDrive\Desktop\snapclass\venv\Scripts\Activate.ps1`

### pip install fails?
- Ensure virtual env is activated: `pip --version` should show path to venv
- Try: `python -m pip install --upgrade pip`
- Then retry: `pip install -r requirements.txt`

### Supabase connection error?
- Check `.env` file has correct credentials
- Verify internet connection
- Check Supabase project is running

---

## 🤝 Next Steps

1. ✅ Setup complete! All environments configured
2. 📦 Install dependencies when ready (takes ~10-15 minutes)
3. 🔑 Add Supabase credentials to `.env`
4. ▶️ Run `streamlit run app.py`
5. 📤 Push changes: `git push origin main`

---

**Your project is ready to use!** 🎉
