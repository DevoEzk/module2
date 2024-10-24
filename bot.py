import discord
from discord.ext import commands
import random, os
import requests

intents = discord.Intents.default()
intents.message_content = True

#tidak efisien
#image = ["mem1.jpg","mem2.jpg","mem3.jpg"]
#print(random.choice(image))

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def animals(ctx):
    animals_name = random.choice(os.listdir("animals"))
    with open(f'animals/{animals_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

# bot.run("token")

#rb = read binary --> membaca
#f = int