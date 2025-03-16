from fastapi import FastAPI
from app.routes.ingest import router as ingest_router

app = FastAPI()

# Include API routes
app.include_router(ingest_router)

@app.get("/")
def root():
    return {"message": "FastAPI is running!"}
