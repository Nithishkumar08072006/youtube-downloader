from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_video():
    url = input("Enter the YouTube video URL: ")
    
    try:
        print("\nConnecting to YouTube...")
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")
        print("Downloading...")
        ys = yt.streams.get_highest_resolution()
        ys.download()    
        print("\n✅ Download Complete!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    download_video()