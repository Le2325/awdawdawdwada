import discord
from discord.ext import commands
import os

# ====== Environment Variables ======
TOKEN = os.environ.get("TOKEN")
GUILD_ID = int(os.environ.get("GUILD_ID"))
VOICE_CHANNEL_ID = int(os.environ.get("VOICE_CHANNEL_ID"))

# ====== Intents ======
intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

    guild = bot.get_guild(GUILD_ID)
    if guild is None:
        print("❌ GUILD_ID غلط")
        return

    channel = guild.get_channel(VOICE_CHANNEL_ID)
    if channel is None:
        print("❌ VOICE_CHANNEL_ID غلط")
        return

    try:
        await channel.connect(self_mute=True, self_deaf=True)
        print("🎧 دخل الروم وهو ميوت ودفن")
    except Exception as e:
        print("❌ خطأ أثناء الدخول:", e)

bot.run(TOKEN)