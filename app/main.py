from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User
from app.schemas import UserCreate, UserResponse

app = FastAPI()


@app.post("/users", response_model=UserResponse)
async def create_user(
    payload: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    user = User(
        name=payload.name,
        email=payload.email,
    )

    db.add(user)

    await db.commit()
    await db.refresh(user)

    return user


@app.get("/users", response_model=list[UserResponse])
async def get_users(
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(User))

    return result.scalars().all()
