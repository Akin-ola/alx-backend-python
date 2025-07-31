import aiosqlite
import asyncio

async def async_fetch_users():
    async with aiosqlite.connect("example.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            rows = [row async for row in cursor]
        return rows


async def async_fetch_older_users():
    async with aiosqlite.connect("example.db") as db:
        async with db.execute("SELECT *FROM users WHERE age > 40") as cursor:
            rows = [row async for row in cursor]
        return rows


async def main():
    users, older_users = await asyncio.gather(
        async_fetch_users(), 
        async_fetch_older_users()
    )
    print("All Users:", users)
    print("Older Users:", older_users)


asyncio.run(main())
