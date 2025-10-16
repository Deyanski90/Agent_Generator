"""
Quick verification script to check if everything is set up correctly
"""

import sys
import os

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python version: {version.major}.{version.minor}.{version.micro}")
        print("   Required: Python 3.8 or higher")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    required = ['langchain', 'langchain_openai', 'pydantic', 'openai']
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print(f"✅ {package} installed")
        except ImportError:
            print(f"❌ {package} NOT installed")
            missing.append(package)
    
    if missing:
        print(f"\n💡 Install missing packages with: pip install -r requirements.txt")
        return False
    return True

def check_api_key():
    """Check if OpenAI API key is configured"""
    api_key = os.getenv('OPENAI_API_KEY')
    
    if api_key:
        # Show only first and last 4 characters for security
        masked_key = f"{api_key[:7]}...{api_key[-4:]}"
        print(f"✅ OpenAI API Key found: {masked_key}")
        return True
    else:
        print("❌ OpenAI API Key NOT found")
        print("\n💡 Set it with:")
        print("   export OPENAI_API_KEY='sk-your-key-here'  # Mac/Linux")
        print("   set OPENAI_API_KEY=sk-your-key-here       # Windows CMD")
        print("   $env:OPENAI_API_KEY='sk-your-key-here'    # Windows PowerShell")
        return False

def test_basic_functionality():
    """Try to import and initialize the test generator"""
    try:
        from test_case_generator import TestCaseGenerator
        print("✅ Test case generator module loaded successfully")
        
        # Try to initialize (this will check API key)
        try:
            generator = TestCaseGenerator()
            print("✅ Test case generator initialized successfully")
            return True
        except ValueError as e:
            print(f"❌ Initialization failed: {str(e)}")
            return False
            
    except Exception as e:
        print(f"❌ Failed to load module: {str(e)}")
        return False

def main():
    """Run all verification checks"""
    print("="*60)
    print("🔍 Verifying Test Case Generator Setup")
    print("="*60 + "\n")
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("API Key", check_api_key),
        ("Basic Functionality", test_basic_functionality),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n📋 Checking {name}...")
        results.append(check_func())
        print()
    
    print("="*60)
    if all(results):
        print("✅ ALL CHECKS PASSED! You're ready to generate test cases!")
        print("\n🚀 Run: python test_case_generator.py")
    else:
        print("❌ SOME CHECKS FAILED. Please fix the issues above.")
        failed_count = len([r for r in results if not r])
        print(f"\n   {failed_count} issue(s) found")
    print("="*60)

if __name__ == "__main__":
    main()