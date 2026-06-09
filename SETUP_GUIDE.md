# SnapClass - Complete Setup Guide

## 📋 Project Overview

This is a monorepo containing two applications:

1. **Main Application** (AI Attendance) - Streamlit based face recognition attendance system
2. **Landing Page** - Flask based marketing landing page

---

## ✅ Setup Completed

### Main Application Setup:
- ✅ Repository cloned from `ai-attendance-project-app`
- ✅ Virtual environment created (`venv/`)
- ✅ Dependencies installed:
  - Streamlit, NumPy, Pandas, Scikit-Learn
  - Supabase client
  - Image & QR processing (Pillow, Segno)
  - Audio processing (Librosa, Resemblyzer)
  - Bcrypt for security

### Landing Page Setup:
- ✅ Repository cloned from `ai-attendance-project-landing`
- ✅ Virtual environment created (`landing-page/venv/`)
- ✅ Dependencies installed:
  - Flask (web framework)
  - Gunicorn (production server)

### Git Configuration:
- ✅ Git user: Sumit Dangi (sumitdangi8455@gmail.com)
- ✅ Remote updated to your GitHub: `https://github.com/sumitdangi45/snapclass.git`

---

## 🚀 Running the Applications

### Main Application (Streamlit)

**Terminal 1 - Activate & Run:**
```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run Streamlit app
streamlit run app.py
```

**Access at:** `http://localhost:8501`

---

### Landing Page (Flask)

**Terminal 2 - Activate & Run:**
```powershell
# Navigate to landing page directory
cd landing-page

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run Flask app
python app.py
```

**Access at:** `http://localhost:5002`

---

## 🔑 Supabase Configuration

### For Main Application:

1. Create account at https://supabase.com
2. Create a new project
3. Get credentials from Project Settings:
   - Project URL
   - Anon Public Key
   - Database Password (if needed)

4. Update `.env` file in root:
```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_anon_public_key_here
```

---

## 📁 Project Structure

```
snapclass/
├── Main Application
│   ├── app.py                 # Streamlit main entry point
│   ├── src/                   # Source code
│   │   ├── components/        # Reusable UI components
│   │   ├── database/          # Database operations
│   │   ├── pipelines/         # ML/Processing pipelines
│   │   ├── screens/           # App screens/pages
│   │   └── ui/                # UI utilities
│   ├── requirements.txt       # Main app dependencies
│   ├── venv/                  # Virtual environment
│   ├── .env                   # Environment variables
│   ├── .gitignore             # Git ignore rules
│   └── README.md              # Original documentation
│
├── Landing Page
│   ├── landing-page/
│   │   ├── app.py             # Flask main entry point
│   │   ├── requirements.txt   # Landing page dependencies
│   │   ├── venv/              # Virtual environment
│   │   ├── static/            # CSS, JS, images
│   │   ├── templates/         # HTML templates
│   │   ├── vercel.json        # Vercel deployment config
│   │   └── README.md          # Landing page docs
│
└── SETUP_GUIDE.md             # This file
```

---

## 🔄 Git Workflow

### Check Status:
```bash
git status
```

### Make Changes:
```bash
# Stage all changes
git add .

# Or stage specific files
git add src/screens/my_file.py

# Commit
git commit -m "Your meaningful message"
```

### Push to GitHub:
```bash
git push origin main
```

### Pull Latest:
```bash
git pull origin main
```

---

## ⚙️ Development Tips

### Main Application (Streamlit)
- **Hot reload:** Changes auto-reload in browser
- **State persistence:** Use `st.session_state` for variables
- **Debugging:** Check browser console and terminal logs
- **Database:** All Supabase operations through `/src/database`

### Landing Page (Flask)
- **Hot reload:** Set `debug=True` in `app.run()`
- **Routes:** Check `app.py` for URL mappings
- **Templates:** Jinja2 templates in `templates/`
- **Static files:** CSS/JS in `static/`

---

## 🐛 Troubleshooting

### Virtual Environment Issues
```powershell
# Force activate (PowerShell)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
.\venv\Scripts\Activate.ps1
```

### Port Already in Use
```bash
# Streamlit on different port
streamlit run app.py --server.port 8502

# Flask on different port
python app.py  # Change port in app.py: app.run(port=5003)
```

### Supabase Connection Error
- Verify `.env` file exists and has correct values
- Check internet connection
- Ensure Supabase project is active
- Try: `python -c "import supabase; print('Supabase OK')"`

### Dependencies Not Installing
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Clear cache and reinstall
pip install --no-cache-dir -r requirements.txt
```

---

## 📤 Deploying

### Main App (Streamlit Cloud)
1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Connect your repository
4. Add `.env` secrets via Streamlit Cloud UI

### Landing Page (Vercel)
1. Push to GitHub
2. Go to https://vercel.com
3. Import project from GitHub
4. `vercel.json` already configured
5. Deploy!

---

## 🎯 Next Steps

1. ✅ **Setup complete!** Both apps configured
2. 📦 **Run the apps** using commands above
3. 🔑 **Add Supabase credentials** to `.env`
4. 🧪 **Test both applications** locally
5. 📤 **Push to GitHub** when ready: `git push origin main`
6. 🌍 **Deploy to cloud** (Streamlit Cloud or Vercel)

---

## 📞 Quick Reference

| Task | Command |
|------|---------|
| Start Main App | `.\venv\Scripts\Activate.ps1 && streamlit run app.py` |
| Start Landing Page | `cd landing-page && .\venv\Scripts\Activate.ps1 && python app.py` |
| Check Dependencies | `pip list` |
| Update Dependencies | `pip install -r requirements.txt --upgrade` |
| Add New Package | `pip install package_name` then `pip freeze > requirements.txt` |
| Git Push | `git add . && git commit -m "msg" && git push origin main` |
| Check Git Status | `git status` |

---

**Your SnapClass project is fully setup and ready! 🚀**
