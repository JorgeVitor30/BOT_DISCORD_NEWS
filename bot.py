import discord
from discord.ext import commands, tasks
from buscar_dados_noticia import *

intents = discord.Intents.default()
intents.message_content = True

lista = []

bot = commands.Bot("#", intents = intents)

Buscar = BuscarDados('https://www.cnnbrasil.com.br/ultimas-noticias/')

link = Buscar.buscar_new()
i = 0
# FAZER UMA LISTA COM OS ULTIMOS LINKS PRA FZR UM HISTORICO DOS ULTIMOS 5
# FAZER UMA VERIFICAÇÃO DA LISTA ATUAL DENTRO DO ARRAY
@bot.listen()
async def on_ready():
    Variavel.start() 
    
    
@tasks.loop(seconds=5)
async def Variavel():
    global i
    global link 

    use_link = Buscar.buscar_new()
    channel = bot.get_channel(1074361880145043617)
    
    if use_link != link:
        link = use_link
        await channel.send(link)
    elif i == 0:
        i += 1
        await channel.send(link)
    else:
        return
        


bot.run('MTA3NTIxNDQxODM0MzkwNzQyOA.G4qd3R.pvBNYpPZbS4KaoQVfflkgzsRnFK6iLEy6Yr7Jo')


