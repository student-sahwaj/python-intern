from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import RedirectResponse
from app.auth.oauth import google
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.auth.models import User

auth_router = APIRouter()

@auth_router.get("/google/login")
async def google_login():
    redirect_uri = "http://localhost:8000/auth/google/callback"
    return await google.authorize_redirect(redirect_uri)

@auth_router.get("/google/callback")
async def google_callback(db: Session = Depends(get_db)):
    token = await google.authorize_access_token()
    user_info = await google.get("userinfo", token=token)
    if not user_info:
        raise HTTPException(status_code=400, detail="Google authentication failed")

    # Process user info
    # Save or update user in the database
    return {"user": user_info.json()}
