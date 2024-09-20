from telegram import Bot
import asyncio

async def test():
    bot = Bot("7036134694:AAG7RTtJ7Cztew7iWtLJZnm0k_UalJLgkYE")
    await bot.send_message(-4593454565, "12345")

if __name__ == "__main__":
    asyncio.run(test())