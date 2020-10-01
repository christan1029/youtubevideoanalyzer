# Author:  Christopher Tan

# youtube_video_analyzer.py searches YouTube for a user-provided amount of videos matching the user given search term.
# To run from terminal window:   python3 youtube_video_analyzer.py
# After running that command, user will be prompted twice; one for the amount of videos, and another for the search term.

from googleapiclient.discovery import build     
import csv 
import operator

API_KEY = "AIzaSyCsGXvPF1Br8po5JSh7xjvy6CSJZQMySIg"
API_NAME = "youtube"
API_VERSION = "v3"

# youtube_search prompts user for a search term (s_term) and a maximum number of videos (s_max) to search for.
# Searches youtube for s_term, retrieves videos up to s_max, and creates various lists containing different fields of data.
# Creates a CSV file named youtubedata.csv which contains the videos' ids, dates, titles, durations, view counts, and like counts.
# Prints the data results in the three lists in a user-friendly report form.

def youtube_search(s_term, s_max):
    totalList = []
    sortedDateList = []
    myList = []
    viewList = []
    sortedViewList = []
    likePercentList = []
    sortedPercentList = []
    youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)
    search_data = youtube.search().list(q=s_term, part="id,snippet", maxResults = s_max).execute()   
    # search for videos matching search term s_term
    for search_instance in search_data.get("items", []):
        # check if search instance is a video
        if search_instance["id"]["kind"] == "youtube#video":
            videoId = search_instance["id"]["videoId"]  
            title = search_instance["snippet"]["title"]
            date = search_instance["snippet"]["publishedAt"]        
            video_data = youtube.videos().list(id=videoId,part="contentDetails,statistics").execute()
            for video_instance in video_data.get("items",[]):
                viewCount = video_instance["statistics"]["viewCount"]
                duration = video_instance["contentDetails"]["duration"]
                if 'likeCount' in video_instance["statistics"]:
                    likeCount = video_instance["statistics"]["likeCount"]
                else:
                    likeCount = 0
            likecount = int(likeCount)
            viewcount = int(viewCount)
            if viewcount == 0:
                likePercent = 0
            else:
                likePercent = likecount/viewcount
            totalList.append([title,videoId,date,duration])
            viewList.append([title,videoId,date,duration,viewcount])
            myList.append([videoId, date, title, duration, viewcount, likecount])
            likePercentList.append([title, videoId, likePercent, viewcount, likecount, date, duration])
    filename = "youtubedata.csv"
    fields = ['Video ID', 'Date', 'Title', 'Duration', 'View Count', 'Like Count']  
    with open(filename, 'w', encoding="utf-8", newline='') as csvfile:   
        csvwriter = csv.writer(csvfile)   
        csvwriter.writerow(fields)    
        csvwriter.writerows(myList)
    sortedDateList = sorted(totalList, key=operator.itemgetter(2))
    sortedViewList = sorted(viewList, key=operator.itemgetter(4))
    sortedPercentList = sorted(likePercentList, key=operator.itemgetter(2))
    reversedDateList = sortedDateList[::-1] 
    reversedViewList = sortedViewList[::-1]
    reversedViewList = reversedViewList[0:5]
    reversedList = sortedPercentList[::-1] 
    reversedList = reversedList[0:5]
    print("Here are the all of the videos' titles, ids, dates, and durations sorted by newest first.\n")
    for i in reversedDateList:
        print("title = ", i[0], "\n video ID = ", i[1], ", date = ", i[2], ", duration = ", i[3], "\n")
    
    print("Here are the top 5 videos by viewcount and their titles, ids, dates, durations and views sorted by highest first.\n")
    for i in reversedViewList:
        print("title = ", i[0], "\n video ID = ", i[1], ", date = ", i[2], ", duration = ", i[3], ", views = ", i[4], "\n")
    
    print("Here are the top 5 videos by like percentage (like count / view count) and their titles, ids, percentage of likes, views, likes, dates, and durations sorted by highest percentage first.\n")
    for i in reversedList:
        print("title = ", i[0], "\n video ID = ", i[1], ", like percentage: ", i[2], ", views = ", i[3], ", likecount = ", i[4], ", date = ", i[5], ", duration = ", i[6], "\n")

a = input('Hello, please enter a search term. \n')
search_term = a
b = input('Now, please enter the maximum amount of videos to search for. \n')
search_max = b
print("Now searching youtube for search term: ",search_term, ",amount of videos: ", search_max)
youtube_search(search_term, search_max)