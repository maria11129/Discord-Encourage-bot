import discord
import os
import requests
import random
from dotenv import load_dotenv
import json
from keep_alive import keep_alive

# Load environment variables from the .env file
load_dotenv()

# Load existing data from JSON file
def load_data():
    if os.path.exists("db.json"):
        with open("db.json", "r") as file:
            return json.load(file)
    return {"encouragements": [], "responding": True}  # Ensure "responding" is included by default

# Save data to JSON file
def save_data(data):
    with open("db.json", "w") as file:
        json.dump(data, file)

# Load data
data = load_data()

def update_encouragements(encouraging_msg):
    data["encouragements"].append(encouraging_msg)
    save_data(data)

def delete_encouragement(index):
    if len(data["encouragements"]) > index:
        del data["encouragements"][index]
        save_data(data)

# Define the necessary intents
intents = discord.Intents.default()
intents.messages = True  # Enable the intent to receive message events
intents.message_content = True  # Enable message content (required for reading message content)

client = discord.Client(intents=intents)

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing", "3yit", "krht", "kraht", "lonely", "crying"]

starter_encouragements = [
    "Cheer up!",
    "Hang in there!",
    "You got this!",
    "You're strong!",
    "You're doing great!"
]

# Ensure "responding" exists in data
if "responding" not in data:
    data["responding"] = True
    save_data(data)

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
    
    msg = message.content  # This variable is for convenience

    if message.content.startswith('$hello'):
        print("Hello command triggered!")  # Debugging
        await message.channel.send('Hello awesome person!')

    if message.content.startswith('$inspire'):
        quote = get_inspirational_quote()  # Define 'quote' by calling the function
        print("Inspire command triggered!")  # Debugging
        await message.channel.send(quote)  # Send the quote



    if data["responding"]:  # Use the "responding" value from the JSON file
        options = starter_encouragements
        if "encouragements" in data:
            options += data["encouragements"]

        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))

    if msg.startswith("$new"):
        encouraging_message = msg.split("$new", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added.")

    if msg.startswith("$del"):
        if "encouragements" in data:
            index = int(msg.split("$del", 1)[1])
            delete_encouragement(index)
            encouragements = data["encouragements"]  # Get the updated list
            await message.channel.send(encouragements)

    if msg.startswith("$list"):
        encouragements = []
        if "encouragements" in data:
            encouragements = data["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("$responding"):
        value = msg.split("$responding", 1)[1].strip().lower()

        if value == "true":
            data["responding"] = True
            await message.channel.send("Responding is on.")
        elif value == "false":
            data["responding"] = False
            await message.channel.send("Responding is off.")
        else:
            await message.channel.send("Invalid value for responding. Use 'true' or 'false'.")
        
        save_data(data)  # Ensure the "responding" status is saved
keep_alive()
client.run(os.getenv('TOKEN'))
