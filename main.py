import logging
import sys

from aiohttp import web
from aiogram import executor
from telegram.bot import dp
import DRGLIB


# Configure the logger
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger instance
logger = logging.getLogger(__name__)

# إعداد خادم HTTP بسيط
async def handle(request):
    return web.Response(text="Bot is running")

async def init_web_server():
    server = web.Application()
    server.router.add_get('/', handle)
    runner = web.AppRunner(server)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()

async def main():
    await init_web_server()
    executor.start_polling(dp, skip_updates=True)
    
if __name__ == '__main__':
    DRGLIB.client.loop.run_until_complete(main())
