import discord
import os
import requests
import json



client = discord.Client()

def get_fact():
  response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
  data = json.loads(response.text)
  x = json.dumps(data)
  y = x.split('"')
  fact = y[7]
  return(fact)

@client.event
async def on_ready():
    print('We have loged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
      return
  
  if message.content.startswith('!hello'):
      await message.channel.send('Hello beautiful')
  
  if message.content.startswith('!kys'):
    await message.channel.send('No, fuck off')
  
  #random fact line
  if message.content.startswith('!fact'):
    fact = get_fact()
    await message.channel.send(fact)


client.run(os.getenv('token'))
