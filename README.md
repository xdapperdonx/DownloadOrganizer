Python program that automates downloads folder
Setup:
    1.) Create an executable using pyinstaller and title "DownloadOrganizer.exe". Use https://www.youtube.com/watch?v=UZX5kH72Yx4 for reference.
    2.) In StartMonitoring.ps1 change: folder to monitor: $watcher.Path = "D:\source", file filter to include only certain file types: watcher.Filter         = "*.*", include subdirectories yes/no: $watcher.IncludeSubdirectories = $true.
    3.) Make sure StartMonitoring.ps1 contains "Start-Process -FilePath "DownloadOrganizer.exe"".
    4.) Add StartMonitoring.ps1 to schedule Task Scheduler.
