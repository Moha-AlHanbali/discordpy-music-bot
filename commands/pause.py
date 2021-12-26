"""This module allows bot to pause playing"""

async def pause(voice_channel, queue, message):
    """
    pause stops bot from playing until resumed

        Arguments:
            voice_channel: VoiceChannel Instance
            queue: MusicBot track queue
            message: Message instance

        Return:
            Sends a status message
    """
    if not queue:
        return await message.channel.send('Queue is empty!')

    if voice_channel.is_paused():
        return await message.channel.send('Queue is already paused!')

    voice_channel.pause()
    return await message.channel.send(f'Player paused {queue[0]["title"]}!')

