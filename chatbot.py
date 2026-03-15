'''
This program requires the following modules:
- python-telegram-bot==22.5
- urllib3==2.6.2
'''
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import configparser
import logging
from ChatGPT_HKBU import ChatGPT  # <--- 新增
gpt = None                        # <--- 新增：定义全局变量
def main():
    # Configure logging so you can see initialization and error messages
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    # Load the configuration data from file
    logging.info('INIT: Loading configuration...')
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')
    global gpt                 # <--- 新增
    gpt = ChatGPT(config)      # <--- 新增
    # Create an Application for your bot
    logging.info('INIT: Connecting the Telegram bot...')
    # Note: application builder reads the token from your config file
    app = ApplicationBuilder().token(config['TELEGRAM']['ACCESS_TOKEN']).build()

    # Register a message handler
    logging.info('INIT: Registering the message handler...')
    # This handler listens for text messages that are NOT commands
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, callback))

    # Start the bot
    logging.info('INIT: Initialization done!')
    app.run_polling()

async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await update.message.reply_text(response)
    logging.info("UPDATE: " + str(update))
    
    # 1. 先发一个 "Thinking..." 告诉用户收到消息了
    loading_message = await update.message.reply_text('Thinking...')

    # 2. 把用户的消息发给 ChatGPT，并等待回复
    # 注意：这里我们用 global gpt 变量
    global gpt
    response = gpt.submit(update.message.text)

    # 3. 把 "Thinking..." 修改成真正的回复内容
    await loading_message.edit_text(response)

if __name__ == '__main__':
    main()