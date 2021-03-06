import os
import discord
from keep_alive import keep_alive
from discord.ext import commands
import random
import requests
import giphypop
from giphypop import translate

token = os.environ['token']
author_id = os.environ['author_id']
api_key= os.environ['api_key']

#Command prefix.
bot = commands.Bot(
	command_prefix="~",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = author_id  # Change to your discord id!!!


@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

#Test
@bot.command(name='test', help='Tests the bot.')
async def test(ctx, *, arg):
  print(arg)
  await ctx.send(arg)

@test.error
async def test_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Error: Something went wrong.')

#Random dance command.
@bot.command(name='dance', help='Sends random dance gif.')
async def dance(ctx):
    dance_gif = translate('Dance', api_key=api_key)
    await ctx.send(dance_gif.bitly)

@dance.error
async def dance_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Error: Something went wrong.')

#Random spin command.
@bot.command(name='spin', help='Sends random spin gif.')
async def spin(ctx):
    spin_gif = translate('Spin', api_key=api_key)
    await ctx.send(spin_gif.bitly)

@dance.error
async def spin_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Error: Something went wrong.')

#Random hazbin gif command.
@bot.command(name='hazbin', help='Sends random hazbin hotel gif.')
async def hazbin(ctx):
    hazbin_gif = translate(phrase='hazbin hotel', api_key=api_key)
    await ctx.send(hazbin_gif.bitly)

@hazbin.error
async def hazbin_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Error: Something went wrong.')

#Yell command.
@bot.command(name='yell', help='Yell at someone.')
async def yell(ctx, *, member:discord.Member):
  await ctx.send(f"Dear <@{member.id}>, AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!")

@yell.error
async def yell_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Error: There is no member by that name.')


#Insult command
@bot.command(name='insult', help='Insult another member. Mention y/n. By defult it mentions the other user')
async def insult(ctx, member:discord.Member, *mention: bool):
  if mention in ('yes', 'y', 'true', 't', 'enable', 'on'):
    return True
  elif mention in ('no', 'n', 'false', 'f', 'disable', 'off'):
    return False

  if mention == True or mention == ():
    insulted = f"<@{member.id}>"
    response = requests.get("https://insult.mattbas.org/api/insult.txt")
    response_text = response.text.replace("Y", "y", 1)
    await ctx.send(f"{insulted} {response_text}.")
  else:
    insulted = f"{member.nick}"
    response = requests.get("https://insult.mattbas.org/api/insult.txt")
    response_text = response.text.replace("Y", "y", 1)
    await ctx.send(f"{insulted} {response_text}.")

@insult.error
async def insult_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Error: Syntax')

extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

#keep_alive()  # Starts a webserver to be pinged.


bot.run(token)  # Starts the bot