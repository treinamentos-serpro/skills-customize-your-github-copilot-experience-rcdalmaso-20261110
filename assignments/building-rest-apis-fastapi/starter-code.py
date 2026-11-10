from fastapi import FastAPI, Field, HTTPException, Response
from pydantic import BaseModel

app = FastAPI(title="Item Catalog API")


class ItemInput(BaseModel):
    name: str
    description: str = ""
    price: float = Field(gt=0)


class Item(ItemInput):
    id: int


items = {
    1: {"id": 1, "name": "Notebook", "description": "A ruled notebook", "price": 3.5},
    2: {"id": 2, "name": "Pen", "description": "A blue ink pen", "price": 1.25},
}


@app.get("/items", response_model=list[Item])
def list_items():
    # Task 1: return all items.
    pass


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    # Task 1: return one item or raise HTTPException with status code 404.
    pass


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemInput):
    # Task 2: assign a new ID, save the item, and return it.
    pass


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemInput):
    # Task 2: replace an existing item or raise HTTPException with status code 404.
    pass


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    # Task 2: delete an existing item or raise HTTPException with status code 404.
    # Return Response(status_code=204) after a successful deletion.
    pass