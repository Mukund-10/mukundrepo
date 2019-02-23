import discord
from discord.ext import command

Token = "NTQ4ODg3OTUzODU5MDE4Nzgy.D1L3kg.pTuhu2ppXdMfkusmJxLXJEZYRso"

client = commands.Bot(command_prefix ='e!')

@client.event
async def on_ready();
     await client.change_presence(game=discord.Game(name='beta test'))
     print('Bot is ready')

 client.run(TOKEN)
