import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

load_dotenv()

app = FastAPI(
    title="Decision First Runbooks API",
    description="API for managing and executing decision-first runbooks",
    version="1.0.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Frontend development server
        os.getenv("FRONTEND_URL", "http://localhost:3000"),
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Decision First Runbooks API is running!"}


@app.get("/health")
async def health_check():
    return JSONResponse(
        status_code=200,
        content={
            "ok": True,
            "data": {
                "status": "healthy",
                "service": "decision-first-runbooks-api",
                "version": "1.0.0",
            },
        },
    )


@app.get("/api/health")
async def api_health_check():
    return JSONResponse(
        status_code=200,
        content={
            "ok": True,
            "data": {
                "status": "healthy",
                "api_version": "1.0.0",
            },
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
