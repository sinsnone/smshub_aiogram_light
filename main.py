import logging
import sys

from aiohttp import web
from aiogram import executor
from telegram.bot import dp

async def handle(request):
    return web.Response(text="Bot is running")

async def init_web_server():
    try:
        server = web.Application()
        server.router.add_get('/', handle)
        runner = web.AppRunner(server)
        await runner.setup()
        site = web.TCPSite(runner, '0.0.0.0', 8080)
        await site.start()
        logging.info("Web server started at http://0.0.0.0:8080")
    except Exception as e:
        logging.error(f"Error starting web server: {e}")
        raise

if __name__ == '__main__':
    try:
        # Set up logging configurations
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            stream=sys.stdout,
        )
        
        # Start the web server
        asyncio.run(init_web_server())
        
        # Start the bot
        executor.start_polling(dp, skip_updates=True)
    except KeyboardInterrupt:
        logging.warning("Bot stopped by user")
    except Exception as e:
        logging.exception(f"Unhandled error: {e}")
