# Environment Variables Setup Guide

## Overview

All sensitive configuration (API keys, Firebase credentials, secret keys) are now stored in environment variables using a `.env` file.

## Files Structure

```
market-classifier-main/
├── .env                 # Your actual credentials (NOT committed to git)
├── .env.example         # Template file (safe to commit)
└── .gitignore          # Ensures .env is not committed
```

## Quick Setup

### 1. Install python-dotenv

```bash
pip install python-dotenv
```

Or install all dependencies:

```bash
pip install -r requirements.txt
```

### 2. Copy Example File

```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

### 3. Edit .env File

Open `.env` and update the values:

```env
# Flask Secret Key - Generate a random string
SECRET_KEY=your-random-secret-key-change-this-in-production

# Firebase Configuration - Already filled with your project details
FIREBASE_API_KEY=your-firebase-api-key
FIREBASE_AUTH_DOMAIN=your-project-id.firebaseapp.com
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_STORAGE_BUCKET=your-project-id.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID=your-sender-id
FIREBASE_APP_ID=1:your-sender-id:web:d325ace529b0511cf5cf0a
FIREBASE_MEASUREMENT_ID=your-measurement-id

# Financial News API (Optional)
FINANCIAL_NEWS_API_KEY=demo
```

## Generating a Secure SECRET_KEY

### Option 1: Python
```python
import secrets
print(secrets.token_hex(32))
```

### Option 2: Online
Use a password generator to create a 64-character random string.

### Option 3: Command Line
```bash
# Linux/Mac
openssl rand -hex 32

# Windows PowerShell
[Convert]::ToBase64String((1..32 | ForEach-Object { Get-Random -Maximum 256 }))
```

## How It Works

### Backend (app.py)
```python
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Access variables
secret_key = os.environ.get('SECRET_KEY')
firebase_api_key = os.environ.get('FIREBASE_API_KEY')
```

### Frontend (login.html)
Firebase config is fetched from backend API endpoint `/api/firebase-config` which reads from environment variables.

## Production Deployment (Render.com)

### Don't use .env file in production!

Instead, set environment variables in Render dashboard:

1. Go to your service on Render
2. Click **Environment** tab
3. Add each variable:

```
SECRET_KEY = your-production-secret-key
FIREBASE_API_KEY = your-firebase-api-key
FIREBASE_AUTH_DOMAIN = your-project-id.firebaseapp.com
FIREBASE_PROJECT_ID = your-project-id
FIREBASE_STORAGE_BUCKET = your-project-id.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID = your-sender-id
FIREBASE_APP_ID = 1:your-sender-id:web:d325ace529b0511cf5cf0a
FIREBASE_MEASUREMENT_ID = your-measurement-id
FINANCIAL_NEWS_API_KEY = demo
```

4. Click **Save Changes**
5. Service will automatically redeploy

## Security Best Practices

### ✅ DO:
- Keep `.env` file in `.gitignore`
- Use different SECRET_KEY for development and production
- Generate strong random SECRET_KEY (64+ characters)
- Commit `.env.example` as a template
- Set environment variables in production dashboard

### ❌ DON'T:
- Commit `.env` file to git
- Share `.env` file publicly
- Use default/weak SECRET_KEY in production
- Hardcode credentials in source code
- Use same SECRET_KEY across environments

## Verification

### Check .gitignore
```bash
cat .gitignore
```

Should contain:
```
.env
```

### Check if .env is tracked by git
```bash
git status
```

`.env` should NOT appear in the list. If it does:
```bash
git rm --cached .env
git commit -m "Remove .env from tracking"
```

### Test environment variables
```python
from dotenv import load_dotenv
import os

load_dotenv()
print(os.environ.get('SECRET_KEY'))  # Should print your secret key
print(os.environ.get('FIREBASE_API_KEY'))  # Should print Firebase API key
```

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'dotenv'"
**Solution**: Install python-dotenv
```bash
pip install python-dotenv
```

### Issue: Environment variables not loading
**Solution**: 
1. Check `.env` file exists in project root
2. Check file is named exactly `.env` (not `.env.txt`)
3. Ensure `load_dotenv()` is called before accessing variables
4. Restart the application

### Issue: Firebase config not loading in frontend
**Solution**:
1. Check `/api/firebase-config` endpoint is accessible
2. Open browser console and check for errors
3. Verify environment variables are set correctly

### Issue: .env file committed to git
**Solution**:
```bash
# Remove from git tracking
git rm --cached .env

# Add to .gitignore if not already there
echo ".env" >> .gitignore

# Commit the changes
git add .gitignore
git commit -m "Remove .env from tracking and update .gitignore"
```

## Environment Variables Reference

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `SECRET_KEY` | Flask session encryption key | Yes | dev-secret-key |
| `FIREBASE_API_KEY` | Firebase API key | Yes | None |
| `FIREBASE_AUTH_DOMAIN` | Firebase auth domain | Yes | None |
| `FIREBASE_PROJECT_ID` | Firebase project ID | Yes | None |
| `FIREBASE_STORAGE_BUCKET` | Firebase storage bucket | Yes | None |
| `FIREBASE_MESSAGING_SENDER_ID` | Firebase messaging sender ID | Yes | None |
| `FIREBASE_APP_ID` | Firebase app ID | Yes | None |
| `FIREBASE_MEASUREMENT_ID` | Firebase measurement ID | No | None |
| `FINANCIAL_NEWS_API_KEY` | Financial news API key | No | demo |

## Testing

1. Create `.env` file with your credentials
2. Run the application:
   ```bash
   python app.py
   ```
3. Check console output - should not show any environment variable errors
4. Test login - Firebase should initialize correctly
5. Check browser console - should see Firebase config loaded from backend

## Migration Checklist

- [x] Created `.env` and `.env.example` files
- [x] Updated `.gitignore` to exclude `.env`
- [x] Added `python-dotenv` to `requirements.txt`
- [x] Updated `app.py` to load environment variables
- [x] Created `/api/firebase-config` endpoint
- [x] Updated `login.html` to fetch config from backend
- [x] Removed hardcoded credentials from source code
- [x] Created documentation (this file)

## Next Steps

1. ✅ Install python-dotenv: `pip install python-dotenv`
2. ✅ Copy `.env.example` to `.env`
3. ✅ Generate secure SECRET_KEY
4. ✅ Test application locally
5. ✅ Set environment variables in production (Render)
6. ✅ Verify `.env` is not committed to git

---

**Status**: All credentials are now securely stored in environment variables! 🔒

