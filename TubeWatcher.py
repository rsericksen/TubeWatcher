import json
from datetime import datetime
from collections import Counter
from pprint import pprint

def mainMenu():
    """
    Creates and navigates a main directory
    """
    choice = ""
    while choice.upper() != "Q":
        print("1: First Watched Video (Channel Specific)")
        print("2: Watched Video Counter (Channel Specific)")
        print("3: Most Watched Video (Channel Specific)")
        print("4: Most Watched Video")
        print("5: Most Watched Channel")
        print("Q to QUIT")
        choice = input("Choose an option: ")
        if choice == "1":
            firstWatch()
            printLineBreak(1)
        elif choice == "2":
            countWatchedVideoChannel()
            printLineBreak(1)
        elif choice == "3":
            mostWatchedVideoByChannel()
            printLineBreak(1)
        elif choice == "4":
            mostWatchedVideo()
            printLineBreak(1)
        elif choice == "5":
            mostWatchedChannel()
            printLineBreak(1)

def printLineBreak(x):
    """
    Prints a specific line break display x times
    """
    for y in range(x):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

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

def firstWatch():
    """
    Prints the first watched video from a specific channel
    """
    channelName = input("Enter Channel Name: ")
    earliest = {'time': str(datetime.now()), 'name': channelName, 'title': "N/A"}

    for item in json.load(open('watch-history.json')):
        if "titleUrl" not in item:
            continue
        if "subtitles" not in item:
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
        printLineBreak(1)
        print("No videos found in history matching given Channel Name")
    else:
        printLineBreak(1)
        printEarliest(earliest)

def countWatchedVideoChannel():
    """
    Prints how many watched videos from a specific channel
    """
    watched = 0
    channelName = input("Enter Channel Name: ")

    for item in json.load(open('watch-history.json')):
        if "titleUrl" not in item:
            continue
        if "subtitles" not in item:
            continue
        if item["subtitles"][0]["name"].lower() == channelName.lower():
            if channelName != item["subtitles"][0]["name"]:
                channelName = item["subtitles"][0]["name"]
            watched += 1
            
    printLineBreak(1)
    print("You have watched " + str(watched) + " videos uploaded by " + channelName)

def mostWatchedVideoByChannel():
    """
    Prints most watched videos on a specific channel
    """
    channelName = input("Enter Channel Name: ")

    watched = Counter()
    limit = int(input("How many videos do you want to list?: "))

    for item in json.load(open('watch-history.json')):
        if "titleUrl" not in item:
            continue
        if "subtitles" not in item:
            continue
        if item["subtitles"][0]["name"].lower() == channelName.lower():
            title = item["title"]
            name = item["subtitles"][0]["name"]
            key = f"{title} by {name}"
            watched[key] += 1

    printLineBreak(1)
    for item in watched.most_common(limit):
        print(item)
        
def mostWatchedVideo():
    """
    Prints most watched videos overall
    """
    watched = Counter()
    limit = int(input("How many videos do you want to list?: "))

    for item in json.load(open('watch-history.json')):
        if "titleUrl" not in item:
            continue
        if "subtitles" not in item:
            continue
        title = item["title"]
        name = item["subtitles"][0]["name"]
        key = f"{title} by {name}"
        watched[key] += 1

    printLineBreak(1)
    for item in watched.most_common(limit):
        print(item)

def mostWatchedChannel():
    watched = Counter()
    limit = int(input("How many Channels do you want to list?: "))

    for item in json.load(open('watch-history.json')):
        if "titleUrl" not in item:
            continue
        if "subtitles" not in item:
            continue
        name = item["subtitles"][0]["name"]
        key = f"{name}"
        watched[key] += 1

    printLineBreak(1)
    for item in watched.most_common(limit):
        print(item)

mainMenu()