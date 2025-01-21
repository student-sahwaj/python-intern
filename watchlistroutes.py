from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.watchlist.models import Watchlist
from app.core.database import get_db
from app.auth.oauth import google

watchlist_router = APIRouter()

@watchlist_router.post("/")
async def create_watchlist_entry(data: dict, db: Session = Depends(get_db)):
    new_entry = Watchlist(**data)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@watchlist_router.get("/")
async def list_watchlist(db: Session = Depends(get_db)):
    return db.query(Watchlist).all()
