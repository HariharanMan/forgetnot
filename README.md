# 🧠 ForgetNot – Backend

A FastAPI + MongoDB backend for **ForgetNot**, the mindful voice-based journaling and reminder app.  
This service handles user authentication, audio uploads, AI-powered transcriptions/summaries, and gentle reminder management.

---

## ✨ Features

- **Voice Upload & Storage**  
  Upload audio notes (MP3/WAV) stored in MongoDB GridFS.

- **AI Transcription & Summaries**  
  Endpoints ready to integrate with Whisper/OpenAI/Google APIs for real-time or post-processing transcription and summarization.

- **Reminders & Journals**  
  CRUD operations for journals, notes, and gentle reminders.

- **Authentication**  
  JWT-based signup/login.

- **Async & Scalable**  
  FastAPI + Motor (async MongoDB driver) for high concurrency.

---

## 🏗️ Tech Stack

| Layer           | Technology |
|-----------------|------------|
| Framework       | [FastAPI](https://fastapi.tiangolo.com/) |
| Database        | [MongoDB](https://www.mongodb.com/) with [Motor](https://motor.readthedocs.io/) |
| Storage         | GridFS for audio files |
| Auth            | JSON Web Tokens (JWT) |
| Containerization | Docker & docker-compose |

---

## 📂 Project Structure

forgetnot-backend/
├─ app/
│ ├─ main.py # Entry point
│ ├─ config.py # Environment settings
│ ├─ models/ # Pydantic models
│ ├─ routers/ # API routes (auth, notes, upload)
│ ├─ services/ # Helper functions (AI summary, etc.)
│ └─ db/ # Mongo connection & init
├─ tests/
│ └─ ... # Pytest unit/integration tests
├─ .env.example # Sample environment variables
├─ Dockerfile
├─ docker-compose.yml
└─ requirements.txt

yaml
Copy code

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/forgetnot-backend.git
cd forgetnot-backend
2️⃣ Create Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Environment Variables
Create a .env file (or copy .env.example) and set:

ini
Copy code
MONGO_URI=mongodb://localhost:27017/forgetnot
JWT_SECRET=<your-secret-key>
OPENAI_API_KEY=<optional-for-transcription>
5️⃣ Run MongoDB
Use Docker (recommended):

bash
Copy code
docker-compose up -d
6️⃣ Start the Server
bash
Copy code
uvicorn app.main:app --reload
API will be available at http://localhost:8000

🧪 Running Tests
bash
Copy code
pytest
🚀 Deployment
Docker: Build and run the image:

bash
Copy code
docker build -t forgetnot-backend .
docker run -d -p 8000:8000 --env-file .env forgetnot-backend
Cloud Options: Compatible with services like Render, Railway, AWS ECS/Fargate.

🔗 Key Endpoints (MVP)
Method	Endpoint	Description
POST	/auth/register	Create new user
POST	/auth/login	Get JWT token
POST	/upload	Upload audio file
POST	/transcribe	Transcribe & summarize audio
GET	/notes	Fetch all notes/reminders for a user
PUT	/notes/{id}	Update a note/reminder
DELETE	/notes/{id}	Delete a note/reminder

Swagger docs are auto-generated at /docs.

🛣️ Roadmap
 Sentiment detection & mood analytics

 Voice-command search (“What did I say last Sunday?”)

 Push notifications & gentle quote reminders

 Multi-language transcription

🤝 Contributing
Fork the repo

Create a feature branch: git checkout -b feature/your-feature

Commit changes: git commit -m "Add new feature"

Push branch: git push origin feature/your-feature

Submit a Pull Request

📜 License
MIT

ForgetNot – Help your mind breathe. Nothing forgotten, everything gently cared for.

yaml
Copy code

---

### Tips
- Replace `<your-username>` with your GitHub handle.
- Add badges (CI, coverage) when ready.
- If you integrate OpenAI/Whisper later, update **Setup & Installation** with any extra API keys.







Ask ChatGPT
