from typing import Union

from fastapi import APIRouter

router = APIRouter(
    prefix='',
    tags = ['root']
)

@router.get("/")
def read_root():
    return {"Hello": "World"}
