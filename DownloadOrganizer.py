#Python program that automates downloads folder
#Setup:
    #1.) Create an executable using pyinstaller and title "DownloadOrganizer.exe". Use https://www.youtube.com/watch?v=UZX5kH72Yx4 for reference.
    #2.) In StartMonitoring.ps1 change: folder to monitor: $watcher.Path = "D:\source", file filter to include only certain file types: $watcher.Filter = "*.*", include subdirectories yes/no: $watcher.IncludeSubdirectories = $true.
    #3.) Make sure StartMonitoring.ps1 contains "Start-Process -FilePath "DownloadOrganizer.exe"".
    #4.) Add StartMonitoring.ps1 to schedule Task Scheduler.

import os
import shutil

download_dir = "D:/Downloads"

doc_dir = "D:/Downloads/Documents"
if not os.path.isdir(doc_dir):
    os.mkdir(doc_dir)
audio_dir = "D:/Downloads/Audio"
if not os.path.isdir(audio_dir):
    os.mkdir(audio_dir)
img_dir = "D:/Downloads/Images"
if not os.path.isdir(img_dir):
    os.mkdir(img_dir)
video_dir = "D:/Downloads/Videos"
if not os.path.isdir(video_dir):
    os.mkdir(video_dir)
zip_dir = "D:/Downloads/Zip"
if not os.path.isdir(zip_dir):
    os.mkdir(zip_dir)

if(os.listdir(download_dir) !=  None):
    
    for file in os.listdir(download_dir):
        
        f_split = os.path.splitext(file)

        if f_split[1] == '.pdf' or  f_split[1] == '.docx' or  f_split[1] == '.txt' or f_split[1] == '.doc' or f_split[1] == '.html' or f_split[1] == '.htm' or f_split[1] == '.xls' or f_split[1] == '.xlsx' or f_split[1] == '.ods' or f_split[1] == '.ppt' or f_split[1] == '.pptx':
            shutil.move(download_dir+'/'+file, doc_dir)

        elif f_split[1] == '.mp3' or f_split[1] == '.m4a' or f_split[1] == '.flac' or f_split[1] == '.wav' or f_split[1] == '.wma' or f_split[1] == '.acc':
            shutil.move(download_dir+'/'+file, audio_dir)

        elif f_split[1] == '.jpg' or f_split[1] == '.jpeg' or f_split[1] == '.png' or f_split[1] == '.gif' or f_split[1] == '.tiff' or f_split[1] == '.psd' or f_split[1] == '.eps' or f_split[1] == '.ai':
            shutil.move(download_dir+'/'+file, img_dir)  

        elif f_split[1] == '.mp4' or f_split[1] == '.webm' or f_split[1] == '.mpg' or f_split[1] == '.ogg' or f_split[1] == '.avi' or f_split[1] == '.mov':
            shutil.move(download_dir+'/'+file, video_dir) 

        elif f_split[1] == '.zip':
            shutil.move(download_dir+'/'+file, zip_dir)