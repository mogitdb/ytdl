# YT-DLP Downloader README

This script is a simple graphical user interface (GUI) application that utilizes `yt-dlp` to download videos. The application is built with `tkinter` for Python and is designed to be simple af.

## Table of Contents

- Prerequisites
- Installation
- Features
- How to Use
- Troubleshooting
- License

## Prerequisites

- Python 3.x
- `yt-dlp` command-line utility
- `tkinter` for the GUI interface (Should be pre-installed with python otherwise -> pip install tkinter

## Installation

Before running the script, `yt-dlp` must be installed. The script checks for the presence of `yt-dlp` and installs it if it's not found: 

```
pip install yt-dlp
```

## Features

- Simple and easy-to-use GUI
- Downloads videos directly to the user's desktop in an `mp3/dl` folder
- Status updates provided through the GUI

## How to Use

1. Run the script using Python
    
3. Enter the video URL in the text field.
    
2. Click the "YTDLP" button to start the download.
    
3. The progress will be displayed in the application window.
## Troubleshooting

If the download doesn't start, check the following:

- Ensure the entered URL is valid and accessible.
- Check if `yt-dlp` is installed correctly and added to the system's PATH.
- Confirm that Python and `tkinter` are installed correctly.
## License

This script is provided "as is", without warranty of any kind. Feel free to use and modify it as needed. `yt-dlp` is released under the Unlicense and `tkinter` is part of Python's standard library. Please adhere to their respective licenses when using them in your projects.
