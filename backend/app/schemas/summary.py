from pydantic import BaseModel

class SummaryOut(BaseModel):
    id: str
    note_id: str
    text: str
    summary: str
    sentiment: str
