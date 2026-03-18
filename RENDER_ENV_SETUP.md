# Render Environment Variables Setup Guide

## Step-by-Step Instructions

### Step 1: Go to Your Render Service

1. Login to Render: https://dashboard.render.com/
2. Find your NiveshAI service (or create new one if deploying for first time)
3. Click on the service name

### Step 2: Access Environment Variables

1. In your service dashboard, click on **"Environment"** tab in the left sidebar
2. You'll see a section called **"Environment Variables"**

### Step 3: Add Each Variable

Click **"Add Environment Variable"** and add these one by one:

#### 1. SECRET_KEY (Required)
```
Key:   SECRET_KEY
Value: <generate-a-random-64-character-string>
```

**How to generate SECRET_KEY:**
- Option A: Use Python
  ```python
  import secrets
  print(secrets.token_hex(32))
  ```
- Option B: Use online generator: https://randomkeygen.com/
- Option C: Use this: `your-super-secret-production-key-change-this-to-random-string-64-chars`

#### 2. Firebase API Key (Required)
```
Key:   FIREBASE_API_KEY
Value: AIzaSyC0qUMB0Uoq3lR95ZPfiuQlIMWW6Q4Hk1o
```

#### 3. Firebase Auth Domain (Required)
```
Key:   FIREBASE_AUTH_DOMAIN
Value: loginapp-e7f18.firebaseapp.com
```

#### 4. Firebase Project ID (Required)
```
Key:   FIREBASE_PROJECT_ID
Value: loginapp-e7f18
```

#### 5. Firebase Storage Bucket (Required)
```
Key:   FIREBASE_STORAGE_BUCKET
Value: loginapp-e7f18.firebasestorage.app
```

#### 6. Firebase Messaging Sender ID (Required)
```
Key:   FIREBASE_MESSAGING_SENDER_ID
Value: 419910970303
```

#### 7. Firebase App ID (Required)
```
Key:   FIREBASE_APP_ID
Value: 1:419910970303:web:d325ace529b0511cf5cf0a
```

#### 8. Firebase Measurement ID (Optional)
```
Key:   FIREBASE_MEASUREMENT_ID
Value: G-7S5VG2W9PL
```

#### 9. Financial News API Key (Optional)
```
Key:   FINANCIAL_NEWS_API_KEY
Value: demo
```

### Step 4: Save Changes

1. After adding all variables, click **"Save Changes"** button
2. Render will automatically redeploy your service with the new environment variables

### Step 5: Verify Deployment

1. Wait for deployment to complete (usually 2-5 minutes)
2. Check the logs for any errors
3. Visit your deployed URL
4. Test the login functionality

## Quick Copy-Paste Format

For faster setup, copy this entire block and add variables one by one:

```
SECRET_KEY=<generate-random-64-char-string>
FIREBASE_API_KEY=AIzaSyC0qUMB0Uoq3lR95ZPfiuQlIMWW6Q4Hk1o
FIREBASE_AUTH_DOMAIN=loginapp-e7f18.firebaseapp.com
FIREBASE_PROJECT_ID=loginapp-e7f18
FIREBASE_STORAGE_BUCKET=loginapp-e7f18.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID=419910970303
FIREBASE_APP_ID=1:419910970303:web:d325ace529b0511cf5cf0a
FIREBASE_MEASUREMENT_ID=G-7S5VG2W9PL
FINANCIAL_NEWS_API_KEY=demo
```

## Visual Guide

### Where to Find Environment Tab:
```
Render Dashboard
├── Your Service Name
    ├── Events
    ├── Logs
    ├── Shell
    ├── Metrics
    ├── Settings
    └── Environment  ← Click here!
```

### Adding a Variable:
```
1. Click "Add Environment Variable"
2. Enter Key (e.g., SECRET_KEY)
3. Enter Value (e.g., your-secret-key)
4. Click "Add" or press Enter
5. Repeat for all variables
6. Click "Save Changes" at the bottom
```

## Important Notes

### ⚠️ SECRET_KEY
- **MUST be different from your local .env**
- Use a strong random string for production
- Never share this key publicly
- Generate a new one specifically for production

### ⚠️ Firebase Configuration
- These values are from your Firebase project
- They're already set up for your project
- Don't change them unless you create a new Firebase project

### ⚠️ After Adding Variables
- Render will automatically redeploy
- Wait for deployment to complete
- Check logs for any errors
- Test the application

## Troubleshooting

### Issue: "Environment variable not found"
**Solution**: 
- Make sure you clicked "Save Changes"
- Wait for redeployment to complete
- Check spelling of variable names (case-sensitive)

### Issue: "Login not working after deployment"
**Solution**:
1. Check Firebase authorized domains:
   - Go to Firebase Console → Authentication → Settings
   - Add your Render domain: `your-app.onrender.com`
2. Verify all Firebase variables are set correctly

### Issue: "Application not starting"
**Solution**:
- Check Render logs for errors
- Verify SECRET_KEY is set
- Make sure all required variables are added

### Issue: "Can't see environment variables"
**Solution**:
- Click on "Environment" tab (not Settings)
- Scroll down to "Environment Variables" section
- If empty, start adding variables

## Verification Checklist

After adding all variables:

- [ ] All 9 variables added
- [ ] SECRET_KEY is a strong random string
- [ ] Firebase variables match your project
- [ ] Clicked "Save Changes"
- [ ] Deployment completed successfully
- [ ] Application is accessible
- [ ] Login page loads
- [ ] Can login with Firebase credentials
- [ ] Main dashboard loads after login

## Security Best Practices

✅ **DO:**
- Use different SECRET_KEY for production
- Keep environment variables private
- Rotate SECRET_KEY periodically
- Use strong random strings

❌ **DON'T:**
- Use the same SECRET_KEY as local development
- Share environment variables publicly
- Commit .env file to git
- Use weak or predictable keys

## Next Steps After Setup

1. ✅ Add all environment variables
2. ✅ Wait for deployment
3. ✅ Add your Render domain to Firebase authorized domains
4. ✅ Test login functionality
5. ✅ Test stock predictions
6. ✅ Verify all features work

## Firebase Authorized Domains Setup

After deploying to Render:

1. Go to Firebase Console: https://console.firebase.google.com/
2. Select your project: `loginapp-e7f18`
3. Go to **Authentication** → **Settings** → **Authorized domains**
4. Click **Add domain**
5. Enter your Render URL: `your-app-name.onrender.com`
6. Click **Add**

This allows Firebase authentication to work on your production domain.

## Getting Your Render URL

Your Render URL will be:
- Format: `https://your-service-name.onrender.com`
- Find it in Render dashboard at the top of your service page
- Example: `https://niveshaii.onrender.com`

## Complete Setup Flow

```
1. Deploy to Render (connect GitHub repo)
   ↓
2. Add environment variables (this guide)
   ↓
3. Wait for deployment to complete
   ↓
4. Get your Render URL
   ↓
5. Add Render URL to Firebase authorized domains
   ↓
6. Test the application
   ↓
7. Done! 🎉
```

---

**Need Help?**

If you encounter issues:
1. Check Render logs for errors
2. Verify all environment variables are set
3. Check Firebase authorized domains
4. Ensure Firebase authentication is enabled

**Your Firebase Project**: loginapp-e7f18
**Repository**: https://github.com/canvameet/niveshaii
