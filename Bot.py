import discord
import asyncio
from discord.ext.commands import Bot
from threading import Thread



with open('AmogusRapKruto.txt', 'r', encoding='utf-8') as f:
    Boken = f.read()

# открываем файл, обязательно указывая режим и кодировку
with open(r'IdArray.txt', mode='r', encoding='utf-8') as fl:
    # считываем содержимое файлам одним списком стром
    person_ids = fl.readlines()

person_ids_dict = {}  
channels_ids_dict = {}




for i in person_ids:
    k, v = i.split(':')
    v = v.strip()
    v = int(v) if v.isdigit() else v
    person_ids_dict[k] =  v
    
with open(r'ChannelId.txt', mode='r', encoding='utf-8') as fr:
    # считываем содержимое файлам одним списком стром
    channels_ids = fr.readlines()


for i in channels_ids:
    k, v = i.split(':')
    v = v.strip()
    v = int(v) if v.isdigit() else v
    channels_ids_dict[k] =  v


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
        
#    if message.author.id == person_ids_dict['Мой_id']:
#        await message.channel.send("Тест")
        
    if message.author.id == person_ids_dict['Саня']:
        emoji = '🐔'
        await message.add_reaction(emoji)

    


def write_message():
    while True:
        target_channel = client.get_channel(int(channels_ids_dict['Общее']))
        
        print("Id чела для упоминания")
        user_id = str(input())
        print("Пиши сообщение")
        message = str(input())
        
        
        
        if (user_id == ""):
            asyncio.run_coroutine_threadsafe(target_channel.send(f"{message}"), client.loop)
        else:
            asyncio.run_coroutine_threadsafe(target_channel.send(f"<@{user_id}> {message}"), client.loop)
            
        
        
        
    
    
    
    
    

client.run(Boken)