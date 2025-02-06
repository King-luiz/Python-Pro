
import yt_dlp

def download_yt_video(video_url, output_dir):
    ydl_opts = {
       'format': 'bestvideo[height<=100]',
    'noplaylist': True,
    
    
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
        
        if __name__== "__main__":
        video_url = input("Enter video url")
        download_yt_video(video_url)