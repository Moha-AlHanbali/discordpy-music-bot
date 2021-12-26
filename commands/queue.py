"""This module shows bot track queue"""

async def queue(queue, message):
    """
    
    """
    if len(queue) == 0:
        return await message.channel.send('Queue is empty!')

    await message.channel.send('Songs in queue:')
    for track in range(len(queue)):
         await message.channel.send(f'{track + 1} - {queue[track]["title"]}')
    return