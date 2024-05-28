import json
from datetime import datetime
from collections import Counter
from pprint import pprint

def getReadableTime(givenTime):
    """
    Return a human-readable string containing the date of a watched video
    """
    givenTime = givenTime.replace("T", " ").replace("Z", "")[:-4]
    readTime = datetime.strptime(givenTime, "%Y-%m-%d %H:%M:%S").strftime("Watched on %b %d, %Y at %H:%M:%S")
    return readTime

def removeActionName(actionTitle):
    """
    Returns the title of the earliest watched video with the "Watched" action removed
    """
    title = actionTitle.replace("Watched ", "")
    return title

def printEarliest(earliest):
    """
    Prints the information of the earliest watched video
    """
    earliest["time"] = getReadableTime(earliest["time"])
    earliest["title"] = removeActionName(earliest["title"])
    print('"' + earliest["title"] + '"' + " by " + earliest["name"])
    print(earliest["time"])


channelName = input("Enter Channel Name: ")
earliest = {'time': str(datetime.now()), 'name': channelName, 'title': "N/A"}

for item in json.load(open('watch-history.json')):
    if "titleUrl" not in item:
        # Watched a video that has been removed
        continue
    if "subtitles" not in item:
        # Watched a video that has been removed
        continue

    title = item["title"]
    url = item["titleUrl"]
    dateWatch = item["time"]
    name = item["subtitles"][0]["name"]

    if name.lower() == channelName.lower():
        if dateWatch < earliest["time"]:
            earliest["time"] = dateWatch
            earliest["name"] = name
            earliest["title"] = title

if earliest["title"] == "N/A":
    print("No videos found in history matching given Channel Name")
else:
    printEarliest(earliest)