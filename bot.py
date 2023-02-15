import discord
import os


intents = discord.Intents.default()
intents.message_content = True


class MeuBot(discord.Client):
    async def on_ready(self):
        pass
    
    async def on_message(self, message):
        if "#regras" in message.content:
            await message.channel.send("CLB COUTO LIXO SMT")
    
    


client = MeuBot(intents = intents)
client.run('MTA3NTIxNDQxODM0MzkwNzQyOA.G4qd3R.pvBNYpPZbS4KaoQVfflkgzsRnFK6iLEy6Yr7Jo')


