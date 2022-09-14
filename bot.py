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
         response = requests.get('https://dad-jokes.p.rapidapi.com/random/joke')
         joke = json.loads(response.text)
         return(joke['value'])
       the_joke = await get_joke(self)
       await message.channel.send(the_joke)
     await client.process_commands(message)


        
@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()



 
client.run(TOKEN)
