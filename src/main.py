from bs4 import BeautifulSoup
import requests
import os
from requests.exceptions import ConnectionError
import logging


class BaseScraper():
    """
    MVP version of my project.
    """

    def __init__(self):
        print ('...')
        logging.basicConfig(format='%(levelname)s:%(asctime)s:%(message)s',
         filename='animeDownloader.log',level=logging.DEBUG)

    def main(self):
        self.leechTorrent(self.download_torrent(*self.getUrl()))

    def getUrl(self):
        """
        Parse the showpage and return the 1080p torrent link.
        """

        # Catch error if the page is not available.
        url = 'http://horriblesubs.info/lib/getshows.php?type=show&showid=347'
        try:
            rq = requests.get(url)
        except ConnectionError:
            logging.info('Offline, exiting now.')
            exit()

        soup = BeautifulSoup(rq.text, 'lxml')


        # Get latest epsiode description.
        episode_string_td = soup.find('tr').find(id).get_text()
        # Parse the number from the description.
        episode_number = ([str(s) for s in episode_string_td.split() \
                            if s.isdigit()][-1])
        # Use the number to build the class string.
        episode_class = 'one-piece-%s-1080p' % episode_number
        # Search for the div containing class string that contains our download.
        episode = soup.find("div", {"class":"%s" % episode_class})
        # Get the td thay contains the torrent link.
        episode_1080p = episode.find("td", {"class" : "hs-torrent-link"})
        # Get the torrent link.
        torrent_link = episode_1080p.a.get('href')

        return torrent_link, episode_number

    def download_torrent(self, torrent_link, episode_number):
        """
        Download the torrent file, if file already exists, exit.
        """
        r = requests.get(torrent_link, allow_redirects=True)
        torrent_filepath = 'C:/Users/dahoo/Downloads/onepiece%s_1080p.torrent' \
                            % episode_number

        if os.path.exists(torrent_filepath):
            logging.info('File already exists, exiting now.')
            exit()

        with open(torrent_filepath,
                    'wb') as f:
            f.write(r.content)

        return torrent_filepath

    def leechTorrent(self, torrent):
        """
        Start uTorrent to download the epsiode.
        """
        os.system('C:\\Users\\dahoo\\AppData\\Roaming\\uTorrent\\uTorrent.exe \
        /DIRECTORY c:\\Users\\dahoo\\Downloads %s' % torrent)


if __name__ == "__main__":
    baseScraper = BaseScraper()
    baseScraper.main()
