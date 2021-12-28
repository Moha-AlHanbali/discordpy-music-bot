"""This module enqueues a song into tracks queue"""

import youtube_dl

ytdl_opts = {
    'format': 'bestaudio/best',
    'default_search': 'auto',
    'quiet': True,
    'skip_download': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',

    }],
}

ytdl = youtube_dl.YoutubeDL(ytdl_opts)

async def enqueue(queue, url, message):
    """
    enqueue detects if the message containes keywords or urls and adds the requested track to the bot track queue.

        Arguments:
            queue: MusicBot track queue
            url: str
            message: Message instance

        Return:
            Modified queue

    """

    try:
        song_info =  ytdl.extract_info(url, download = False)
        if 'formats' in song_info:
            song = {
                'title': song_info['title'],
                'url': song_info['url']
            }

        if 'entries' in song_info:
            song = {
                'title': song_info['entries'][0]['title'],
                'url': song_info['entries'][0]["formats"][0]['url']
            }

        queue.append(song)

        await message.channel.send(f'Added {song["title"]} to queue!')

        return queue

    except Exception as error:
        await message.channel.send('An error occurred..')
        await message.channel.send(f'Error: {error}')