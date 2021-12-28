"""This module allows bot to control player volume"""

import discord

async def volume(voice_channel, volume, message):
    """
    """
    try:  
        if volume == 'reset':
            voice_channel.source = discord.PCMVolumeTransformer(voice_channel.source)
            voice_channel.source.volume = 100/voice_channel.source.volume**2
            return await message.channel.send(f'Volume set to 100%!')

        if not 0 <= int(volume) <= 100:
            return await message.channel.send(f'Volume to has to be "reset" or a number between 0 and 100!')

        voice_channel.source = discord.PCMVolumeTransformer(voice_channel.source)
        voice_channel.source.volume = int(volume)/100
        await message.channel.send(f'Volume set to {volume}%!')

    except Exception as error:
        await message.channel.send(f'Volume to has to be "reset" or a number between 0 and 100!')
        await message.channel.send(f'Error: {error}')