import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'hello...purchase the subscription quickly and easily just do what bot says')
    print('Sent message to ' + member.name)

    
@client.event    
async def on_ready():
    await client.change_presence(game=Game(name='LOCO,HQ,BB//TRIVIA ROCK'))
    print('Ready, Freddy') 


client.run('NTQ4NzkyMjczNDYzNDEwNjk5.D1KpCg.G1cuZ1HJnae0cIVDwhqQa9ag-WE')
