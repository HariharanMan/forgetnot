from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
class TranscribeRequest(BaseModel):
    audio_id: str
    text: str
    summary: str
    sentiment: str
from app.config import settings
from motor.motor_asyncio import AsyncIOMotorClient
import datetime

router = APIRouter()
client = AsyncIOMotorClient(settings.MONGODB_URI)
db = client[settings.MONGODB_DB]

@router.get("/debug/voice_notes")
async def debug_voice_notes():
    notes = await db.voice_notes.find().to_list(100)
    return [{"_id": str(n["_id"]), "user_id": n.get("user_id"), "audio_id": n.get("audio_id"), "note_type": n.get("note_type")} for n in notes]

@router.get("/debug/summaries")
async def debug_summaries():
    summaries = await db.summaries.find().to_list(100)
    return [{"_id": str(s["_id"]), "note_id": s.get("note_id"), "text": s.get("text"), "summary": s.get("summary"), "sentiment": s.get("sentiment")} for s in summaries]

@router.post("/transcribe")
async def transcribe(req: TranscribeRequest):
    note = await db.voice_notes.find_one({"audio_id": req.audio_id})
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    doc = {
        "note_id": str(note["_id"]),
        "text": req.text,
        "summary": req.summary,
        "sentiment": req.sentiment,
        "created_at": datetime.datetime.utcnow()
    }
    res = await db.summaries.insert_one(doc)
    return {"summary_id": str(res.inserted_id)}

@router.get("/transcribe/{audio_id}")
async def get_transcription(audio_id: str):
    note = await db.voice_notes.find_one({"audio_id": audio_id})
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    summary = await db.summaries.find_one({"note_id": str(note["_id"])});
    if not summary:
        raise HTTPException(status_code=404, detail="Transcription not found")
    return {
        "note_id": summary["note_id"],
        "text": summary["text"],
        "summary": summary["summary"],
        "sentiment": summary["sentiment"]
    }

@router.get("/notes")
async def get_notes(user_id: str, note_type: str = Query(None)):
    query = {"user_id": user_id}
    if note_type:
        query["note_type"] = note_type
    notes = await db.voice_notes.find(query).to_list(100)
    return [{"id": str(n["_id"]), "audio_id": n["audio_id"], "note_type": n["note_type"]} for n in notes]
