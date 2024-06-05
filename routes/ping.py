from typing import Union

from fastapi import APIRouter

router = APIRouter(
    prefix='/ping',
    tags = ['ping']
)

@router.get("")
def read_root():
    return {"Ping": "Pong"}
