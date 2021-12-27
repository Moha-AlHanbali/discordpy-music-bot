"""This module allows bot to play queued tracks"""

import discord
import asyncio

from .play_next import play_next

async def play(bot, queue, voice_channel, message):
    """
    play allows bot to start playing queue tracks in voice channel.

        Arguments:
            bot: MusicBot instance
            queue: MusicBot track queue
            voice_channel: VoiceChannel Instance
            message: Message instance

        Return:
            Modified queue
    """

    voice_channel.play(discord.FFmpegPCMAudio(queue[0]['url'], before_options='-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'), after = lambda e: asyncio.run_coroutine_threadsafe(play_next(bot, queue, voice_channel, message), bot.loop))
    await message.channel.send(f'Started Playing {queue[0]["title"]}!')

    return queue