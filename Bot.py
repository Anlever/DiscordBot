import discord
import asyncio

import ArrayId

from discord.ext import commands
from threading import Thread

with open('DiscordToken.txt', 'r', encoding='utf-8') as f:
    DISCORD_BOT_TOKEN = f.read()

person_ids_dict = ArrayId.person()
channels_ids_dict = ArrayId.channel()
servers_ids_dict = ArrayId.server()

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='/', intents=intents, application_id=ArrayId.appid())


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.tree.sync()
    t1 = Thread(target=write_message)
    t1.start()

@bot.tree.command(name="амогус", description="Скидывает амогуса")
async def amogus_command(interaction: discord.Interaction):
    await interaction.response.send_message(file=discord.File('amogus.gif'))

@bot.event
async def on_message(message):
    if message.author.id == person_ids_dict['Лёха']:
        emoji = '🤡'
        await message.add_reaction(emoji)
        
    if message.author.id == person_ids_dict['Сырник']:
        emoji = '💤'
        await message.add_reaction(emoji)
        
    if message.author.id == person_ids_dict['Егор']:
        emoji = '🚼'
        await message.add_reaction(emoji)
        
    if message.author.id == person_ids_dict['Рома']:
        await message.channel.send("О привет Рома")
        
    if message.author.id == person_ids_dict['Саня']:
        emoji = '🐔'
        await message.add_reaction(emoji)
    

def write_message():
    while True:
        target_channel = bot.get_channel(int(channels_ids_dict['Общее']))
        
        print("Id чела для упоминания")
        user_id = str(input())
        print("Пиши сообщение")
        message = str(input())
        
        if (user_id == ""):
            asyncio.run_coroutine_threadsafe(target_channel.send(f"{message}"), bot.loop)
        else:
            asyncio.run_coroutine_threadsafe(target_channel.send(f"<@{user_id}> {message}"), bot.loop)

bot.run(DISCORD_BOT_TOKEN)
