from discord.ext import commands
import threading
import time
import asyncio
import config
from steam.client import SteamClient
from steam.enums import EResult

client = SteamClient()

#Steambot
@client.on('connected')
def connected():
    print('Connected steambot\n')

@client.on('chat_message')
def handle_message(user, message_text):
    print('Got steam message: ' + str(message_text) + ' from: ' + user.name +' with steamid:' + str(user.steam_id))
    user.send_message('Command not found, if there anything wrong, contact with my creator - fmouse, steamid = 76561198071680434')

class MyBot(commands.Bot):
    async def on_ready(self):
        print(f'Ready {self.user}:{self.user.id}')
    async def on_message(self, message):
    	print('Got discord message: ' + message.content + ' from: ' + str(message.author.nick) +'')
    	client.get_user(76561198071680434).send_message('Got discord message: [' + message.content + '] from: [' + str(message.author.nick) +']')


def run_bot_in_thread():
    # Important to make an event loop for the new thread
    asyncio.set_event_loop(asyncio.new_event_loop())
    bot = MyBot(command_prefix='!')
    bot.run(config.TOKEN)

threading.Thread(target=run_bot_in_thread, daemon=True).start()

# Something with main thread here

#steambot
def start_steam_bot():
    print("Logining started")
    print("-"*20)
    result = client.login(config.USERNAME, config.PASSWORD)
    print('Steam bot login result = ' + str(result))

start_steam_bot()
client.run_forever()