import discord
import os
from discord.ext import commands, tasks
from buscar_dados_noticia import *
import datetime

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot("#", intents = intents)

Buscar = BuscarDados('https://www.cnnbrasil.com.br/ultimas-noticias/')

link = Buscar.buscar_new()

# FAZER UMA LISTA COM OS ULTIMOS LINKS PRA FZR UM HISTORICO DOS ULTIMOS 5
# FAZER UMA VERIFICAÇÃO DA LISTA ATUAL DENTRO DO ARRAY


# async def on_message(self, message):
#     if "#função" in message.content:
#         await message.channel.send("DAR NOTICIAS")
            
#     if "#abc" in message.content:
#         pass
            
 
@bot.listen()
async def on_ready():
    Variavel.start() 
    
    
@tasks.loop(seconds=5)
async def Variavel():
    channel = bot.get_channel(1074361880145043617)
    await channel.send(link)
        





bot.run('MTA3NTIxNDQxODM0MzkwNzQyOA.G4qd3R.pvBNYpPZbS4KaoQVfflkgzsRnFK6iLEy6Yr7Jo')


