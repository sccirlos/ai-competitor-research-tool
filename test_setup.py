#!/usr/bin/env python3
"""
Pre-Deployment Test Script
Run this before deploying to verify everything is configured correctly.
"""

import os
import sys
from pathlib import Path

def test_files_exist():
    """Check that all required files are present"""
    print("🔍 Checking required files...")
    
    required_files = [
        "streamlit_app.py",
        "deepcomp_enhanced.py",
        "compile_to_csv_enhanced.py",
        "requirements.txt",
        ".gitignore",
        "README.md"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
            print(f"   ❌ Missing: {file}")
        else:
            print(f"   ✅ Found: {file}")
    
    if missing_files:
        print(f"\n❌ {len(missing_files)} required file(s) missing!")
        return False
    else:
        print("\n✅ All required files present!")
        return True

def test_env_file():
    """Check if .env file exists and has API key"""
    print("\n🔍 Checking environment configuration...")
    
    if not os.path.exists(".env"):
        print("   ⚠️  No .env file found (needed for local development)")
        print("   Create .env with: FIRECRAWL_API_KEY=your_key_here")
        return False
    
    with open(".env", "r") as f:
        content = f.read()
        
    if "FIRECRAWL_API_KEY" not in content:
        print("   ❌ .env file exists but FIRECRAWL_API_KEY not found")
        return False
    
    if "your_" in content or "placeholder" in content.lower():
        print("   ⚠️  .env file has placeholder value - replace with real API key")
        return False
    
    print("   ✅ .env file configured!")
    return True

def test_gitignore():
    """Check that .gitignore properly excludes sensitive files"""
    print("\n🔍 Checking .gitignore configuration...")
    
    if not os.path.exists(".gitignore"):
        print("   ⚠️  No .gitignore file found!")
        return False
    
    with open(".gitignore", "r") as f:
        content = f.read()
    
    required_ignores = [".env", "outputs/", "__pycache__"]
    missing_ignores = []
    
    for item in required_ignores:
        if item not in content:
            missing_ignores.append(item)
            print(f"   ⚠️  .gitignore missing: {item}")
        else:
            print(f"   ✅ .gitignore includes: {item}")
    
    if missing_ignores:
        print(f"\n⚠️  Consider adding these to .gitignore: {', '.join(missing_ignores)}")
        return False
    
    print("\n✅ .gitignore properly configured!")
    return True

def test_imports():
    """Test that required Python packages can be imported"""
    print("\n🔍 Checking Python dependencies...")
    
    required_packages = {
        "streamlit": "streamlit",
        "pandas": "pandas",
        "dotenv": "python-dotenv",
        "firecrawl": "firecrawl-py",
        "pydantic": "pydantic"
    }
    
    missing_packages = []
    
    for package, pip_name in required_packages.items():
        try:
            __import__(package)
            print(f"   ✅ {package} installed")
        except ImportError:
            missing_packages.append(pip_name)
            print(f"   ❌ {package} not installed")
    
    if missing_packages:
        print(f"\n❌ Missing packages! Install with:")
        print(f"   pip install {' '.join(missing_packages)}")
        return False
    
    print("\n✅ All dependencies installed!")
    return True

def test_api_key():
    """Test that API key is accessible"""
    print("\n🔍 Checking API key accessibility...")
    
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv("FIRECRAWL_API_KEY")
        
        if not api_key:
            print("   ❌ FIRECRAWL_API_KEY not found in environment")
            return False
        
        if api_key.startswith("your_") or "placeholder" in api_key.lower():
            print("   ❌ API key appears to be a placeholder")
            return False
        
        print(f"   ✅ API key found (length: {len(api_key)})")
        return True
        
    except Exception as e:
        print(f"   ❌ Error loading API key: {e}")
        return False

def test_script_imports():
    """Test that custom scripts can be imported"""
    print("\n🔍 Checking custom script imports...")
    
    try:
        from deepcomp_enhanced import DeepCompScraper, COMPETITORS
        print("   ✅ deepcomp_enhanced.py imports successfully")
        print(f"   ✅ Found {len(COMPETITORS)} competitors configured")
    except Exception as e:
        print(f"   ❌ Error importing deepcomp_enhanced.py: {e}")
        return False
    
    try:
        from compile_to_csv_enhanced import compile_json_to_csv
        print("   ✅ compile_to_csv_enhanced.py imports successfully")
    except Exception as e:
        print(f"   ❌ Error importing compile_to_csv_enhanced.py: {e}")
        return False
    
    print("\n✅ Custom scripts import successfully!")
    return True

def main():
    """Run all tests"""
    print("=" * 60)
    print("🧪 Pre-Deployment Test Suite")
    print("=" * 60)
    
    results = []
    
    # Run all tests
    results.append(("Files", test_files_exist()))
    results.append(("Environment", test_env_file()))
    results.append((".gitignore", test_gitignore()))
    results.append(("Dependencies", test_imports()))
    results.append(("API Key", test_api_key()))
    results.append(("Script Imports", test_script_imports()))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\n{passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! You're ready to:")
        print("   1. Test locally: streamlit run streamlit_app.py")
        print("   2. Push to GitHub (without .env!)")
        print("   3. Deploy on Streamlit Cloud")
        print("\nSee DEPLOYMENT_GUIDE.md for detailed instructions.")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above before deploying.")
        print("   See README.md for setup instructions.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
