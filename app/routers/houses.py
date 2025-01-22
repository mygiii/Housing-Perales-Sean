from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.models import House
from app.schemas import House, HouseCreate

router = APIRouter()

@router.get("/houses", response_model=list[House])
async def get_houses(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(House))
    return result.scalars().all()

@router.post("/houses", response_model=House)
async def create_house(house: HouseCreate, db: AsyncSession = Depends(get_db)):
    new_house = House(**house.dict())
    db.add(new_house)
    await db.commit()
    await db.refresh(new_house)
    return new_house

