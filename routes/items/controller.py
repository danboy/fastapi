from db.db import db_session
from db.models.item import Item
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

class ItemsController:
    def __init__(self, session: AsyncSession = Depends(db_session)):
        self.session = session

    async def get_all_items(self) -> list[Item]:
        items = await self.session.execute(select(Item))

        return items.scalars().fetchall()

    async def create_item(self, data) -> Item:
        item = Item(**data.dict())
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)

        return item
