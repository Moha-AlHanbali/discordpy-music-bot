"""This module allows bot to restart playing a track"""

from .skip import skip


async def replay(bot, voice_channel, queue, message):
    """
    replay restarts the current track

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

        queue.insert(1, queue[0])
        await message.channel.send(f'Replaying {queue[0]["title"]}!')
        return await skip(bot, voice_channel, queue, message)

    except Exception as error:
        await message.channel.send('An error occurred..')
        await message.channel.send(f'Error: {error}')