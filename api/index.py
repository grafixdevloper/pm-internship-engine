"""
Vercel serverless function entry point for Flask backend.
This file exports the Flask app instance for Vercel deployment.
"""

import sys
import os

# Add the backend directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app import app

# Export the app for Vercel
if __name__ == "__main__":
    app.run()