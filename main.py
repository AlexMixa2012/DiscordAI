import discord
from discord.ext import commands
from model import AI

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for i in ctx.message.attachments:
            file_name = i.filename
            await i.save(f"./images/{file_name}")
            await ctx.send(AI(f"./images/{file_name}"))
    else:
        await ctx.send("где картинка")

bot.run("TOKEN")
