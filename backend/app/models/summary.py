from datetime import datetime

def summary_doc(note_id, text, summary, sentiment):
    return {
        "note_id": note_id,
        "text": text,
        "summary": summary,
        "sentiment": sentiment,
        "created_at": datetime.utcnow()
    }
