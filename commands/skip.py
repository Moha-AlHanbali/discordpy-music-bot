"""This module allows bot to skip a track"""

from .play import play

async def skip(bot, voice_channel, queue, message):
    """
    """
    if not queue:
            return await message.channel.send('Queue is empty!')

    voice_channel.stop()
    await message.channel.send(f'Skipped {queue[0]["title"]}!')

    if len(queue) > 1:
        queue.pop(0)
        queue =  await play(bot, queue, voice_channel, message)
        