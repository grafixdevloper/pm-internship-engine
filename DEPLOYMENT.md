# Vercel Deployment Instructions

## 🚀 Quick Deploy to Vercel

This repository is configured for easy deployment to Vercel with both frontend and backend.

### Prerequisites
- A GitHub account
- A Vercel account (linked to GitHub)

### Deployment Steps

1. **Fork/Clone this repository** to your GitHub account
2. **Go to Vercel.com** and sign in with GitHub
3. **Click "New Project"** and import your repository
4. **Configure deployment settings:**
   - Framework Preset: **Other**
   - Root Directory: **.** (leave as default)
   - Build Command: **(leave empty or use default)**
   - Output Directory: **frontend**
   - Install Command: **(leave empty)**

5. **Click "Deploy"** - Vercel will automatically:
   - Install Python dependencies for the backend API
   - Serve the frontend as static files
   - Route API calls to the serverless backend

### 🔧 Configuration Files

This repository includes all necessary Vercel configuration:

- **`vercel.json`** - Main Vercel configuration
- **`api/index.py`** - Serverless function entry point
- **`api/requirements.txt`** - Python dependencies for API
- **`.vercelignore`** - Files to exclude from deployment
- **`package.json`** - Project metadata and scripts

### 📱 Frontend & Backend Structure

- **Frontend**: Static files in `/frontend/` directory
  - `index.html` - Main application
  - `styles.css` - Styling
  - `script.js` - JavaScript (auto-detects production API URL)

- **Backend**: Python Flask API
  - `/api/*` routes → serverless functions
  - Automatic CORS handling
  - JSON data processing

### 🌐 After Deployment

Once deployed, your application will be available at:
```
https://your-project-name.vercel.app
```

The API endpoints will be at:
```
https://your-project-name.vercel.app/api/recommend
https://your-project-name.vercel.app/api/internships
https://your-project-name.vercel.app/api/sectors
```

### 🔄 Updates

Push changes to your GitHub repository - Vercel will automatically redeploy.

### 📞 Troubleshooting

**Build fails**: Check that all Python dependencies are in `api/requirements.txt`
**API not responding**: Verify `vercel.json` routes configuration
**CORS errors**: Backend includes Flask-CORS configuration
**Frontend not loading**: Ensure `frontend/index.html` exists

### 🎯 Environment Variables (Optional)

Add environment variables in Vercel dashboard:
- Go to Project Settings → Environment Variables
- Add any needed configuration (e.g., `FLASK_ENV=production`)