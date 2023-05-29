import nextcord
import aiohttp
from nextcord.ext import commands
intents = nextcord.Intents.default()
intents.message_content = True
from nextcord import Interaction, SlashOption
from nextcord import ui , Button
import requests
import random
import asyncio


client = bot = commands.Bot(command_prefix = '.', intents=intents)
client.remove_command("help")
@bot.event
async def on_ready():
       await client.change_presence(status=nextcord.Status.do_not_disturb, activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="Cowboys"))

client.slash_command(description="sends a roast")
async def roast(interaction:Interaction):
 get = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
 day = get.json()
 embed=nextcord.Embed(title="roast :face_with_symbols_over_mouth:")
 embed = embed.add_field(name="",value=day['insult'])
 await interaction.response.send_message(embed=embed)

client.slash_command(description="shows help menu")
async def help(interaction:Interaction):
   embed=nextcord.Embed(title="Help command")
   embed.add_field(name="/cat", value="/catfact", inline=False)
   embed.add_field(name="/dog", value="/fox", inline=False)
   embed.add_field(name="/invite", value="/ping", inline=True)
   embed.add_field(name="/member_count", value="/help", inline=True)
   await interaction.response.send_message(embed=embed)


@client.slash_command(description="get a catfact")
async def catfact(interaction: Interaction):
  async with aiohttp.ClientSession() as session:
    async with session.get("https://catfact.ninja/fact") as response:
      fact = (await response.json())["fact"]
      length = (await response.json())["length"]
      embed = nextcord.Embed(title=f'Random Cat Fact Number: **{length}**', description=f'Cat Fact: {fact}', colour=0x400080)
      embed.set_footer(text="")
  await interaction.response.send_message(embed=embed)

@client.slash_command(description="get a cat picture")
async def cat(interaction: Interaction):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.thecatapi.com/v1/images/search') as response:
            catjson = await response.json()
            caturl = catjson[0]['url']
            embed = nextcord.Embed(title=f"Here's a random image of cat! :cat:", color=nextcord.Color.blue())
            embed.set_image(url=caturl)
            await interaction.response.send_message(embed=embed)

  # dog command
@client.slash_command(description="get a dog picture")
async def dog(interaction: Interaction, breed: str):
    async with aiohttp.ClientSession() as session:
        request = await session.get(f'https://dog.ceo/api/breed/{breed}/images/random')
        dogjson = await request.json()
    
    embed = nextcord.Embed(title=f"Here's a random image of a {breed.capitalize()}! :dog:", color=nextcord.Color.blue())
    embed.set_image(url=dogjson['message'])
    
    await interaction.response.send_message(embed=embed)

   # fox command
@client.slash_command(description="get a fox picture")
async def fox(interaction: Interaction):
      response = requests.get('https://randomfox.ca/floof/')
      data = response.json()
      embed = nextcord.Embed(
          title = 'Fox :fox:',
          description = '',
          colour = nextcord.Colour.orange()
          )
      embed.set_image(url=data['image'])            
      embed.set_footer(text="")
      await interaction.response.send_message(embed=embed)

#invite
@client.slash_command(description="Invite the bot")
async def invite(interaction: Interaction):
      embed=nextcord.Embed(title="Invite the bot to your server", url="https://discord.com/api/oauth2/authorize?client_id=1107315813448425535&permissions=8&scope=bot%20applications.commands", color=0xb4d704)
      embed.set_author(name="Invite the bot")
      await interaction.response.send_message(embed=embed)

@client.slash_command(description="ping")
async def ping(interaction: Interaction):
 embed=nextcord.Embed(title="Discord api :ping_pong:")
 embed.add_field(name="",value='ms: {0}'.format(round(client.latency),inline=False))
 await interaction.response.send_message(embed=embed)

@client.slash_command(description="gets the numder of Members")
async def member_count(interaction: Interaction):
 embed=nextcord.Embed(title=interaction.guild.name)
 embed.add_field(name="Members",value=interaction.guild.member_count)
 await interaction.response.send_message(embed=embed)
 
