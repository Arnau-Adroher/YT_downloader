from pytube import YouTube

def download_video():
    try:
        # Get YouTube video URL from user input
        url = input("Enter the YouTube video URL: ")

        # Create a YouTube object
        yt = YouTube(url)

        # Try to get the stream with itag 299 (1080p, video and audio in one stream)
        video_stream = yt.streams.get_by_itag(299)

        # If itag 299 doesn't exist, get the highest resolution stream
        if not video_stream:
            video_stream = yt.streams.get_highest_resolution()

        # Print stylish video details
        print("\n----- Video Details -----")
        print("Title:", yt.title)
        print("Author:", yt.author)
        print("Published on:", yt.publish_date)
        print("Views:", f"{yt.views:,}")  # Add commas to views for better readability
        print("Duration:", yt.length, "seconds")
        print("Resolution:", video_stream.resolution)
        
        # Download the video
        print("\n----- Downloading -----")
        print("Please wait...")

        video_stream.download()

        print("\nDownload complete!")

    except Exception as e:
        print("\nError:", str(e))

def main():
    print("----- YT VIDEO DOWNLOADER -----")
    download_video()

if __name__ == "__main__":
    main()
