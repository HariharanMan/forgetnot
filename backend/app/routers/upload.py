from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from app.config import settings
from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorGridFSBucket

router = APIRouter()
client = AsyncIOMotorClient(settings.MONGODB_URI)
db = client[settings.MONGODB_DB]

@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    if file.content_type not in ["audio/mpeg", "audio/wav"]:
        raise HTTPException(status_code=400, detail="Invalid audio format")
    contents = await file.read()
    fs = AsyncIOMotorGridFSBucket(db)
    upload_stream = fs.open_upload_stream(file.filename, metadata={"content_type": file.content_type})
    await upload_stream.write(contents)
    await upload_stream.close()
    audio_id = upload_stream._id
    return {"audio_id": str(audio_id)}
