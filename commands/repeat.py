"""This module allows bot to play a track on a loop"""


async def repeat(queue, message, repeat):
    """
    repeat sets the repeat mode for the current track on or off

        Arguments:
            queue: MusicBot track queue
            message: Message instance
            repeat: boolean

        Return:
            repeat: boolean
    """

    if not queue:
        return await message.channel.send('Queue is empty!')
    
    if not repeat:
        repeat = True
        await message.channel.send(f'Turned ON repeat for {queue[0]["title"]}!')
    else:
        repeat = False
        await message.channel.send(f'Turned OFF repeat for {queue[0]["title"]}!')

    return repeat