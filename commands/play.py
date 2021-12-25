"""This module allows bot to play queued tracks"""

import discord


async def play(queue, voice_channel, message):
    """
    play allows bot to play a track in voice channel.

        Arguments:
            queue: MusicBot track queue
            voice_channel: VoiceChannel Instance
            message: Message instance

        Return:
            Modified queue
    """
    voice_channel.play(discord.FFmpegPCMAudio(queue[0]['url']))
    await message.channel.send(f'Started Playing {queue[0]["title"]}!')
    return queue.pop(0)