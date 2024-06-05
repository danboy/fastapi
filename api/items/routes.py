from .controller import ItemsController
from typing import Union

from .schemas import ItemSchema
from db.db import db_session
from db.models.item import Item
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter(
    prefix='/items',
    tags = ['items']
)

@router.get("/", response_model=list[Item])
async def get_items(
    session: AsyncSession = Depends(db_session),
) -> list[Item]:
    item_service = ItemsController(session=session)
    return await item_service.get_all_items()


@router.post("/", response_model=Item)
async def create_item(
    data: ItemSchema,
    session: AsyncSession = Depends(db_session),
) -> Item:
    item_service = ItemsController(session=session)
    item = await item_service.create_item(data)
    return item
