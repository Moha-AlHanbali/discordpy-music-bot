"""This module handles operates the muisc bot"""

import discord
import os
from dotenv import load_dotenv

from commands.enqueue import enqueue
from commands.summon import summon
from commands.leave import leave
from commands.clear import clear
from commands.play import play
from commands.queue import queue

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

                    Arguments: 
                        message: Message instance

                    Return: None 


            command_handler:

                Directs a command to its' corresponding function.

                    Arguments: 
                        message: Message instance
                        command: str
                        content: str

                    Return: None 
                   
    """

    def __init__(self):
        super().__init__()
        self.queue = []
        self.voice_channel = None


    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        if self.voice_clients:
            self.voice_channel = self.voice_clients[0]


    async def on_message(self, message):

        if message.author == self.user or  not message.content.startswith(prefix):
            return

        if not message.author.voice:
            return await message.channel.send('You need to be in a voice channel to use bot commands!')


        command = message.content.lower().split(" ")[0][1:]
        content = " ".join(message.content.split(" ")[1:])      # NOTE: HASHED URLS MAY CONTAIN UPPER CASE LETTERS

        if not self.voice_clients and not command == 'leave':
            await summon(message.author)
            self.voice_channel = self.voice_clients[0]

        await self.command_handler(message, command, content)



    async def command_handler(self, message, command, content=''):

        if command == 'add':
            self.queue = await enqueue(self.queue, content, message)

        if command == 'play':
            self.queue = await enqueue(self.queue, content, message)
            if not self.voice_channel.is_playing():
                self.queue = await play(self, self.queue, self.voice_channel, message)

        if command == 'join':
            if not self.voice_clients:
                return await summon(message.author)
            await message.channel.send('Bot is already joined a vocie channel!')

        if command == 'leave':
            if self.voice_clients:
                self.queue = clear(self.queue)
                self.voice_channel = None
                return await leave(self)
            await message.channel.send('Bot is not in a vocie channel!')

        if command == 'clear':
            self.queue = await clear(self.queue, message)

        if command == 'queue':
            await queue(self.queue, message)

music_bot = MusicBot()
music_bot.run(os.getenv('API_KEY'))