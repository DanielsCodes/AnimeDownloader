# AnimeDownloader
MVP version of my project.

Since I'm running this on a windows machine I'm using schtask to schedule the script to execute every sunday at 13:00 as follows:

- schtask /create /SC WEEKLY /D SUN /ST 13:00 /TN AnimeDownloader /TR file_path_python_file
