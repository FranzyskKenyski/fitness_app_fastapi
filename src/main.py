import uvicorn
from fastapi import FastAPI
from src.api.v1.router import api_router
from src.core.config import settings

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

app = FastAPI(
    title="Fitness Tracker",
    version="0.1",
    openapi_url="/fitness-tracker/openapi.json",
)
app.include_router(api_router)




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, log_level="error")