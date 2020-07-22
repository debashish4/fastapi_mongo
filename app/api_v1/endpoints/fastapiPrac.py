from enum import IntEnum
from enum import Enum
import psutil
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from db.mongodb import mydb

class ModelName(str, Enum):
    debashish = "debashish"
    sahoo = "sahoo"
    lenet = "lenet"


class Item(BaseModel):
    name: str
    price: int
    is_offer: Optional[bool] = None

class Post_Item(BaseModel):
    id: int
    first_name: str
    last_name: str	
    email: str
    gender: str
    ip_address: str


router = APIRouter(IntEnum)

@router.get("/names/{name}")
def read_root(name: str):
    mycol = mydb["names"]
    myquery = { "name": 1 }
    print(mydb.list_collection_names() )
    mydoc = mycol.find({}, {"_id": 0, "first_name": 1, "last_name": 1})
    print(mydoc)
    for x in mydoc:
        if x.get("first_name") == name:
            return x

# GET
@router.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.debashish:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# PUT
@router.put("/update_items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": "working put", "item_id": item_id}

#POST
@router.post("/add_post/")
def save_item(item: Post_Item): 
    mycol = mydb["names"]
    # mydict = { "name": "John", "address": "Highway 37" }
    print("data is:", item.name)
    mydict = {"first_name": item.name}
    x = mycol.insert_many(mydict)
    return { "first_name": "new name", "item": item}


#DELETE
@router.delete("/delete_post/{item_id}")
def delete_item(item_id: int):
    print(item_id)
    mycol = mydb["names"]
    myquery = { "id": item_id }
    x = mycol.delete_one(myquery)
    return {}

# # PATH PARAMS WITH TYPES
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


# QUERY PARAMS
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@router.get("/items_query/")
def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]



