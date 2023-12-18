import os
from dotenv import load_dotenv
import discord
import interactions


# Load .env
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')


# Init bot
bot = interactions.Client(token=BOT_TOKEN)

@bot.event
async def on_ready():
    await bot.change_presence(interactions.ClientPresence(activities=[interactions.PresenceActivity(name=f"за вашей безопасностью в сети", type=interactions.PresenceActivityType.WATCHING)]))

# Ping command
@bot.command(name="ping", description="This is a simple ping command.",)
async def ping(ctx: interactions.CommandContext):
    await ctx.send("pong!")


# Run the bot with your token
bot.start()