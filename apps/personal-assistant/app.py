import os
from fastapi import FastAPI, HTTPException, Depends, Header
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Simple Personal Assistant API",
    description="A simple FastAPI app with Google Gemini LLM and basic auth",
    version="1.0.0"
)

# Configure Google Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if GOOGLE_API_KEY:
    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        api_key=GOOGLE_API_KEY
    )
else:
    print("Warning: GOOGLE_API_KEY not found in environment variables")

# Simple auth function - just check if API key is provided
async def verify_api_key(x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(status_code=401, detail="API key required")
    return x_api_key

# Routes
@app.get("/")
async def root():
    return {"message": "Simple Personal Assistant API with Google Gemini"}

@app.post("/chat")
async def chat_with_gemini(
    chat_request: dict,
    api_key: str = Depends(verify_api_key)
):
    if not GOOGLE_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="Google API key not configured"
        )
    
    message = chat_request.get("message")
    if not message:
        raise HTTPException(status_code=400, detail="Message is required")
    
    try:
        # Generate response using Google Gemini
        response = model.invoke(message)
        
        return {"response": response.content}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating response: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
