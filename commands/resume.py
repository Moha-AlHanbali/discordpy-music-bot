"""This module allows bot to resume playing tracks"""

async def resume(voice_channel, queue, message):
    """
    
    """
    if not queue:
        return await message.channel.send('Queue is empty!')

    if not voice_channel.is_paused():
        return await message.channel.send('Queue is already playing!')

    voice_channel.resume()
    return await message.channel.send(f'Player resumed playing {queue[0]["title"]}!')