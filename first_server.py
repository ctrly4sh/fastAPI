from fastapi import FastAPI

app = FastAPI()

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