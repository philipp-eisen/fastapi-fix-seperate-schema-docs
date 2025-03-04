from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict


class Item(BaseModel):
    model_config = ConfigDict(json_schema_serialization_defaults_required=True)

    name: str
    description: Union[str, None] = None


app = FastAPI(separate_input_output_schemas=False)


@app.post("/items/")
def create_item(item: Item):
    return item


@app.get("/items/")
def read_items() -> List[Item]:
    return [
        Item(
            name="Portal Gun",
            description="Device to travel through the multi-rick-verse",
        ),
        Item(name="Plumbus"),
    ]
