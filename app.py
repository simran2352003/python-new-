from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List
import uvicorn


app = FastAPI()

@app.get("/")
def read_roots():
    return {"message": "Welcome to FastAPI"}

item_db = {"name":"simran", "course":"MCA","college":"govt.college una"}
class item(BaseModel):
    name:str
    course:str
    college:str
@app.post("/user")
def create_user(user:item):
    return item


@app.get("items/{user_id}") 
def read_item (user_id:int):
    for item in item_db:
        if item["name"]==user_id:
            return item
        


@app.get("/search")
def search(q:str):
    return {"query": q}        

@app.post("/add_item")
def create_item(item:item):
    item_db.append(item.dict())
    return item


@app.get("/users")
def read_items():
    return item_db
    
@app.get("/users/{user_id}")
def read_item(item_id:int):
        for item in item_db:
            if item["college"]==item_id:
                return item
        raise HTTPException(status_code=404,detail="Item not found")
@app.post("/add_item")
def create_item(item:item):
     item_db.append(item.dict())
     return item
@app.put("/update/{user_id}")
def update_item(item_id:str,item):
    for i,db_item in enumerate(item_db):
        if db_item["ID"]==item_id:
               item_db[i]=item.dict()
        return {"message":"Item updated sucessfully "}
    raise HTTPException(status_code=404,detail="item not found")


@app.delete("/delete/{user_id}")
def delete_data(item_id:str):
    for i,db_item in enumerate(item_db):
        if db_item["name"]==item_id:
            del item_db[i]
            return {"message":"item deleted successfully"}
    raise HTTPException(status_code=404,detail="item not found")

@app.post("/uploadfile/")
def create_upload_file(file:UploadFile=File(...)):
    return{"filename":file.filename,"content_type":file.content_type}


if __name__=="__main__":
  import uvicorn
  uvicorn.run(app,host="127.0.0.1",port=8000)


     