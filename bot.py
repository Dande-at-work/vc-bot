import discord
from discord.ext import commands, tasks
import os

TOKEN = os.getenv("TOKEN")
VC_ID = 1505265983454056610

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
        print("Connected to VC and yapping")
    except Exception as e:
        print(e)

bot.run(TOKEN)
