# AnimeDownloader
UPDATE: The script no longer works because as pf 1-7-2018 the url 'http://horriblesubs.info/lib/getshows.php?type=show&showid=347' returns 404.
TODO: Fix this issue.

MVP version of my project.

Since i'm running this on a windows machine I'm using schtask to schedule the script to execute every sunday at 13:00 as follows:

- schtask /create /SC WEEKLY /D SUN /ST 13:00 /TN AnimeDownloader /TR file_path_python_file
