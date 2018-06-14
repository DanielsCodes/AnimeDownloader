from bs4 import BeautifulSoup
import requests

class BaseScraper():

    def __init__(self):
        print ('...')

    def main(self):
        rq = requests.get('http://horriblesubs.info/lib/getshows.php?type=show&showid=347')
        soup = BeautifulSoup(rq.text, 'lxml')
        episode = soup.find("div", {"class":"one-piece-840-1080p"})
        print (soup.div.a.get('href'))
        torrent = episode.find("td", {"class" : "hs-torrent-link"})
        torrent_link = torrent.a.get('href')


if __name__ == "__main__":
    baseScraper = BaseScraper()
    baseScraper.main()
