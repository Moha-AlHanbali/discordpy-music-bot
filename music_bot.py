"""This module handles operates the muisc bot"""

import discord
import os
from discord import client
from dotenv import load_dotenv

# NOTE: USE ENV VARIABLES
load_dotenv()
prefix = '!'

class MusicBot(discord.Client):
    """
    MusicBot Class inherits Discord Client Class, which is the connection to discord. Each class instance is a bot that is able to play music on its' own.

        Methods:

            on_ready:
                Prints the bot name once its' online.
                    Arguments: None
                    Return: None

            on_message:
                Receives user messages and interprets if they were sent as a command or not.
                    Arguments: message
                    Return: None                    
    """

    async def on_ready(self):
        print(f'Logged on as {self.user}!')


    async def on_message(self, message):

        if message.author == self.user or  not message.content.startswith(prefix):
            return

        command = message.content[1:]

        await message.channel.send(command)


        print(f'Message from {message.author}: {message.content}')






# RUN THE MUSIC BOT INSTANCE
music_bot = MusicBot()
music_bot.run(os.getenv('API_KEY'))