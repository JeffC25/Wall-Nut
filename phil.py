import discord
import os
import asyncio
import youtube_dl
import env

token = env.token()

client = discord.Client()

voiceClients = {}

ytOptions = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(ytOptions)

ffmpegOptions = {'options': "-vn"}

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("??play"):
        try:                                        
            url = message.content.split()[1]                                                                    # option video URL

            voiceClient = await message.author.voice.channel.connect()                                          # handle voice connection 
            voiceClients[voiceClient.guild.id] = voiceClient                                                    # store in dictionary

            loop = asyncio.get_event_loop()                                                                     # async event loop
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download = False))           # data to video audio
            song = data['url']                                                                                  # pass data
            player = discord.FFmpegPCMAudio(song, **ffmpegOptions)                                              # set up player

            voiceClient.play(player)

        except Exception as err:
            print(err)

client.run(token)
