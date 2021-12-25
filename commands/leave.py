"""This module allows bot to leave a voice channel"""


async def leave(bot):
    """
    leave disconnnects bot from a voice channel.

        Arguments: 
            user: MusicBot instance

        Return: 
            Disconnects bot from VC 
    """
    return await bot.voice_clients[0].disconnect()