from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/send',
    tags = ['send']
)

@router.post("/")
def send_message():
    return { "send": "message"}
