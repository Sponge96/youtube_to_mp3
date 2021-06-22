import youtube_dl
import time


def run():
    video_url = input("Youtube URL: ")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    filename = "{}.mp3".format(video_info['title'])
    options = {
        'outtmpl': 'C:/Users/JPick/Desktop/{}'.format(filename),
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_url])
    print("*" * 20)
    print("File Downloaded")
    time.sleep(5)


if __name__ == '__main__':
    run()
