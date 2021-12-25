"""This module allows bot to join a voice channel"""

async def summon(user):
    """
    summon joins bot to user's voice channel.

        Arguments: 
            user: User instance

        Return: 
            Connects bot to VC 
    """
    return await user.voice.channel.connect()