from db.models.shared import TimestampModel, UUIDModel

class Item(TimestampModel, UUIDModel, table=True):
    __tablename__ = "item"

    name: str
    active: bool = True

    def __repr__(self):
        return f"<Item (id: {self.id})>"
