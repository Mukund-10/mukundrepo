import discord
from discord.ext import command

Token = "NTQ4NTMyMTQ4MjcwMDA2Mjcy.D1LmHw.vofXTbKXgYFBifEUhEMVYi-dChY"

client = commands.Bot(command_prefix ='e!')

@client.event
async def on_ready();
     print('Bot is ready')

 client.run(TOKEN)
