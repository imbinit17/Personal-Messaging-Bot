# Personal-Messaging-Bot

This bot enables you to chat with other telegram users without needing to reveal your personal contact details such as phone number or username with which your personal telegram acccount operates .

<h1>Telegram Initialisation</h1>

1. Create a telegram channel and a telegram group .
2. Add the group as "Discussion Group" in channel settings .
3. Create a bot using @BotFather and add it to both the channel and group .

<h1>Set Up The Bot ?</h1>

1. Clone the repo

   <pre><code>git init
   git clone git@github.com:imbinit17/Personal-Messaging-Bot.git
   </code></pre>
2. Install python-telegram-bot
   `<code>pip install python-telegram-bot</code>`
3. Set your telegram bot api key to "TOKEN" in environment variables .
4. Set the chat_id of the channel and group respectively as : CHANNEL_ID & GROUP_ID in environment variables .

   To get the chat_id , you can :-
   i.  Open Telegram Web > Open the Channel/Group and from the URL copy the the numeric (with or without a '-') next to the "#"
   ii. Use external bots
5. Run the bot ! (file : telegram_bot.py)

You are ready to use the bot . Head to telegram and anonymously chat with your peers (authorised users) . Also check the other commands in console .

<h2>Note:</h2>

Now ,leave the group you created as it is and try not to touch that if you do not want to break the bot down . Use the channel and you can reply to specific people by commenting under the broadcast in the channel that contains their name and username .
