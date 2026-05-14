from fastapi import FastAPI
from app.routes.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health():
    return {
        "status": "ok"
    }

@app.get("/test-db")
async def test_db():
    return {"db": "ready"}

@app.get("/health")
async def health():
    return {"status": "ok"}