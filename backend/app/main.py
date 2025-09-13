from fastapi import FastAPI
from app.routers import auth, upload, notes

app = FastAPI(title="ForgetNot API")

app.include_router(auth.router, prefix="/auth")
app.include_router(upload.router)
app.include_router(notes.router)
