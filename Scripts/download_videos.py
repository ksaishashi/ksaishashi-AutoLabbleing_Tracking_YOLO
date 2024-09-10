import os
import pandas as pd
from pytube import YouTube
from urllib.parse import urlparse, parse_qs
import time

def clean_youtube_url(link):
    """Function to clean YouTube URL and retain only the base part."""
    parsed_url = urlparse(link)
    query_params = parse_qs(parsed_url.query)
    video_id = query_params.get('v')
    if video_id:
        # Construct clean URL
        return f"https://www.youtube.com/watch?v={video_id[0]}"
    return link

def download_youtube_video(link, download_folder, file_number):
    try:
        # Clean the URL before downloading
        clean_link = clean_youtube_url(link)

        # Create the download folder if it doesn't exist
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # Get the YouTube video
        yt = YouTube(clean_link)

        # Download the highest resolution video
        print(f"Downloading video: {yt.title}")
        stream = yt.streams.filter(file_extension='mp4').first() 
        downloaded_file = stream.download(output_path=download_folder)

        # Construct the new filename with the numbering (e.g., 1.mp4, 2.mp4)
        new_filename = f"{file_number}.mp4"
        new_file_path = os.path.join(download_folder, new_filename)

        # Replace backslashes with forward slashes
        new_file_path = new_file_path.replace("\\", "/")

        # Rename the downloaded file to the new filename
        os.rename(downloaded_file, new_file_path)
        print(f"Downloaded and renamed to: {new_filename}")

    except Exception as e:
        # Return the error message
        return f"An error occurred for {link}: {e}"
    return None  # No error

def download_videos_from_dataframe(df, download_folder):
    errors = []
    
    # Iterate over each link in the DataFrame and download the video
    for index, row in df.iterrows():
        link = row['Link']
        file_number = index + 1  # Start numbering from 1
        print(f"Processing {file_number}: {link}")
        error = download_youtube_video(link, download_folder, file_number)
        time.sleep(10)
        if error:
            errors.append(error)
    
    # Print summary after all downloads
    if errors:
        print("\nDownload completed with errors:")
        for err in errors:
            print(err)
    else:
        print("\nAll videos downloaded and renamed successfully!")

if __name__ == "__main__":

    df = pd.read_excel("../Intern_project/Tracker/Tracker.xlsx") 

    download_folder = "../Intern_project/Dataset/Videos"

    download_videos_from_dataframe(df, download_folder)
