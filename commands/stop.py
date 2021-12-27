"""This module allows bot to stop playing a track"""

import discord

async def stop(voice_channel, queue, message):
    """
    stop ends the bot activity and clears queue

        Arguments:
            bot: MusicBot instance
            voice_channel: VoiceChannel Instance
            queue: MusicBot track queue
            message: Message instance

        Return:
            Modified queue
    """

    if not queue:
        await message.channel.send('Queue is empty!')
        return queue

    queue = []
    voice_channel.stop()
    await message.channel.send('Player stopped playing and cleared queue!')

    return queue


    