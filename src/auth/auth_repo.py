from sqlalchemy.ext.asyncio import AsyncSession


class AuthRepository:
    def __init__(self, session):
        self.session = session

    async def create_access_token(self, identity):
        pass

