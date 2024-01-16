import datetime
from dataclasses import dataclass, asdict
from typing import Any, Mapping
from pymongo.collection import Collection
import uuid


@dataclass
class Record:
    user_uid: uuid.UUID 
    detail: str
    category: str
    price: int | str
    date: datetime.datetime


@dataclass(frozen=True)
class SpendDBManager:
    """ Manager for working with spend record's collection """
    records: Collection

    def select_one(self, **kwargs) -> Record | None:
        """"""
        record: Mapping[str, Any] | None = self.records.find_one(kwargs)
        return Record(
            user_uid=record.get("user_uid"),
            detail=record.get("detail"),
            category=record.get("category"),
            price=record.get("price"),
            date=record.get("date"),
        ) if record else None

    def insert(self, record: Record):
        return self.records.insert_one(asdict(record)).inserted_id

