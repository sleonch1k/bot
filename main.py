# import discord
# import json
# import requests
# from discord.ext import commands
# import random
import json
import requests

import discord
from discord.ext import commands
# from discord.ext.commands import CommandNotFound
# from config import settings
from urllib import parse, request
import re


class DiscoAPI:
    json_data = None
    query = None

    def youtube(self, finds):
        query = parse.urlencode({'search_query': finds})
        html = request.urlopen('http://www.youtube.com/results?' + query)
        results = re.findall('href=\"/watch\\?v=(.{11})', html.read().decode())
        return results


api = DiscoAPI
bot = commands.Bot(command_prefix='#')
TOKEN = 'OTYxNjQ0MjkzMTI1MjAxOTMw.Yk7_CQ.uCklanpYDx51BtZdbWog9Co1D-Q'


@bot.command()  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx):  # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author  # Объявляем переменную author и записываем туда информацию об авторе.

    await ctx.send(f'Hello, {author.mention}!')


@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')  # Get-запрос
    json_data = json.loads(response.text)  # Извлекаем JSON

    embed = discord.Embed(color=0xff9900, title='Random Fox')  # Создание Embed'a
    embed.set_image(url=json_data['link'])  # Устанавливаем картинку Embed'a
    await ctx.send(embed=embed)  # Отправляем Embed


@bot.command()
async def dog(ctx):
    response = requests.get('https://some-random-api.ml/img/dog')
    json_data = json.loads(response.text)  # Извлекаем JSON

    embed = discord.Embed(color=0xff9900, title='Random Dog')  #
    embed.set_image(url=json_data['link'])  # Устанавливаем карти
    await ctx.send(embed=embed)  # Отправляем Embed


@bot.command()
async def tracker(ctx):
    author = ctx.message.author
    await ctx.send(f'https://fortnitetracker.com/, {author.mention}!')


@bot.command()
async def anime(ctx):
    response = requests.get('https://some-random-api.ml/animu/wink')
    json_data = json.loads(response.text)  # Извлекаем JSON
    embed = discord.Embed(color=0xff9900, title='UwU')  #
    embed.set_image(url=json_data['link'])  # Устанавливаем карти
    await ctx.send(embed=embed)  # Отправляем Embed


@bot.command()
async def joke(ctx):
    response = requests.get('https://some-random-api.ml/joke')
    json_data = json.loads(response.text)  # Извлекаем JSON
    await ctx.send(json_data["joke"])  # Отправляем Embed


@bot.command()
async def translate(ctx):
    author = ctx.message.author
    await ctx.send(f'https://translate.yandex.ru/, {author.mention}!')


@bot.command()
async def vote(ctx, *, message):
    try:
        await ctx.message.delete()
        msgage = await ctx.send(message)
        await msgage.add_reaction('👍')
        await msgage.add_reaction('👎')
    except Exception as ex:
        print(ex)


@bot.command()
async def youtube(ctx, *, finds):

    try:

        results = api.youtube(finds)
        await ctx.send('https://www.youtube.com/watch?v=' + results[0])
    except Exception as ex:
        print(ex)


@bot.command()
async def help_me(ctx):
    author = ctx.message.author
    await ctx.send(f'#hello, #fox, #dog, #tracker, #anime, #joke, #translate, #, {author.mention}!')


bot.run(TOKEN)
