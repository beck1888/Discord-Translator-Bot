if __name__ == '__main__':
    # Import the api key from .env where .env is at directory root and API_KEY is the key's variable
    from dotenv import load_dotenv
    import os
    load_dotenv()  # Load the .env file
    api_key = str(os.getenv('API_KEY'))
    from bot_functions import respond # Controls responses in a more organized file
    import time
    import datetime # For saying the time with the hello message


    time.sleep(2) # DELAY: Allows for user to switch into Discord window and see bot come online


    ## Import modules for discord bot
    import discord
    from discord.ext import commands

    # Set the bot's destination
    server_name = 'kjhscs2324' # Put the EXACT server name as a string here, tells the bot where to connect
    channel_name = 'becks-bot' # Prevents bot from connecting to every channel in the server
    
    # Prepare bot to connect
    intents = discord.Intents.all() # Says the bot can do everything Discord dev page bot permission list
    client = commands.Bot(command_prefix="!", intents=intents) # Initialize bot

    # Get time and format it
    now = datetime.datetime.now()
    time = now.strftime("%I:%M %p")

    # Make the connection
    @client.event
    async def on_ready():
        guild = discord.utils.get(client.guilds, name=server_name)
        
        if guild:
            print(f"DEBUG: Connected to server {guild.name}")
            channel = discord.utils.get(guild.channels, name=channel_name)  # Try finding channel directly
            if channel: # When channel is found anc connected to
                # await channel.send(f"I logged on at {time}")
                print(f"DEBUG: Logged on to  '{channel.name}' channel")


    # Main loop of code
    @client.event # When something is sent in the server
    async def on_message(message):

        #if message.author == client.user: # If the message is from the bot
            #return  # Ignore and quit to prevent responding to itself
        
        if message.channel.name != channel_name: # If message not received in target channel
            return # Ignore and quit because message is in the wrong channel

        if str(message.author) not in ['frozen_cube_of_water']: # Control the users allowed to interact with bot
            return # Ignore and quit because user is not in allow list

        command = message.content # Makes the received message more readable to humans

        if command[0] == '/': # Only run if it starts with a slash
            reply = respond(command, message.author) # Pass the full message and user
        
        await message.channel.send(reply)

    # Run the bot
    client.run(api_key)