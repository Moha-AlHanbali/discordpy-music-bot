"""This module allows bot to resume playing tracks"""

async def resume(voice_channel, queue, message):
    """
    resume resumes playing paused tracks

        Arguments:
            voice_channel: VoiceChannel Instance
            queue: MusicBot track queue
            message: Message instance

        Return:
            Sends a status message 
    """
    try:
        if not queue:
            return await message.channel.send('Queue is empty!')

        if not voice_channel.is_paused():
            return await message.channel.send('Queue is already playing!')

        voice_channel.resume()
        return await message.channel.send(f'Player resumed playing {queue[0]["title"]}!')

    except Exception as error:
        await message.channel.send('An error occurred..')
        await message.channel.send(f'Error: {error}')