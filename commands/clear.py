"""This module clears the track queue."""

async def clear(queue, message):
    """
    clear empties MusicBot track queue.

        Arguments:
            queue: MusicBot track queue

        Return:
            Modified queue
            
    """
    try:
        if not queue:
            await message.channel.send('Queue is already empty!')
        else:
            queue = queue[:1]
            await message.channel.send('Cleared queue!')
        return queue
    
    except Exception as error:
        await message.channel.send('An error occurred..')
        await message.channel.send(f'Error: {error}')
    