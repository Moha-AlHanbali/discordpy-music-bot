"""This module allows bot to leave a voice channel"""


async def leave(bot, message):
    """
    leave disconnnects bot from a voice channel.

        Arguments: 
            user: MusicBot instance

        Return: 
            Disconnects bot from VC 
    """
    try:
        return await bot.voice_clients[0].disconnect()

    except Exception as error:
        await message.channel.send('An error occurred..')
        await message.channel.send(f'Error: {error}')