from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Welcome to FastAPI"}


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": f"User {user_id} this is a test for black so we can see if it works or not",
    }


@app.post("/items/")
async def create_item(name: str, description: str = None, price: float = 0.0):
    return {
        "name": name,
        "description": description,
        "price": price,
        "status": "Item created successfully",
    }


@app.get("/raw/")
async def raw():
    return PlainTextResponse(
        "This is a plain text response from /raw/ endpoint aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    )


# New API endpoint
@app.get("/status/")
async def status():
    return {"status": "ok", "message": "API is running"}
