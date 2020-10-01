# youtubevideoanalyzer
Youtube search data processing using the YouTube API, written in Python.

youtube_video_analyzer.py prompts user for a search term and a maximum number of videos to search for. 
It then prints several user-friendly data reports about the videos it searched for and outputs a csv file containing the raw data of the videos that were retrieved with the following data fields for each video: id, publish date, video title, video duration, view count, like count.

## Getting Started

To get a local copy up and running:

1. Download the file youtube_video_analyzer.py.
2. If you would like to use your own API key, sign up [here](https://developers.google.com), enable Youtube Data API v3 and replace the API key used in line 11 with your own.
3. Run the file in your terminal with the command: python3 youtube_video_analyzer.py
4. Follow the prompts.
