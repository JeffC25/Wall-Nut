import discord
import env

token = env.token()

client = discord.Client()

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('??hi'):
        await message.channel.send('Hello!')

client.run(token)
