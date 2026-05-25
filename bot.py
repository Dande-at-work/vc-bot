import discord
from discord.ext import tasks, commands
import os

TOKEN = os.getenv("TOKEN")

VC_ID = 1505265983454056610

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    activity = discord.Game(name="yapping")
    await bot.change_presence(activity=activity)

    print(f"Logged in as {bot.user}")

    keep_alive.start()


@tasks.loop(seconds=30)
async def keep_alive():
    channel = bot.get_channel(VC_ID)

    if channel is None:
        print("Channel not found")
        return

    if len(bot.voice_clients) == 0:
        try:
            await channel.connect(reconnect=True)
            print("Connected to VC")
        except Exception as e:
            print(e)


bot.run(TOKEN)
