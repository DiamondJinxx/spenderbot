import datetime
from dataclasses import dataclass, field, asdict
from typing import Any, Mapping
from pymongo import MongoClient
from pymongo.collection import Collection
import uuid



from config import db_config

client = MongoClient(db_config.mongo_uri)
db = client.test_database

documents = db.documents
# test_document = {
#     "id": str(uuid.uuid4()),
#     "title": "test title",
#     "body": "test body"
# }
# id = documents.insert_one(test_document).inserted_id
# print(f"inserting record {id}")

selected_record = documents.find_one(
    {
        "id": "4f945c4f-8fd0-49ae-82f2-859df2822ff2"
    }
)
print(selected_record)
#


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
        return documents.insert_one(asdict(record)).inserted_id


manager = SpendDBManager(db.documents)
rec = Record(
    user_uid=uuid.uuid4(),
    detail="Чипсы",
    category="Вредное",
    price=420,
    date=datetime.datetime.now()
)
# inserted_id = manager.insert(rec)

