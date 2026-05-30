from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {
        "message": "Welcome to FastAPI"
    }



@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {
        "user_id": user_id,"name": f"User {user_id} this is a test for black so we can see if it works or not"
    }