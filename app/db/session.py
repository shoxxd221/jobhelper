from typing import AsyncGenerator

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

import settings


engine = create_async_engine(
    settings.DATABASE_URL,
    future=True,
    echo=True,
    execution_options={"isolation_level": "AUTOCOMMIT"},
)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    date_publication = Column(DateTime, nullable=False)
    title = Column(String, nullable=False)
