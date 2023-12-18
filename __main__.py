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
    print("Bot is ready.")


# Ping command
@bot.command(name="ping", description="This is a simple ping command.")
async def ping(ctx: interactions.CommandContext):
    await ctx.send("pong!")
    

button =[
    interactions.ActionRow(
        components=[
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                label="Click me!",
                custom_id="click_me",
            ),
            interactions.Button(
                style=interactions.ButtonStyle.DANGER,
                label="Do not click!",
                custom_id="do_not_click",
            ),
        ]
    )
]


@bot.command(name="languages", description="Send choose-language mesage.")
async def languages(ctx: interactions.CommandContext):
    await ctx.send("Привет! | Hello!", components=button)


@bot.component("click_me")
async def click_me(ctx: interactions.ComponentContext):
    await ctx.send("Clicked!")


@bot.component("do_not_click")
async def do_not_click(ctx: interactions.ComponentContext):
    await ctx.send("You clicked the wrong button!")



# Run the bot with your token
bot.start()