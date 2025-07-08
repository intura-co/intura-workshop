# Simple Personal Assistant API with Google Gemini

A simple FastAPI tutorial application that integrates Google Gemini LLM with basic authentication.

## Features

- 🤖 Google Gemini LLM integration
- 🔐 Simple API key authentication
- 💬 Chat interface with AI responses
- 📚 Auto-generated API documentation

## Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_google_gemini_api_key_here
   ```

   **To get a Google Gemini API key:**
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the key to your `.env` file

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the API**
   - API Documentation: http://localhost:8000/docs
   - Base URL: http://localhost:8000

## API Endpoints

- `GET /` - Welcome message
- `POST /chat` - Send message to Gemini LLM (requires API key)

## Usage Example

### Chat with Gemini
```bash
curl -X POST "http://localhost:8000/chat" \
     -H "X-API-Key: your-api-key-here" \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello, how are you today?"}'
```

## Authentication

This tutorial uses simple API key authentication via the `X-API-Key` header. Any non-empty value will work for the tutorial.

## Next Steps

- Visit http://localhost:8000/docs for interactive API documentation
- Try different messages with the chat endpoint
- Explore the FastAPI documentation for more features 