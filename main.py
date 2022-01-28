import os
import discord
from keep_alive import keep_alive
from discord.ext import commands
import random


token = os.environ['token']
author_id = os.environ['author_id']

dancers = ['https://media.giphy.com/media/tsX3YMWYzDPjAARfeg/giphy.gif', 'https://media.giphy.com/media/14qb1Uhf40ndw4/giphy.gif', 'https://media.giphy.com/media/l2QZSjo0lwEMC0GVG/giphy.gif', 'https://media.giphy.com/media/5xaOcLGvzHxDKjufnLW/giphy.gif']

insults = [' smells like rotten fish.', ' is kind of like Jim Carrey\'s grinch; but uglier and more of a dick.', ', fuck you.', ' \"little ho, little bitch, suck my 5.3\" dick\"', ', you know what i did last night? Ya that\'s right, I fucked your mom.', ' Go back to where you came from. You should go climb right back into your dad\'s hairy ballsack you ugly mofo.', ' Calling all men/women: If you think a blob fish is hot, then you\'ll love this person. \nhttps://media.giphy.com/media/QGBWk7DnckEN2/giphy.gif ']

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
    await ctx.send(arg)

@test.error
async def test_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Error: Something went wrong.')

#Random dance command.
@bot.command(name='dance', help='Sends random dance gif.')
async def dance(ctx):
    await ctx.send(random.sample(dancers, 1)[0])

@dance.error
async def dance_error(ctx, error):
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
@bot.command(name='insult', help='Insult another member.')
async def insult(ctx, *, member:discord.Member):
  await ctx.send(f"<@{member.id}>{random.sample(insults, 1)[0]}")

@insult.error
async def insult_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Error: There is no member by that name.')

extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

#keep_alive()  # Starts a webserver to be pinged.


bot.run(token)  # Starts the bot