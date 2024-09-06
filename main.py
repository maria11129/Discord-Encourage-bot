import discord
import os
from dotenv import load_dotenv
#import requests
#import json

# Load environment variables from the .env file
load_dotenv()

# Define the necessary intents
intents = discord.Intents.default()
intents.messages = True  # Enable the intent to receive message events
intents.message_content = True  # Enable message content (required for reading message content)

client = discord.Client(intents=intents)

#def get_quote():
  #  response =requests.get("https://zenquotes.io/api/random")
   # json_data = json.loads(response.text)
   # quote

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Debugging line to check if the bot receives messages
    print(f"Message received: {message.content}")

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello awesome person!')

client.run(os.getenv('TOKEN'))
