from bs4 import BeautifulSoup
import requests
import os
import logging
import re

from requests.exceptions import ConnectionError

class BaseScraper():
    """
    MVP version of my project.
    """

    def __init__(self):
        print ('...')
        # Create logging object, write to animeDownloader.log in the same
        # directory as this file.
        logging.basicConfig(format='%(levelname)s:%(asctime)s:%(message)s',
         filename='animeDownloader.log',level=logging.DEBUG)

    def main(self):
        self.download_episode(self.getUrl())

    def getUrl(self):
        """
        Parse the RSS feed and return the 1080p torrent link.
        """
        url = 'https://horriblesubs.info/rss.php?res=1080'

        # Catch the error if the page is not available and exit.
        try:
            rq = requests.get(url)
        except ConnectionError:
            logging.info('Website unavailable, exiting now.')
            exit()

        # Create the paracble soup object.
        soup = BeautifulSoup(rq.text, 'lxml')
        # Find all items to get to the one containing One Piece.
        items = soup.find_all('item')
        onepiece_item = ""

        # Loop through all the items and extract the one containing One Piece.
        for item in items:
            if "One Piece" in item.getText():
                onepiece_item = item

        # Extract the magnet url from the whole string.
        dl_link = onepiece_item.getText().split('mkv',1)[1]
        return dl_link

    def download_episode(self, dl_link):
        """
        Download the episode.
        """
        os.startfile(dl_link)


if __name__ == "__main__":
    baseScraper = BaseScraper()
    baseScraper.main()
