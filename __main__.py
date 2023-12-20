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


class ChooseLanguageView(disnake.ui.View): # Create a class called MyView that subclasses discord.ui.View

    @disnake.ui.button(label="Русский", style=disnake.ButtonStyle.primary, emoji='🇷🇺') # Create a button with the label "😎 Click me!" with color Blurple
    async def button1_callback(self, button, inter):

        guild = inter.guild  # Assuming the command is used in a guild
        role = disnake.utils.get(guild.roles, name="Russian")  # Replace "TestRole" with the actual role name

        roles = []
        for i in range(0, len(inter.author.roles)):
            roles.append(inter.author.roles[i].name)

        if "Russian" in roles:
            await inter.author.remove_roles(role)
            await inter.response.send_message("Remove Russian role.") # Send a message when the button is clicked
        else:
            await inter.author.add_roles(role)
            await inter.response.send_message("Added Russian role.") # Send a message when the button is clicked


    @disnake.ui.button(label="English", style=disnake.ButtonStyle.green, emoji='🇺🇸') # Create a button with the label "😎 Click me!" with color Blurple
    async def button2_callback(self, button, inter):

        guild = inter.guild  # Assuming the command is used in a guild
        role = disnake.utils.get(guild.roles, name="English")  # Replace "TestRole" with the actual role name
        
        roles = []
        for i in range(0, len(inter.author.roles)):
            roles.append(inter.author.roles[i].name)

        if "English" in roles:
            await inter.author.remove_roles(role)
            await inter.response.send_message("Remove English role.") # Send a message when the button is clicked
        else:
            await inter.author.add_roles(role)
            await inter.response.send_message("Added English role.") # Send a message when the button is clicked




@bot.slash_command(name="choose-language-message", description="При исползовании этой команды будет отправлено сообщение для выбора основного языка сервера.")
async def choose_language_message(inter):
    await inter.response.send_message("Привет! Hello!", view=ChooseLanguageView())


# -- -- For testing below this line -- --


@bot.slash_command(name="ping", description="It is just a ping command.")
async def ping(inter):
    await inter.response.send_message("Pong!")


# @bot.slash_command(name="test")
# async def test(inter):
#     # Get the role object
#     guild = inter.guild  # Assuming the command is used in a guild
#     role = disnake.utils.get(guild.roles, name="🧷 Community Contributor")  # Replace "TestRole" with the actual role name
    
#     # Assign the role to the user
#     if role:
#         await inter.author.add_roles(role)
#         await inter.response.send_message(f"Role {role.name} assigned!")
#     else:
#         await inter.response.send_message("Role not found!")


# @bot.slash_command(name="buttonscommand")
# async def buttonscommand(inter):
#     button = [
#         disnake.ui.Button(label="button1", style=disnake.ButtonStyle.primary, custom_id="button1"),
#         disnake.ui.Button(label="button2", style=disnake.ButtonStyle.primary, custom_id="button2")
#     ]
    
#     await inter.response.send_message("some", components=button)


# @bot.event
# async def on_button_click(inter):
#     # Check the custom ID of the clicked button
#     if inter.component.custom_id == "button1":
#         await inter.response.edit_message(content="Button 1 clicked!", components=[])
#     elif inter.component.custom_id == "button2":
#         await inter.response.edit_message(content="Button 2 clicked!", components=[])


bot.run(TOKEN)