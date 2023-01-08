import asyncpg
import asyncio
import os

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
database = os.getenv("POSTGRES_DATABASE")

async def main():
    async with asyncpg.connect(
        user=user,
        password=password,
        database=database,
        host="localhost",
    ) as conn:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (message TEXT NOT NULL)
        """)

asyncio.run(main())