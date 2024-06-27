import discord
import asyncio
from discord.ext.commands import Bot
from threading import Thread

with open('Bot token.txt', 'r', encoding='utf-8') as f:
    Boken = f.read()

# открываем файл, обязательно указывая режим и кодировку
with open(r'IdArray.txt', mode='r', encoding='utf-8') as fl:
    # считываем содержимое файлам одним списком стром
    onstring = fl.readlines()

# определяем выводной словарь. Ключевое слово dict занято классом словаря,
# поэтому его использовать в качестве идентификатора переменной не рекомендуется.
# Так же не рекомендуется напрямую инициализировать его экземпляры. Для этого
# есть соответствующий синтаксический литерал
res = {}

# проходим в цикле по списку строк
for i in onstring:
    # присваиваем переменным k и v левую и правую часть подстроки,
    # разделяя по символу ':'
    k, v = i.split(':')
    # убираем лишние концевые пробелы
    v = v.strip()
    # определяем, является ли значение переменной v числом, и если да, то 
    # преобразуем к целому числу, иначе оставляем строкой
    v = int(v) if v.isdigit() else v
    # добавляем в словарь соответствующие пары ключ:значение
    res[k] =  v


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
    if message.author.id == res['Лёха']:
        emoji = '🤡'
        await message.add_reaction(emoji)
        
    if message.author.id == res['Сырник']:
        emoji = '💤'
        await message.add_reaction(emoji)
        
    if message.author.id == res['Егор']:
        emoji = '🚼'
        await message.add_reaction(emoji)
        
    if message.author.id == res['Рома']:
        await message.channel.send("О привет Рома")
        
#    if message.author.id == res['Мой_id']:
#        await message.channel.send("Тест")
        
    if message.author.id == res['Саня']:
        emoji = '🐔'
        await message.add_reaction(emoji)

    


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
            
        
        
        
    
    
    
    
    

client.run(Boken)