"""This module shows bot track queue"""

async def queue(queue, message, repeat):
    """
    queue sends a message with the current track queue state

        Arguments:
            queue: MusicBot track queue
            message: Message instance
            repeat: boolean

        Return:
            repeat: None           
    """
    if len(queue) == 0:
        return await message.channel.send('Queue is empty!')

    
    for track in range(len(queue)):
        if  track == 0:
            if repeat:
                await message.channel.send(f' Currently playing: {queue[track]["title"]} - [ON REPEAT]')
            else:
                await message.channel.send(f' Currently playing: {queue[track]["title"]}')

            if len(queue) > 1:
                await message.channel.send('Songs in queue:')
            else:
                await message.channel.send('Nothing else enqueued!')         
                       
            continue

        await message.channel.send(f'{track} - {queue[track]["title"]}')
