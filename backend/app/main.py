from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="BNZFS Membership API",
    description="Membership management system for Bangladesh New Zealand Friendship Society",
    version="1.0.0"
)

# Configure CORS to allow frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js development server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "BNZFS Membership API is running", "status": "active"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "bnzfs-api"}