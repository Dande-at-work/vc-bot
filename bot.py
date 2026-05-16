import discord
from discord.ext import commands, tasks
import os

TOKEN = os.getenv("MTUwNTA3NDY2MjE2MDIwMzg5OA.GchuoJ.EUsOj5CLMhNr2bridecuux8DY7cf7qFKg3V79I")
VC_ID = 1505093424028581939

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    keep_alive.start()

@tasks.loop(seconds=20)
async def keep_alive():
    print("Checking VC...")

    channel = bot.get_channel(VC_ID)

    if channel is None:
        print("Channel not found")
        return

    print(f"Found channel: {channel.name}")

    for vc in bot.voice_clients:
        if vc.channel.id == VC_ID:
            print("Already connected")
            return

    try:
        await channel.connect(reconnect=True)
        print("Connected to VC")
    except Exception as e:
        print(e)

bot.run(TOKEN)
