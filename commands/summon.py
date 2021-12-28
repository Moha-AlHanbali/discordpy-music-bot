"""This module allows bot to join a voice channel"""

async def summon(message):
    """
    summon joins bot to user's voice channel.

        Arguments: 
            user: User instance

        Return: 
            Connects bot to VC 
    """
    try:
        return await message.author.voice.channel.connect()

    except Exception as error:
        await message.channel.send('An error occurred..')
        await message.channel.send(f'Error: {error}')