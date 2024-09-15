import sqlite3

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from src.bot.constants import commands


async def send_get_message(
        update: Update, 
        context: ContextTypes.DEFAULT_TYPE
) -> None:

    connection = sqlite3.connect('../../agenda.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_master")
    test_string = "asdasd"

    await update.effective_chat.send_message(
        test_string
    )


def send_get_message_handler(app: Application):
    app.add_handler(CommandHandler(commands.GET, send_get_message))