#!/usr/bin/env python3
"""
Build and publish script for ScrapeSage package.
"""

import subprocess
import sys
import os
import shutil

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n📦 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def clean_build():
    """Clean previous build artifacts."""
    print("\n🧹 Cleaning previous build artifacts...")
    dirs_to_clean = ['build', 'dist', 'scrapesage.egg-info']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"   Removed {dir_name}/")

def main():
    """Main build function."""
    print("ScrapeSage - Build & Publish Script")
    print("=" * 45)
    
    # Check if we're in the right directory
    if not os.path.exists("pyproject.toml"):
        print("❌ Error: pyproject.toml not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Clean previous builds
    clean_build()
    
    # Install build dependencies
    success = run_command(
        "pip install build twine", 
        "Installing build dependencies"
    )
    
    if not success:
        print("\n❌ Failed to install build dependencies.")
        sys.exit(1)
    
    # Build the package
    success = run_command(
        "python -m build", 
        "Building the package"
    )
    
    if not success:
        print("\n❌ Failed to build the package.")
        sys.exit(1)
    
    # Check the package
    success = run_command(
        "python -m twine check dist/*", 
        "Checking the built package"
    )
    
    if not success:
        print("\n❌ Package check failed.")
        sys.exit(1)
    
    print("\n" + "=" * 45)
    print("✅ Package built successfully!")
    print("\n📁 Built files:")
    if os.path.exists("dist"):
        for file in os.listdir("dist"):
            print(f"   - dist/{file}")
    
    print("\n📝 Next steps:")
    print("1. Test the package locally:")
    print("   pip install dist/akillabs_scraper-1.0.0-py3-none-any.whl")
    print("\n2. Upload to Test PyPI:")
    print("   python -m twine upload --repository testpypi dist/*")
    print("\n3. Upload to PyPI:")
    print("   python -m twine upload dist/*")
    print("\n4. Install from PyPI:")
    print("   pip install akillabs-scraper")

if __name__ == "__main__":
    main()
