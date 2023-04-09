import discord
from discord import app_commands
import RCON

#Set up discord client and command settings
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

#A simple echo command to make sure the bot is running
@tree.command(name = "echo", description = "I repeat what you send", guild=discord.Object(id=689876684752814132)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
@app_commands.describe(repeatstring = "The phrase to repeat")
async def fuck(interaction, repeatstring:str):
    await interaction.response.send_message(repeatstring)

#This sends a minecraft command using RCON
@tree.command(name = "sendmccommand", description = "Sends an arbitrary minecraft server command", guild=discord.Object(id=689876684752814132))
@app_commands.describe(commandstring = "The command you want to send")
#Checks to make sure the user has permissions to use the command
@app_commands.checks.has_role("Officer")
async def sendMCcommand(interaction, commandstring:str):
    resp = RCON.sendCommand(commandstring)
    #trim the server response so it looks nice
    if resp == "[0m":
        resp = "No response"
    else:
        resp = resp[:-3]
    await interaction.response.send_message("Server response: " + resp)
        
#If the user doesn't have permissions this activates
@sendMCcommand.error
async def onMCCommandError(interaction: discord.Interaction, error: app_commands.AppCommandError):
    await interaction.response.send_message("Sorry, only officers can use this command", ephemeral=True)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=689876684752814132))
    print('We have logged in as {0.user}'.format(client))


token = open('token.env', 'r')
client.run(token.read())

