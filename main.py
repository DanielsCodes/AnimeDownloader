from bs4 import BeautifulSoup
import requests

class BaseScraper():

    def __init__(self):
        print ('...')

    def main(self):
        print (self.getUrl())

    # Parse the showpage and return the 1080p torrent link.
    def getUrl(self):
        rq = requests.get('http://horriblesubs.info/lib/getshows.php?type=show&showid=347')
        soup = BeautifulSoup(rq.text, 'lxml')
        episode = soup.find("div", {"class":"one-piece-840-1080p"})
        episode_1080p = episode.find("td", {"class" : "hs-torrent-link"})
        torrent_link = episode_1080p.a.get('href')

        return torrent_link


if __name__ == "__main__":
    baseScraper = BaseScraper()
    baseScraper.main()
