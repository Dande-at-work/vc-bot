import discord
from discord.ext import tasks, commands
import os

TOKEN = os.getenv("TOKEN")

VC_ID = 1505265983454056610

LOFI_URL = "https://youtube.com/shorts/umoXVhKrVZQ?si=3vcZCgzboL1rvGj9"

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

FFMPEG_OPTIONS = {
    'options': '-vn'
}

YDL_OPTIONS = {
    'format': 'bestaudio',
    'noplaylist': True
}


@bot.event
async def on_ready():

    await bot.change_presence(
    activity=discord.CustomActivity(name="yapping")
    )

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

            vc = await channel.connect(reconnect=True)

            import yt_dlp

            with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(LOFI_URL, download=False)
                url2 = info['url']

            source = await discord.FFmpegOpusAudio.from_probe(
                url2,
                **FFMPEG_OPTIONS
            )

            vc.play(source)

            print("Playing lofi")

        except Exception as e:
            print(e)


bot.run(TOKEN)
