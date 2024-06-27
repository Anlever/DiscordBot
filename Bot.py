import discord
import asyncio
from discord.ext.commands import Bot
from threading import Thread



with open('Bot token.txt', 'r', encoding='utf-8') as f:
    DISCORD_BOT_TOKEN = f.read()


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    t1 = Thread(target=write_message)
    t1.start()
    

@client.event
async def on_message(message):
    if message.author.id == 249133834866655232:
        emoji = '🤡'
        await message.add_reaction(emoji)
    if message.author.id == 272345981142695936:
        emoji = '💤'
        await message.add_reaction(emoji)
    if message.author.id == 151662277001609216:
        emoji = '🚼'
        await message.add_reaction(emoji)
    if message.author.id == 205998644262862849:
        await message.channel.send("О привет Рома")
    if message.author.id == 241517599165382656:
        await message.channel.send("Тест")


def write_message():
    while True:
        target_channel = client.get_channel(int(1067805711049949275))
        
        print("Id чела для упоминания")
        user_id = str(input())
        print("Пиши сообщение")
        message = str(input())
        
        
        
        if (user_id == ""):
            asyncio.run_coroutine_threadsafe(target_channel.send(f"{message}"), client.loop)
        else:
            asyncio.run_coroutine_threadsafe(target_channel.send(f"<@{user_id}> {message}"), client.loop)
            
        
        
        
    
    
    
    
    

client.run(DISCORD_BOT_TOKEN)