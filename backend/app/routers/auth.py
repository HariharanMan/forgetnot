from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserOut
from app.config import settings
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
import jwt, datetime

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
client = AsyncIOMotorClient(settings.MONGODB_URI)
db = client[settings.MONGODB_DB]

def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)})
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

@router.post("/register", response_model=UserOut)
async def register(user: UserCreate):
    if await db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email exists")
    hashed_pw = pwd_context.hash(user.password)
    doc = {"email": user.email, "hashed_pw": hashed_pw, "created_at": datetime.datetime.utcnow()}
    res = await db.users.insert_one(doc)
    return UserOut(id=str(res.inserted_id), email=user.email)

@router.post("/login")
async def login(user: UserCreate):
    db_user = await db.users.find_one({"email": user.email})
    if not db_user or not pwd_context.verify(user.password, db_user["hashed_pw"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": str(db_user["_id"])});
    return {"access_token": token, "token_type": "bearer"}
