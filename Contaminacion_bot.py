import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot para informar sobre la contaminacion{bot.user}!')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    lista_de_imagenes = os.listdir('images')
    image_aleatoria = random.choice(lista_de_imagenes)
    with open(f'images/{image_aleatoria}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def con(ctx):
    lista_de_imagenes = os.listdir('contaminacion')
    image_aleatoria = random.choice(lista_de_imagenes)
    with open(f'contaminacion/{image_aleatoria}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("TOKEN DE TU BOT")
