# workout_api/atleta/router.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_atletas():
    return {"message": "List of atletas"}

@router.post("/")
async def create_atleta():
    return {"message": "Create atleta"}
