from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str , Enum):
    llama = "Llama"
    GptOmni = "gpt-4O"


@app.get('/')
async def root(): 
    return{
        "message" : "landing page endpoint"
    }

@app.get('/home')
async def home():
    return {    
        "String": "home endpoint"
    }

#endpoint parameteres

@app.get("/path_params/{name}")
async def endpoint_params(name : str):
    return {
        "enpoint params : name" : name
    }

#path operations 
@app.get('/users/me') #this should be declared earlier 
async def usersMe():
    return {
        "endpoint" : "user/me : current user"
    }

@app.get("/users/{user_id}")
async def read_user(user_id : str):
    return {
        "user" : user_id
    }

@app.get('/twovalues')
async def val():
    return ["Ooga" , "booga"]

@app.get('/models/{models_name}')
async def models(models_name : ModelName):
    if models_name is ModelName.GptOmni:
        return {
            "model name" : models_name,
            "message" : "chat gpt o" 
        }
    if models_name is ModelName.llama:
        return {
            "model name" : models_name,
            "message" : "facebook model"
        }
