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
from commands.pause import pause
from commands.resume import resume
from commands.stop import stop
from commands.skip import skip
from commands.replay import replay
from commands.repeat import repeat
from commands.volume import volume

load_dotenv()
prefix = '!'


class MusicBot(discord.Client):
    """
    MusicBot Class inherits Discord Client Class, which is the connection to discord. Each class instance is a bot that is able to play music on its' own.

        Methods:

            on_ready:

                Prints the bot name once its' online and sets its' status.
                
                    Arguments: None

                    Return: None


            on_disconnect

                    Cleans up if bot gets disconnected
                    
                    Arguments:
                        message: Message instance

                    Return:
                        Sends a status message


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
        self.repeat = False

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await self.change_presence(status=discord.Status.idle, activity=discord.Game('!help'))
        

    async def on_disconnect(self, message):
            self.queue = []
            self.repeat = False
            if self.voice_channel:
                self.voice_channel.source = discord.PCMVolumeTransformer(self.voice_channel.source)
                self.voice_channel.source.volume = 100/ self.voice_channel.source.volume**2            
                await leave(self)
            self.voice_channel = None
            return await message.channel.send('Bot got disconnected from Discord!')


    async def on_message(self, message):
        try:
            if message.author == self.user or  not message.content.startswith(prefix):
                return

            if not message.author.voice:
                return await message.channel.send('You need to be in a voice channel to use bot commands!')

            if not self.voice_clients and self.user in message.author.voice.channel.members:    # NOTE: DISCONNECT VC NOT RECOGNIZED
                await message.author.voice.channel.connect()
                await self.voice_clients[0].disconnect()
                return await message.channel.send('Bot encountered an error, please try using the command again!')



            command = message.content.lower().split(" ")[0][1:]
            content = " ".join(message.content.split(" ")[1:])      # NOTE: HASHED URLS MAY CONTAIN UPPER CASE LETTERS


            if not self.voice_clients and not command == 'leave' and not command == 'join':
                await summon(message)
                self.voice_channel = self.voice_clients[0]

                
            return await self.command_handler(message, command, content)


        except Exception as error:
            await message.channel.send('An error occurred..')
            await message.channel.send(f'Error: {error}')
            await self.on_disconnect(message)



    async def command_handler(self, message, command, content=''):

        try:
            if command == 'add':
                self.queue = await enqueue(self.queue, content, message)
                return

            elif command == 'play':
                await self.change_presence(status=discord.Status.online, activity=discord.Game('playing music'))
                self.queue = await enqueue(self.queue, content, message)
                if not self.voice_channel.is_playing():
                    self.queue = await play(self, self.queue, self.voice_channel, message)
                return

            elif command == 'join':
                if not self.voice_clients:
                    await summon(message)
                    self.voice_channel = self.voice_clients[0]
                    return
                await message.channel.send('Bot is already joined a vocie channel!', delete_after=5)
                return

            elif command == 'leave':
                if self.voice_clients:
                    self.queue = []
                    self.voice_channel = None
                    self.repeat = False
                    return await leave(self, message)
                await message.channel.send('Bot is not in a vocie channel!')
                return
                
            elif command == 'clear':
                self.repeat = False
                self.queue = await clear(self.queue, message)
                return

            elif command == 'queue':
                await queue(self.queue, message, self.repeat)
                return

            elif command == 'pause':
                await pause(self.voice_channel, self.queue, message)
                return
                
            elif command == 'resume':
                await resume(self.voice_channel, self.queue, message)
                return

            elif command == 'stop':
                self.repeat = False
                self.queue = await stop(self.voice_channel, self.queue, message)
                return

            elif command == 'skip':
                self.repeat = False
                await skip(self, self.voice_channel, self.queue, message)
                return

            elif command == 'replay':
                await replay(self, self.voice_channel, self.queue, message)
                return

            elif command == 'repeat':
                self.repeat = await repeat(self.queue, message, self.repeat)
                return

            elif command == 'volume':
                await volume(self.voice_channel, content, message)
                return

            elif command == 'help':
                await message.channel.send('Available commands: [Join, Leave, Add, Play, Pause, Resume, Replay, Repeat, Stop, Skip, Queue, Clear, Volume, and Help]')
                return

            else:
                await message.channel.send('Invalid command!')
                await message.channel.send('Available commands: [Join, Leave, Add, Play, Pause, Resume, Replay, Repeat, Stop, Skip, Queue, Clear, Volume, and Help]')  
                return

        except Exception as error:
            await message.channel.send('An error occurred..')
            await message.channel.send(f'Error: {error}')
            await self.on_disconnect(message)

music_bot = MusicBot()
music_bot.run(os.getenv('API_KEY'))