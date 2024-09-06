Encouragement Bot for Discord
This Discord bot is designed to spread positivity and inspiration through text messages. It responds to specific commands and can track and respond to sad messages within the server.

Features:

$hello: Responds with a welcoming message.
$inspiring: Sends an inspiring quote.
$new [message]: Adds a new encouraging message to the database.
$list: Lists all the encouraging messages currently in the database.
$del [index]: Deletes an encouraging message from the database based on its index.
$responding false: Stops the bot from responding to sad messages.
$responding true: Activates the bot to respond to sad messages.

Usage:
Installation: Clone the repository and install necessary dependencies using npm install.

Setup: Create a .env file with your Discord bot token:

makefile
Copy code
DISCORD_TOKEN=your_discord_bot_token_here
Running the Bot: Start the bot using node bot.js.

Commands:

Use $hello to greet new users.
Use $inspiring for an inspiring quote.
Use $new [message] to add new encouraging messages.
Use $list to display all encouraging messages.
Use $del [index] to delete a message by its index.
Use $responding false or $responding true to control the bot's response to sad messages.

Contributing:
Contributions are welcome! If you have ideas for improvements or new features, feel free to fork the repository and submit a pull request.
