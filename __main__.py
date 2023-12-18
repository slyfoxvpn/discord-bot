import os
from dotenv import load_dotenv
import interactions


# Load .env
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')


# Init bot
bot = interactions.Client(token=BOT_TOKEN)


# Ping command
@bot.command(name="ping", description="This is a simple ping command.",)
async def ping(ctx: interactions.CommandContext):
    await ctx.send("pong!")


# Run the bot with your token
bot.start()