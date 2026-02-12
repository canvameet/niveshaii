# Unified Server - Single Port Architecture

## Overview

`server.py` now handles BOTH frontend and backend on a single port (5000), eliminating the need for `app.py`.

## Architecture

### Before (Two Servers)
```
app.py (Port 8080)     →  Frontend (HTML/CSS/JS)
server.py (Port 5000)  →  Backend API (ML predictions)
```

### After (One Server) ✅
```
server.py (Port 5000)  →  Frontend + Backend + Authentication
```

## Benefits

✅ **Simpler deployment** - Only one server to manage  
✅ **No CORS issues** - Same origin for frontend and backend  
✅ **Easier development** - Single command to start everything  
✅ **Better performance** - No cross-server communication overhead  
✅ **Unified authentication** - Session management in one place  

## How It Works

### Frontend Routes (HTML Pages)
```python
@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
```

### Authentication API
```python
@app.route('/api/verify-token', methods=['POST'])
def verify_token():
    # Create Flask session after Firebase auth
    
@app.route('/api/firebase-config', methods=['GET'])
def get_firebase_config():
    # Serve Firebase config from environment variables
```

### Backend API (ML Predictions)
```python
@app.route('/api/predict', methods=['POST'])
def predict():
    # Stock predictions

@app.route('/api/visualizations', methods=['POST'])
def get_visualizations():
    # Charts and graphs

@app.route('/api/orderbook/<ticker>', methods=['GET'])
def get_orderbook(ticker):
    # Real-time order book data
```

## Running the Application

### Single Command
```bash
python server.py
```

That's it! The server will:
1. Load environment variables from `.env`
2. Start on port 5000
3. Serve frontend at `http://localhost:5000`
4. Handle API requests at `http://localhost:5000/api/*`
5. Automatically open browser

### Output
```
======================================================================
NIVESHAI - UNIFIED SERVER (Frontend + Backend)
======================================================================

Frontend Routes:
  GET  /                         - Main dashboard (requires login)
  GET  /login                    - Login page
  GET  /logout                   - Logout

Authentication API:
  POST /api/verify-token         - Verify Firebase token
  GET  /api/firebase-config      - Get Firebase configuration

Backend API Endpoints:
  POST /api/predict              - Predict custom tickers
  POST /api/popular-stocks       - Get popular stocks
  GET  /api/macro-events         - Get macro calendar events
  POST /api/visualizations       - Get model visualizations
  GET  /api/categories           - List all categories
  GET  /api/health               - Health check
  POST /api/clear-cache          - Clear model cache
  GET  /api/orderbook/<ticker>   - Get order book data
======================================================================

Server starting on http://0.0.0.0:5000
Access the application at: http://localhost:5000
======================================================================
```

## URL Structure

| URL | Purpose | Authentication |
|-----|---------|----------------|
| `http://localhost:5000/` | Main dashboard | Required |
| `http://localhost:5000/login` | Login page | Public |
| `http://localhost:5000/logout` | Logout | Public |
| `http://localhost:5000/api/*` | Backend API | Session-based |

## API Base URL

The frontend automatically detects the correct API base URL:

```javascript
const API_BASE = window.location.hostname === 'localhost' 
    ? 'http://localhost:5000/api'
    : window.location.origin + '/api';
```

This works for both:
- **Local development**: `http://localhost:5000/api`
- **Production**: `https://your-domain.com/api`

## File Changes

### Modified Files
- ✅ `server.py` - Added frontend routes and authentication
- ✅ `templates/index.html` - Already configured for port 5000

### Deprecated Files
- ❌ `app.py` - No longer needed (functionality merged into server.py)

## Development Workflow

### 1. Setup Environment
```bash
# Install dependencies
pip install -r requirements.txt

# Setup environment variables
python setup_env.py
```

### 2. Configure Firebase
- Enable Email/Password authentication
- Add authorized users
- Environment variables already set in `.env`

### 3. Start Server
```bash
python server.py
```

### 4. Access Application
Browser will automatically open to `http://localhost:5000`

## Production Deployment

### Render.com Configuration

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
python server.py
```

**Environment Variables:**
Set all variables from `.env` in Render dashboard:
- `SECRET_KEY`
- `FIREBASE_API_KEY`
- `FIREBASE_AUTH_DOMAIN`
- `FIREBASE_PROJECT_ID`
- `FIREBASE_STORAGE_BUCKET`
- `FIREBASE_MESSAGING_SENDER_ID`
- `FIREBASE_APP_ID`
- `FIREBASE_MEASUREMENT_ID`

### Port Configuration
Render automatically assigns a port via `$PORT` environment variable. Update server.py if needed:

```python
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

## Testing

### 1. Test Frontend
- Visit `http://localhost:5000`
- Should redirect to `/login`
- Login with Firebase credentials
- Should see main dashboard

### 2. Test API
```bash
# Health check
curl http://localhost:5000/api/health

# Firebase config
curl http://localhost:5000/api/firebase-config
```

### 3. Test Authentication
1. Login at `/login`
2. Access `/` - should work
3. Logout at `/logout`
4. Try to access `/` - should redirect to login

## Troubleshooting

### Issue: "Address already in use"
**Solution**: Port 5000 is already in use
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

### Issue: "ModuleNotFoundError: No module named 'dotenv'"
**Solution**: Install dependencies
```bash
pip install python-dotenv
```

### Issue: Templates not found
**Solution**: Ensure `templates/` folder exists with `index.html` and `login.html`

### Issue: Static files not loading
**Solution**: Check `static/` folder exists (if you have static assets)

## Migration from Two Servers

If you were using `app.py` + `server.py`:

### Old Way
```bash
# Terminal 1
python app.py      # Port 8080

# Terminal 2
python server.py   # Port 5000
```

### New Way ✅
```bash
# Single terminal
python server.py   # Port 5000 (everything)
```

### Update Your Workflow
1. ✅ Stop using `app.py`
2. ✅ Only run `python server.py`
3. ✅ Access at `http://localhost:5000` (not 8080)
4. ✅ Update any documentation/scripts

## Advantages Summary

| Feature | Two Servers | Unified Server |
|---------|-------------|----------------|
| Commands to start | 2 | 1 |
| Ports to manage | 2 | 1 |
| CORS configuration | Required | Not needed |
| Session management | Complex | Simple |
| Deployment complexity | Higher | Lower |
| Development speed | Slower | Faster |

---

**Status**: Server successfully unified! 🚀

Run `python server.py` and access everything at `http://localhost:5000`
