import sqlite3
from contextlib import closing
from pathlib import Path

from fastapi import FastAPI, Field, HTTPException, Response
from pydantic import BaseModel

app = FastAPI(title="Persistent Item Catalog API")
DATABASE_PATH = Path(__file__).with_name("items.db")


class ItemInput(BaseModel):
    name: str
    description: str = ""
    price: float = Field(gt=0)


class Item(ItemInput):
    id: int


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with closing(get_connection()) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL DEFAULT '',
                price REAL NOT NULL CHECK (price > 0)
            )
            """
        )
        count = connection.execute("SELECT COUNT(*) FROM items").fetchone()[0]
        if count == 0:
            connection.executemany(
                "INSERT INTO items (name, description, price) VALUES (?, ?, ?)",
                [
                    ("Notebook", "A ruled notebook", 3.5),
                    ("Pen", "A blue ink pen", 1.25),
                ],
            )
        connection.commit()


initialize_database()


@app.get("/items", response_model=list[Item])
def list_items():
    # Task 1: select all rows from items and return them as dictionaries.
    pass


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    # Task 1: select one row by ID or raise HTTPException with status code 404.
    pass


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemInput):
    # Task 2: insert the item, then return it with the generated ID.
    pass


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemInput):
    # Task 2: update the row or raise HTTPException with status code 404.
    pass


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    # Task 2: delete the row or raise HTTPException with status code 404.
    # Return Response(status_code=204) after a successful deletion.
    pass