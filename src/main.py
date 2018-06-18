from bs4 import BeautifulSoup
import requests
import os

class BaseScraper():
    """
    MVP version of my project, work in progress.
    """

    def __init__(self):
        print ('...')


    def main(self):
        self.leechTorrent(self.download(self.getUrl()))

    def getUrl(self):
        """
        Parse the showpage and return the 1080p torrent link.
        """
        rq = requests.get('http://horriblesubs.info/lib/getshows.php? \
                            type=show&showid=347')
        soup = BeautifulSoup(rq.text, 'lxml')
        episode = soup.find("div", {"class":"one-piece-840-1080p"})
        episode_1080p = episode.find("td", {"class" : "hs-torrent-link"})
        torrent_link = episode_1080p.a.get('href')

        return torrent_link

    def download(self, torrent_link):
        """
        Download the torrent file.
        """
        r = requests.get(torrent_link, allow_redirects=True)
        torrent = 'C:/Users/dahoo/Downloads/onepiece840_1080p.torrent'

        with open(torrent,
                    'wb') as f:
            f.write(r.content)

        return torrent

    def leechTorrent(self, torrent):
        """
        Start uTorrent to download the epsiode.
        """
        
        os.system('C:\\Users\\dahoo\\AppData\\Roaming\\uTorrent\\uTorrent.exe \
        /DIRECTORY c:\\Users\\dahoo\\Downloads %s' % torrent)


if __name__ == "__main__":
    baseScraper = BaseScraper()
    baseScraper.main()
