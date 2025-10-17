
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from datetime import datetime, timedelta
import uvicorn

app = FastAPI()

# Sample document data
documents = [
    {
        "documentId": "doc001",
        "documentType": "PDF",
        "url": "https://example.com/doc001.pdf"
    },
    {
        "documentId": "doc002",
        "documentType": "Word",
        "url": "https://example.com/doc002.docx"
    },
    {
        "documentId": "doc003",
        "documentType": "Excel",
        "url": "https://example.com/doc003.xlsx"
    },
]

# Rate limit config
RATE_LIMIT = 5  # max requests
WINDOW_SECONDS = 60  # time window in seconds

# In-memory store for rate limiting
rate_limit_store = {}


@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host
    now = datetime.now()  # FIX: get the current time

    # Initialize or clean up old entries
    if client_ip not in rate_limit_store:
        rate_limit_store[client_ip] = []
    rate_limit_store[client_ip] = [
        t for t in rate_limit_store[client_ip]
        if now - t < timedelta(seconds=WINDOW_SECONDS)
    ]

    # Check rate limit
    if len(rate_limit_store[client_ip]) >= RATE_LIMIT:
        return JSONResponse(
            status_code=429,
            content={"detail": "Rate limit exceeded. Try again later."}
        )

    # Record request time
    rate_limit_store[client_ip].append(now)
    response = await call_next(request)
    return response


@app.get("/documents", response_model=List[dict])
async def get_documents():
    return documents


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
