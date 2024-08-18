from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return{
        "message" : "Server started "
    }
    
@app.get("/items/{item_id}")
async def items(item_id : int):
    return("Item id is :" , item_id)
    
