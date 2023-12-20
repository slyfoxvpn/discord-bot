import os
from dotenv import load_dotenv
import disnake
from disnake.ext import commands
from disnake import ui


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


intents = disnake.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix=commands.when_mentioned_or("/"), intents=intents)


@bot.event
async def on_ready():
    game = disnake.Activity(type=disnake.ActivityType.watching, name="за вашей безопасностью в сети")
    await bot.change_presence(activity=game, status=disnake.Status.online)
    print("Bot is ready!")


@bot.slash_command(name="ping", description="It is just a ping.")
async def ping(inter):
    await inter.response.send_message("Pong!")


@bot.slash_command(name="test")
async def test(inter):
    # Get the role object
    guild = inter.guild  # Assuming the command is used in a guild
    role = disnake.utils.get(guild.roles, name="🧷 Community Contributor")  # Replace "TestRole" with the actual role name
    
    # Assign the role to the user
    if role:
        await inter.author.add_roles(role)
        await inter.response.send_message(f"Role {role.name} assigned!")
    else:
        await inter.response.send_message("Role not found!")


@bot.slash_command(name="buttonscommand")
async def buttonscommand(inter):
    button = [
        disnake.ui.Button(label="button1", style=disnake.ButtonStyle.primary, custom_id="button1"),
        disnake.ui.Button(label="button2", style=disnake.ButtonStyle.primary, custom_id="button2")
    ]
    
    await inter.response.send_message("some", components=button)


@bot.event
async def on_button_click(inter):
    # Check the custom ID of the clicked button
    if inter.component.custom_id == "button1":
        await inter.response.edit_message(content="Button 1 clicked!", components=[])
    elif inter.component.custom_id == "button2":
        await inter.response.edit_message(content="Button 2 clicked!", components=[])


bot.run(TOKEN)