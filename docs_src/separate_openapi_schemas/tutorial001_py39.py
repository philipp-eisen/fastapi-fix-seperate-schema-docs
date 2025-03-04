from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict


class Item(BaseModel):
    model_config = ConfigDict(json_schema_serialization_defaults_required=True)

    name: str
    description: Optional[str] = None


app = FastAPI()


@app.post("/items/")
def create_item(item: Item):
    return item


@app.get("/items/")
def read_items() -> list[Item]:
    return [
        Item(
            name="Portal Gun",
            description="Device to travel through the multi-rick-verse",
        ),
        Item(name="Plumbus"),
    ]
