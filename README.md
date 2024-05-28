
# TubeWatcher

A collection of Python utilities to parse and analyze your YouTube watching habits




## Features

- Your most watched videos of all time
- Your most watched channels of all time
- Your first watch of a channel
- Your total number of watches for a channel


## Usage

* Download your YouTube watch history from Google Takeout: https://takeout.google.com/settings/takeout
    * Deselect all options and enable YouTube
    * Set History output to JSON format
    * Wait for email informing that download is ready

* Place the TubeWatcher Python script in the same directory as your watch-history.json file. 
    * This should be located within the path /Takeout/YouTube and YouTube Music/history/

* Run ```python TubeWatcher.py``` from the above directory in your Terminal