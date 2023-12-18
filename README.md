# YouTube Video Downloader

## Overview
This is a simple YouTube video downloader script written in Python using the Pytube library. The script prompts the user to input a YouTube video URL, retrieves video details, and downloads the video in the highest available resolution. To enhance the user experience, the script attempts to download videos in 1080p with both video and audio in one stream (itag 299) and falls back to the highest resolution available if itag 299 is not present.

## Prerequisites
Make sure you have Python installed on your system. You can install the required dependencies by running:

```bash
pip install pytube
```

## Prerequisites
Run the script by executing the following command in the terminal:

```bash
python YTDownloader.py
```
Enter the YouTube video URL when prompted.

The script will display video details such as title, author, publication date, views, duration, and resolution before initiating the download.

The video will be downloaded to the current working directory.

## Converting to .exe
To convert the script into a standalone executable (.exe) file, the PyInstaller tool was used. Follow these steps:

Install PyInstaller:

```bash
pip install pyinstaller
```
Run the following command in the terminal to create the executable:

```bash
pyinstaller --onefile --icon=icon.ico .\YTDownloader.py
```

This command packages the script into a single executable file (YTDownloader.exe) and associates the specified icon (icon.ico) with the executable.
The generated executable can be found in the dist directory.
