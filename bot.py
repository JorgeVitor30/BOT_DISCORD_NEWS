import discord
from discord.ext import commands, tasks
from buscar_dados_noticia import *

intents = discord.Intents.default()
intents.message_content = True

token = 'MTA3NTIxNDQxODM0MzkwNzQyOA.G4qd3R.pvBNYpPZbS4KaoQVfflkgzsRnFK6iLEy6Yr7Jo'

bot = commands.Bot("#", intents = intents)

Buscar = BuscarDados('https://www.cnnbrasil.com.br/ultimas-noticias/')

link = Buscar.buscar_new()
i = 0

@bot.listen()
async def on_ready():
    envio_noticias.start() 
    
    
@tasks.loop(seconds=5)
async def envio_noticias():
    global i
    global link 
    channel_id = 1074361880145043617

    use_link = Buscar.buscar_new()
    channel = bot.get_channel(channel_id)
    
    if use_link != link:
        link = use_link
        await channel.send("MAIS UMA NOTÍCIA 🤮")
        await channel.send(link)

    elif i == 0:    
        i += 1
        await channel.send("MAIS UMA NOTÍCIA 🤮")
        await channel.send(link)
    else:
        return
        


bot.run(token)