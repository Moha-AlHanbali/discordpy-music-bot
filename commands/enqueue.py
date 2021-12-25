"""This module enqueues a song into tracks queue"""

import youtube_dl


ytdl_opts = {
    'format': 'bestaudio/best',
    'quiet': True,
    'skip_download': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',

    }],
}

ytdl = youtube_dl.YoutubeDL(ytdl_opts)

async def enqueue(queue, url):
    """
    enqueue Adds a track to the bot track queue.

        Arguments:
            queue: MusicBot track queue
            url: str

        Return:
            Modified queue

    """
    song_info =  ytdl.extract_info(url)
    song = {
        'title': song_info['title'],
        'url': song_info['url']
    }

    queue.append(song)
    return queue