import discord
from discord.ext import commands
import random, os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')

@bot.command()
async def sampah(ctx, item: str):
    organic = ["kulit_pisang", "buah_busuk", "sisa_sayur"]
    anorganic = ["plastik", "kaleng", "karet", "kaca", "kardus"]
    cat = ["organik", "anorganik"]

    if item in organic:
        await ctx.send("Sampah Tersebut Merupakan Sampah Organik")
    elif item in anorganic:
        await ctx.send("Sampah Tersebut Merupakan Sampah Anorganik")
    else:
        await ctx.send("Sampah Tersebut Tidak Diketahui") 
        

# bot.run("token")