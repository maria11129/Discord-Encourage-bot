import discord
import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define the necessary intents
intents = discord.Intents.default()
intents.messages = True  # Enable the intent to receive message events
intents.message_content = True  # Enable message content (required for reading message content)

client = discord.Client(intents=intents)

# Function to get an inspirational quote
def get_inspirational_quote():
    response = requests.get("https://zenquotes.io/api/random")  # Example API for quotes
    json_data = response.json()
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

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
        print("Hello command triggered!")  # Debugging

        await message.channel.send('Hello awesome person!')

    if message.content.startswith('$inspire'):
        quote = get_inspirational_quote()  # Define 'quote' by calling the function
        print("Inspire command triggered!")  # Debugging

        await message.channel.send(quote)  # Now we can send it
    if message.content.startswith('$abdeRRaouf'):
        print("abdeRRaouf command triggered!")  # Debugging

        await message.channel.send('the sigma diamond woho!')

client.run(os.getenv('TOKEN'))
