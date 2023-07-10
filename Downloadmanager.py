from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    while True:
        print("YouTube Video Download Manager")
        print("-----------------------------")
        print("1. Download a video")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            video_url = input("Enter the YouTube video URL: ")
            download_video(video_url)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
