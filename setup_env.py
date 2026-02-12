#!/usr/bin/env python3
"""
Environment Setup Script for NiveshAI
Helps set up .env file with secure credentials
"""

import os
import secrets
import shutil

def generate_secret_key():
    """Generate a secure random secret key"""
    return secrets.token_hex(32)

def setup_env_file():
    """Setup .env file from .env.example"""
    print("="*70)
    print("NiveshAI - Environment Setup")
    print("="*70)
    print()
    
    # Check if .env already exists
    if os.path.exists('.env'):
        response = input(".env file already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Setup cancelled.")
            return
    
    # Check if .env.example exists
    if not os.path.exists('.env.example'):
        print("Error: .env.example file not found!")
        return
    
    # Copy .env.example to .env
    shutil.copy('.env.example', '.env')
    print("✓ Created .env file from .env.example")
    
    # Generate secure SECRET_KEY
    secret_key = generate_secret_key()
    
    # Read .env file
    with open('.env', 'r') as f:
        content = f.read()
    
    # Replace default SECRET_KEY with generated one
    content = content.replace(
        'SECRET_KEY=your-random-secret-key-change-this-in-production',
        f'SECRET_KEY={secret_key}'
    )
    
    # Write back to .env
    with open('.env', 'w') as f:
        f.write(content)
    
    print(f"✓ Generated secure SECRET_KEY: {secret_key[:20]}...")
    print()
    print("="*70)
    print("Setup Complete!")
    print("="*70)
    print()
    print("Your .env file has been created with:")
    print("  ✓ Secure SECRET_KEY (auto-generated)")
    print("  ✓ Firebase configuration (from your project)")
    print()
    print("Next steps:")
    print("  1. Install dependencies: pip install -r requirements.txt")
    print("  2. Enable Email/Password auth in Firebase Console")
    print("  3. Add users in Firebase Console → Authentication → Users")
    print("  4. Run the app: python app.py")
    print()
    print("For detailed instructions, see:")
    print("  - ENV_SETUP.md (environment variables)")
    print("  - FIREBASE_SETUP.md (Firebase configuration)")
    print("  - LOGIN_TEST_CHECKLIST.md (testing guide)")
    print()
    
    # Check if python-dotenv is installed
    try:
        import dotenv
        print("✓ python-dotenv is installed")
    except ImportError:
        print("⚠ python-dotenv not found. Install it with:")
        print("  pip install python-dotenv")
    print()

if __name__ == '__main__':
    try:
        setup_env_file()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
    except Exception as e:
        print(f"\nError: {e}")
