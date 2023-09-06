import telebot
import tags

broadcaster = telebot.TeleBot(BOT_TOKEN)

chat_ids = tags.chat_ids
tags = tags.tags

# Dictionary to store pending messages with their respective tags
pending_messages = []

@broadcaster.message_handler(commands=['new_message'])
def handle_message(message):
    # Extract the command from the message
    command = '/new_message'
    
    # Strip the command from the message text
    message_text = message.text[len(command):].strip() if message.text.startswith(command) else message.text
    
    # Store the message for this user and ask for tags
    chat_id = message.chat.id
    pending_messages.append(message_text)
    broadcaster.send_message(chat_id, "I logged: " + message_text)
    broadcaster.send_message(chat_id, "Please provide the tag for your message:")

@broadcaster.message_handler(commands=['tags'])
def handle_tags(message):
    command = '/tags'
    # Strip the command from the message text
    message_text = message.text[len(command):].strip() if message.text.startswith(command) else message.text

    chat_id = message.chat.id
    broadcaster.send_message(chat_id, "I logged: " + message_text)

    for tag in tags:
        if message_text == tag:
            for chat in chat_ids:
                if chat in tags[tag]:
                    chat_id = int(chat_ids[chat])
                    broadcaster.send_message(chat_id, pending_messages[-1])
                    broadcaster.send_message(message.chat.id, "Message sent to: " + message.text)
    pending_messages.pop()

broadcaster.infinity_polling()