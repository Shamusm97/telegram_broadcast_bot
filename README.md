# Telegram Broadcaster Bot

## What is it?
This is a MVP for a telegram broadcaster bot.
Extremely basic fuctionality at the moment, with little to no features implemented.

## What does it do?
Right now the user 'loads' a message into the bot with '/new_message {the actual message content here}'.
The bot will save this message and ask for tags.
The user will prvide tags in the following format '/tags {tags goe here, space separated}'
The bot will check against a backend log of which tags are associated with which channels/groups and send the message to the respective place.

## Limits
At the moment there are no UX features implemented, as such it is hard to use.

## Example

### Sending a message to channels with the #tag1 tag
![Sending of #tag1 message](pics/#tag1_send.PNG?raw=true)

### Receiving a message from the broadcaster with the #tag1 tag
![Receiving of #tag1 message](pics/#tag1_receive.PNG?raw=true)

### Sending a message to channels with the #tag2 tag
![Sending of #tag2 message](pics/#tag2_send.PNG?raw=true)

### Receiving a message from the broadcaster with the #tag1 tag
![Receiving of #tag2 message](pics/#tag2_receive.PNG?raw=true)
