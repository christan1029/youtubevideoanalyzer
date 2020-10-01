# youtubevideoanalyzer
Retrieves and processes data from youtube videos relating to a user-entered search term by using the YouTube API.

## About the program
youtube_video_analyzer.py prompts the user for a search term and a maximum number of videos to search for. 
It then prints several user-friendly data reports about the videos it searched for.
In addition, it creates a csv file containing the raw data of the videos that were retrieved with the following data fields for each video: id, publish date, video title, video duration, view count, like count.

## Getting Started

To get a local copy up and running:

1. Make sure you have the latest version of Python downloaded. For instructions, click [here](https://realpython.com/installing-python/).
2. Download the file youtube_video_analyzer.py.
3. (OPTIONAL) If you would like to use your own API key, sign up [here](https://developers.google.com), enable Youtube Data API v3 and replace the API key used in line 11 with your own.
4. Run the file in your terminal with the command: python3 youtube_video_analyzer.py
5. Follow the prompts.

## Output example
![Image Example](https://i.gyazo.com/aa81ff8fe0813f36cee67dbfe05482f6.png)

![Image Example2](https://i.gyazo.com/768f40ace84a43e9c779b8fff8f41997.png)

## Notes

The duration is represented as a ISO 8601 duration. For example, for a video that is at least one minute long and less than one hour long, the duration is in the format PT#M#S, in which the letters PT indicate that the value specifies a period of time, and the letters M and S refer to length in minutes and seconds, respectively. The # characters preceding the M and S letters are both integers that specify the number of minutes (or seconds) of the video. For example, a value of PT15M33S indicates that the video is 15 minutes and 33 seconds long.

If the video is at least one hour long, the duration is in the format PT#H#M#S, in which the # preceding the letter H specifies the length of the video in hours and all of the other details are the same as described above. If the video is at least one day long, the letters P and T are separated, and the value's format is P#DT#H#M#S. 
