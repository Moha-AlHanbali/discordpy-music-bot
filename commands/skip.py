"""This module allows bot to skip a track"""

from .play import play

async def skip(bot, voice_channel, queue, message):
    """
    skip stops playing the current track and moves to the next one

        Arguments:
            bot: MusicBot instance
            voice_channel: VoiceChannel Instance
            queue: MusicBot track queue
            message: Message instance

        Return:
            Sends a status message
    """

    try:
        if not queue:
            return await message.channel.send('Queue is empty!')

        voice_channel.stop()
        await message.channel.send(f'Skipped {queue[0]["title"]}!')

        if len(queue) > 1:
            queue.pop(0)
            await play(bot, queue, voice_channel, message)
        
    except Exception as error:
        await message.channel.send('An error occurred..')
        await message.channel.send(f'Error: {error}')