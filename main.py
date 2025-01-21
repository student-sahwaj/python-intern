from fastapi import FastAPI
from app.auth.routes import auth_router
from app.watchlist.routes import watchlist_router
from app.core.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Stock Watchlist App", version="1.0.0")

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(watchlist_router, prefix="/watchlist", tags=["Watchlist"])
