import discord
import random
import requests
import json

TOKEN = '##your token id'

client = discord.Client(intents=discord.Intents.default())


@client.event 
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
     username = str(message.author).split('#')[0]
     user_message = str(message.content)
     channel = str(message.channel.name)
     print(f'{username}: {user_message}({channel})')
     if message.author == client.user:
        return
     # here two hashes denote that it is a place holder for something ucan put of your own
     if message.channel.name == '##your random server':
      if user_message.lower() == 'hi':
        await message.channel.send(f'Hello master {username}!')
        await message.channel.send(f'what can i do for you')
        return

      elif user_message.lower() == 'bye':
        await message.channel.send(f'See you soon master {username}')
        return
     if message.content.startswith('$joke'):
       async def get_joke(self):
         response = requests.get('https://api.chucknorris.io/jokes/random')
         joke = json.loads(response.text)
         return(joke['value'])
       the_joke = await get_joke(self)
       await message.channel.send(the_joke)
 
client.run(TOKEN)