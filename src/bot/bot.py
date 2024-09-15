from telegram.ext import AIORateLimiter, Application, ApplicationBuilder

from src.bot.handlers import get, hello
from src.settings import settings


def create_bot() -> Application:
    bot = (
        ApplicationBuilder()
        .token(settings.BOT_TOKEN)
        .rate_limiter(AIORateLimiter())
        .build()
    )


    hello.hello_handlers(bot)
    get.send_get_message_handler(bot)
    return bot


async def start_bot() -> Application:
    """Запуск бота."""
    bot = create_bot()

    await bot.initialize()
    await bot.updater.start_polling()
    await bot.start()

    return bot


async def stop_bot(bot: Application):
    """Выключаем бота."""
    await bot.stop()
    await bot.shutdown()