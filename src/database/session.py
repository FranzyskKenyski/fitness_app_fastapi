from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from src.core.config import settings


async_engine = create_async_engine(settings.DATABASE_URL, echo=True)
async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

async def get_db_session_async():
    async with async_session_factory() as session:
        try:
            yield session
        finally:
            await session.close()
