"""
The main script to run the bot.
"""

import logging
import sys

from aiogram import executor

from telegram.bot import dp
from aiohttp import web


async def handle(request):
    return web.Response(text="Bot is running")

async def init_web_server():
    server = web.Application()
    server.router.add_get('/', handle)
    runner = web.AppRunner(server)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()
    


if __name__ == '__main__':
    await init_web_server()
    # Set up logging configurations
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        stream=sys.stdout,
    )
    
    # Start the bot
    executor.start_polling(dp, skip_updates=True)
