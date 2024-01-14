import subprocess
import sys
import os
import tkinter as tk
import threading

# Function to check if yt-dlp is installed
def is_yt_dlp_installed():
    try:
        subprocess.run(['yt-dlp', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

# Function to install yt-dlp using pip
def install_yt_dlp():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'yt-dlp'])

# Check and install yt-dlp if not installed
if not is_yt_dlp_installed():
    print("Installing yt-dlp...")
    install_yt_dlp()

# Function to handle the download process
def download_video():
    update_progress_label("Download in Progress...")
    url = url_entry.get()
    download_path = "C:\\dl"  # Updated download path
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    # Download the best video and audio separately and merge them
    video_command = [
        'yt-dlp',
        '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        '--merge-output-format', 'mp4',
        '-o', os.path.join(download_path, '%(title)s.%(ext)s'),
        url
    ]
    audio_command = [
        'yt-dlp',
        '-x', '--audio-format', 'mp3',
        '-o', os.path.join(download_path, '%(title)s.%(ext)s'),
        url
    ]
    try:
        subprocess.run(video_command, check=True)
        subprocess.run(audio_command, check=True)
        update_progress_label("Download Complete")
    except subprocess.CalledProcessError as e:
        update_progress_label("An error occurred: " + str(e))

# Function to update progress label
def update_progress_label(message):
    progress_label.config(text=message)
    root.update_idletasks()

# Function to run download in a separate thread
def start_download_thread():
    download_thread = threading.Thread(target=download_video)
    download_thread.start()

# Setting up the application window
root = tk.Tk()
root.title("YT-DLP Downloader")
root.geometry("400x200")  # Window size
root.configure(bg='black')

# Text Entry for URL
url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=20)

# Download Button
download_button = tk.Button(root, text="Download", command=start_download_thread, bg="white", fg="black")
download_button.pack(pady=10)

# Progress Label
progress_label = tk.Label(root, text="", bg="black", fg="white")
progress_label.pack(pady=5)

# Run the application
root.mainloop()