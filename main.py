if __name__ == '__main__':
    # Import the api key from .env where .env is at directory root and API_KEY is the key's variable
    from dotenv import load_dotenv
    import os
    load_dotenv()  # Load the .env file
    api_key = str(os.getenv('API_KEY'))
    from bot_functions import respond # Controls responses in a more organized file
    import time
    import datetime # For saying the time with the hello message
    import special_commands


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
                import random
                global shutdown_code
                shutdown_code = ''
                for _ in range(5):
                    shutdown_code += str(random.randint(0,9))
                print(f'🔐 Your shutdown code is: {shutdown_code}')

    # Main loop of code
    @client.event # When something is sent in the server
    async def on_message(message):

        #if message.author == client.user: # If the message is from the bot
            #return  # Ignore and quit to prevent responding to itself
        
        if message.channel.name != channel_name: # If message not received in target channel
            return # Ignore and quit because message is in the wrong channel

        if str(message.author) not in ['frozen_cube_of_water']: # Control the users allowed to interact with bot
            if message.author != client.user: # Prevent self response
                await message.channel.send(f'🚫 ATTENTION: {message.author}. This channel needs to be kept clear for testing. Please do NOT transmit on this channel. Thank you. ')
                return # Ignore and quit because user is not in allow list

        command = message.content # Makes the received message more readable to humans


        # Check for special shutdown code
        if message.content == shutdown_code:
            await message.channel.send('Shutting down')
            await message.delete() # Removes the code for security
            import sys
            import os
            import playsound
            # playsound.playsound('misc/error.mp3', False)
            os.system(f'''
            osascript -e 'tell app "Visual Studio Code" to display dialog "'{message.author}' shut down bot with pin from Discord" buttons {"Dismiss"} default button "Dismiss"'
            ''')
            sys.exit("User forced shutdown")


        # Check if the command is for a logger
        if message.content[0:3] == '/re':
            # because we know that only the two below start with this, we can prepare
            from datetime import datetime
            timestamp = datetime.now().strftime("On %m/%d/%Y at %I:%M:%S %p")
            who_said = message.author

        if message.content[0:7] == '/report':
            report = message.content[8:]
            log_item = f'''🚫 {timestamp} - the user '{who_said}' reported the following issue\n    -> "{report}"'\n\n'''
            with open('reports.txt', 'a') as report_log:
                report_log.write(log_item)
                report_log.close()
                print("New report logged!")
                await message.channel.send(f"Thanks **@{who_said}** for your feedback!")

        elif message.content[0:8] == '/request':
            request = message.content[9:]
            log_item = f'''⭐️ {timestamp} - the user '{who_said}' requested the following feature\n     -> "{request}"'\n\n'''
            with open('requests.txt', 'a') as request_log:
                request_log.write(log_item)
                request_log.close()
                print("New request logged!")
                await message.channel.send(f"Thanks **@{who_said}** for your feedback!")

        else:
            pass
        

        # Check for special commands
        help_reply = special_commands.check_if_it_is_a_special_command(command)
        if help_reply is not None: # A special command
            await message.channel.send(help_reply)
        elif command[0] == '/': # If it's not a help, then treat like normal command
            reply = respond(command, message.author) # Pass the full message and user
            if reply is not None: # If None is returned, then there is nothing to send
                if reply == 'profanity':
                    await message.delete() # Delete the message
                    await message.channel.send(f'@{message.author}: do not use profanity')
                

                await message.channel.send(reply) # Send the reply made by bot_functions.py
            

    ## Run the bot!!!
    client.run(api_key)