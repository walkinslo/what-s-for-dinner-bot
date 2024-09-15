from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from src.bot.constants import commands


async def start_command(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:

    await context.bot.send_message(
        chat_id=update.effective_user.id,
        text="/get {day} to get the corresponding day's agenda."
    )


def hello_handlers(app: Application):
    app.add_handler(CommandHandler(commands.START, start_command))