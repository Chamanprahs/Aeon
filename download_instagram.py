import os
import instaloader
from telegram.ext import CommandHandler, Updater
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def download_instagram(update, context):
    if len(context.args) > 0:
        url = context.args[0]
        shortcode = url.split('/')[-2]  # Extract the shortcode from the URL
        L = instaloader.Instaloader()  # Create an Instaloader instance

        try:
            post = instaloader.Post.from_shortcode(L.context, shortcode)
            L.download_post(post, target=f"{post.owner_username}")
            update.message.reply_text(f"Downloaded {url}")
        except Exception as e:
            update.message.reply_text(f"Failed to download: {str(e)}")
    else:
        update.message.reply_text("Please provide an Instagram post URL.")

def main():
    bot_token = os.getenv("BOT_TOKEN")
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("il", download_instagram))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
