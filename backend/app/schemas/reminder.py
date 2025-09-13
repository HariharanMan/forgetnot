from pydantic import BaseModel

class ReminderOut(BaseModel):
    id: str
    user_id: str
    note_id: str
    remind_at: str
