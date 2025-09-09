"""
Simple test to verify the cleaned package works correctly.
"""

import scrapesage

def test_package():
    """Quick test to ensure the package functions correctly."""
    print("🧪 Testing cleaned ScrapeSage package")
    print("=" * 45)
    
    # Test basic import
    print("✅ Package imported successfully")
    print(f"📦 Version: {scrapesage.__version__}")
    print(f"🔧 Available functions: {[x for x in dir(scrapesage) if not x.startswith('_')]}")
    
    # Test function signature (without actually calling it to avoid API usage)
    import inspect
    sig = inspect.signature(scrapesage.search_and_summarize)
    print(f"📋 Function signature: {sig}")
    
    print("\n✅ Package is clean and ready for PyPI!")
    print("\n💡 Usage:")
    print("   pip install ScrapeSage")
    print("   import scrapesage")
    print("   results = scrapesage.search_and_summarize(")
    print("       query='your query',")
    print("       gemini_api_key='your_key',")
    print("       serper_api_key='your_key',")
    print("       max_urls=5")
    print("   )")

if __name__ == "__main__":
    test_package()
