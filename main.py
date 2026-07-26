import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 6519187818

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! Send your confession here 🤍"
    )

async def confession(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    text = (
        "📩 New confession:\n\n"
        f"{update.message.text}\n\n"
        f"From user ID: {user.id}"
    )

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=text
    )

    await update.message.reply_text(
        "Your confession has been received 🤍"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, confession))

app.run_polling()
