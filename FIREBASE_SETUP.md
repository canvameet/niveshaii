# Firebase Authentication Setup Guide

## Step 1: Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Add project"
3. Enter project name: `niveshai` (or your preferred name)
4. Disable Google Analytics (optional)
5. Click "Create project"

## Step 2: Enable Email/Password Authentication

1. In Firebase Console, go to **Authentication** → **Sign-in method**
2. Click on **Email/Password**
3. Enable the first toggle (Email/Password)
4. Click **Save**

## Step 3: Add Users

1. Go to **Authentication** → **Users**
2. Click **Add user**
3. Enter email and password for authorized users
4. Click **Add user**
5. Repeat for all users who should have access

## Step 4: Get Firebase Configuration

1. Go to **Project Settings** (gear icon)
2. Scroll down to **Your apps**
3. Click the **Web** icon (`</>`)
4. Register app with nickname: `niveshai-web`
5. Copy the `firebaseConfig` object

## Step 5: Update login.html

Open `templates/login.html` and replace the Firebase configuration (around line 230):

```javascript
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_STORAGE_BUCKET",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};
```

With your actual Firebase config values.

## Step 6: Set Secret Key (Production)

For production deployment, set the `SECRET_KEY` environment variable:

```bash
export SECRET_KEY="your-random-secret-key-here"
```

Or in Render.com:
- Go to your service → Environment
- Add environment variable: `SECRET_KEY` = `your-random-secret-key`

## Step 7: Test Login

1. Start the application:
   ```bash
   python app.py
   ```

2. Navigate to `http://localhost:8080`
3. You should be redirected to `/login`
4. Enter the email/password you created in Step 3
5. Upon successful login, you'll be redirected to the main dashboard

## Security Notes

- ✅ Only login is enabled (no signup)
- ✅ Users must be manually added in Firebase Console
- ✅ Session-based authentication with Flask
- ✅ Protected routes require login
- ✅ Logout available at `/logout`

## Firebase Security Rules (Optional)

If using Firestore or Realtime Database, add these rules:

```json
{
  "rules": {
    ".read": "auth != null",
    ".write": "auth != null"
  }
}
```

## Troubleshooting

**Issue**: "Firebase: Error (auth/configuration-not-found)"
- **Solution**: Make sure you've replaced the Firebase config in `login.html`

**Issue**: "No account found with this email"
- **Solution**: Add the user in Firebase Console → Authentication → Users

**Issue**: Session not persisting
- **Solution**: Make sure `SECRET_KEY` is set in environment variables

**Issue**: CORS errors
- **Solution**: Firebase should work from localhost. For production, add your domain to Firebase authorized domains in Authentication → Settings
