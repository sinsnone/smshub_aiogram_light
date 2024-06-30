import logging
import asyncio

from aiohttp import web
from aiogram import executor
from telegram.bot import dp


# Configure the logger
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



# HTTP server handle function
async def handle(request):
    return web.Response(text="Bot is running")

# Initialize the aiohttp web server
async def init_web_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()

# Main function to start the bot and web server
async def main():
    # Start aiohttp web server
    await init_web_server()

    # Start the Telegram bot in the background
    await start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    # Run the main function using asyncio.run
    asyncio.run(main())

