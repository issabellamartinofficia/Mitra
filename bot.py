import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config_loader import validate_key, load_user, is_admin
from task_runner import run_task
from log_handler import get_log
from vps_checker import get_status

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
users = {}

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text("🔑 Use: /start <access-key>")
        return
    key = args[0]
    result = validate_key(key)
    if result:
        users[update.effective_user.id] = result
        await update.message.reply_text(f"✅ Welcome {result['name']} ({result['role']})")
    else:
        await update.message.reply_text("❌ Invalid or expired key.")

async def imgb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = users.get(update.effective_user.id)
    if not user:
        await update.message.reply_text("Use /start <access-key> first.")
        return
    args = context.args
    if len(args) != 3:
        await update.message.reply_text("Usage: /imgb <ip> <port> <duration>")
        return
    ip, port, time = args
    msg = run_task(ip, port, time, user['name'])
    await update.message.reply_text(msg)

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = users.get(update.effective_user.id)
    if not user:
        await update.message.reply_text("Unauthorized.")
        return
    args = context.args
    if not args:
        await update.message.reply_text("Usage: /log <task-id>")
        return
    await update.message.reply_text(get_log(args[0], user['name']))

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_status())

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("imgb", imgb))
app.add_handler(CommandHandler("log", log))
app.add_handler(CommandHandler("status", status))
app.run_polling()
