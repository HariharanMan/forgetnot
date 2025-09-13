from datetime import datetime
from bson import ObjectId

def user_doc(email: str, hashed_pw: str):
    return {
        "email": email,
        "hashed_pw": hashed_pw,
        "created_at": datetime.utcnow()
    }
