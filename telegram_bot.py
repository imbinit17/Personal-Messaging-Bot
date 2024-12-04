from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler ,filters ,MessageHandler

import os 
import database


TOKEN = os.getenv('TOKEN')
channel_id = os.getenv('CHANNEL_ID')
group_id = os.getenv('GROUP_ID')

current_message_id = -1

async def start(update: Update, context) -> None:
    global current_message_id

    init_msg = await context.bot.send_message(chat_id=group_id, text="Bot Internal Initialisation ! Please ignore")
    current_message_id = init_msg.message_id
    chat_id = update.effective_chat.id

    if(database.getUser(chat_id) == None):
        name = update.effective_chat.first_name
        username = update.effective_chat.username

        await context.bot.send_message(chat_id=channel_id, text=f"{name} \n{username} \n{chat_id} \nGroup_message_id = {current_message_id+1}")

        database.addUser(chat_id, current_message_id+1)
        current_message_id += 1
               
    await update.message.reply_text("Hi ! You can message here to talk to Binit")

async def pass_message(update: Update, context) -> None:
    chat_id = update.effective_chat.id
    message = update.message
    message_id = message.id

    # When I mean to chat with someone through my bot
    if chat_id == group_id and message.reply_to_message is not None:
        person_msg_thread_id = message.reply_to_message.id  # This is the thread_id in group...not in channel...in channel it is different
        await context.bot.copy_message(chat_id=database.getUserByThreadID(person_msg_thread_id), from_chat_id=chat_id, message_id=message_id)

    # When someone wants to chat with me through my bot
    elif chat_id != group_id:
        await context.bot.copy_message(chat_id=group_id, from_chat_id=chat_id, reply_to_message_id=database.getThreadIDbyUser(chat_id),message_id=message_id)

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL, pass_message))

    application.run_polling()

if __name__ == '__main__':
    main()