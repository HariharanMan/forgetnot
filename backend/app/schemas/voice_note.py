from pydantic import BaseModel

class VoiceNoteOut(BaseModel):
    id: str
    user_id: str
    note_type: str
    audio_id: str
