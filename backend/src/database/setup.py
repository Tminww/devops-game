from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.config import settings

import logging

logging.basicConfig(
    filename="./src/log/sqlalchemy.log",
    filemode="a",
    format="[%(asctime)s] [%(name)s] [%(levelname)s] > %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)
# logging.getLogger("sqlalchemy.orm").setLevel(logging.INFO)


async_engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True,
)

async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_async_session():
    async with async_session_maker() as session:
        yield session
