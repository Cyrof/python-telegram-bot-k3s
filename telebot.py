import telegram
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import os 
import dotenv

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(f"Hello {user.mention_html()}!, Welcome to the k3s home server notification groupchat.")

async def chatId(update: Update, context: ContextTypes.DEFAULT_TYPE):
    id = update.message.chat_id
    await update.message.reply_html(f"This is the chat id \n {id}")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link = "https://github.com/Cyrof/python-telegram-bot-k3s/issues"
    # text = f"1) To get the chat id use /chatid\n\n\<b>To request for more features visit {link} and create and issue.</b>"
    text = (
        "1) To get the chat id use /chatid\n\n"
        "2) To initialise email ml use /einit\n"
        "For more information on email ml use /ehelp\n\n"
        f"<b>To request for more features visit {link} and create an issue.</b>"
    )
    await update.message.reply_html(text)

async def ehelp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    e_text = (
        "Email ml usage:\n"
        "1) Initialise your email for email ml model generation using the /einit [your-email]."
    )
    await update.message.reply_html(e_text)

async def getemail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = ' '.join(context.args)

    if not user_input:
        await update.message.reply_text("Please enter your email after the command")
        return
    
    await update.message.reply_text(user_input)

def get_token():
    dir_name = os.getcwd()
    env_path = os.path.join(dir_name, ".env")
    dotenv.load_dotenv(env_path)

    return {
        't': os.environ.get("TOKEN")
    }


def main():
    cred = get_token()
    t = cred['t']
    print(t)

    app = Application.builder().token(t).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('ehelp', ehelp))
    app.add_handler(CommandHandler('chatid', chatId))
    app.add_handler(CommandHandler('einit', getemail))

    try:
        app.run_polling()
    except KeyboardInterrupt:
        print("Bot stopped.")

if __name__ == "__main__":
    main()