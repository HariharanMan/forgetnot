from datetime import datetime

def reminder_doc(user_id, note_id, remind_at):
    return {
        "user_id": user_id,
        "note_id": note_id,
        "remind_at": remind_at,
        "created_at": datetime.utcnow()
    }
