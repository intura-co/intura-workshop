from dotenv import load_dotenv
load_dotenv()


from fastapi import FastAPI, HTTPException, Depends, Header
from ai import create_retriever, predict



# Initialize FastAPI app
app = FastAPI(
    title="Simple Personal Assistant API",
    description="A simple FastAPI app with Google Gemini LLM and basic auth",
    version="1.0.0"
)

# Simple auth function - just check if API key is provided
async def verify_api_key(x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(status_code=401, detail="API key required")
    return x_api_key

retriever = create_retriever("data/katalog_tempe.pdf")
# Routes
@app.get("/")
async def root():
    return {"message": "Simple Personal Assistant API with Google Gemini"}

@app.post("/chat")
async def chat_with_gemini(
    chat_request: dict,
    api_key: str = Depends(verify_api_key)
):
    message = chat_request.get("message")
    if not message:
        raise HTTPException(status_code=400, detail="Message is required")
    
    try:
        # Generate response using Google Gemini
        response = predict(retriever=retriever, query=message)
        
        return {"response": response}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating response: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
