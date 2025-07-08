#!/usr/bin/env python3
"""
Simple test script for the Personal Assistant API
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_api():
    print("🧪 Testing Simple Personal Assistant API")
    print("=" * 50)
    
    # Test 1: Check if server is running
    print("\n1. Testing server connection...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ Server is running")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Server returned status code: {response.status_code}")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure it's running on http://localhost:8000")
        return
    
    # Test 2: Test chat endpoint without API key (should fail)
    print("\n2. Testing chat without API key...")
    chat_data = {"message": "Hello!"}
    
    try:
        response = requests.post(f"{BASE_URL}/chat", json=chat_data)
        if response.status_code == 401:
            print("✅ Authentication working - API key required")
        else:
            print(f"❌ Unexpected response: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 3: Test chat endpoint with API key
    print("\n3. Testing chat with API key...")
    headers = {"X-API-Key": "test-key-123"}
    
    try:
        response = requests.post(f"{BASE_URL}/chat", json=chat_data, headers=headers)
        if response.status_code == 200:
            print("✅ Chat successful!")
            chat_response = response.json()
            print(f"   Response: {chat_response.get('response')[:100]}...")
        elif response.status_code == 500:
            print("⚠️  Chat failed - Google API key might not be configured")
            print("   This is expected if you haven't set up your Google Gemini API key")
        else:
            print(f"❌ Chat failed: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Chat error: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 API testing completed!")
    print("\nNext steps:")
    print("1. Set up your Google Gemini API key in .env file")
    print("2. Visit http://localhost:8000/docs for interactive API documentation")
    print("3. Start chatting with your personal assistant!")

if __name__ == "__main__":
    test_api() 