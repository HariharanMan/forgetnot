from datetime import datetime

def voice_note_doc(user_id, audio_id, note_type):
    return {
        "user_id": user_id,
        "audio_id": audio_id,
        "note_type": note_type,  # journal/reminder/todo
        "created_at": datetime.utcnow()
    }
