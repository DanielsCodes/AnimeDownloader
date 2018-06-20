from bs4 import BeautifulSoup
import requests
import os


class BaseScraper():
    """
    MVP version of my project.
    """

    def __init__(self):
        print ('...')


    def main(self):
        self.leechTorrent(self.download_torrent(*self.getUrl()))

    def getUrl(self):
        """
        Parse the showpage and return the 1080p torrent link.
        """
        rq = requests.get('http://horriblesubs.info/lib/getshows.php? \
                            type=show&showid=347')
        soup = BeautifulSoup(rq.text, 'lxml')

        if rq.status_code == 404:
            print ('Web-page not available, extiting now.')
            exit()

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
            print ('File already exists, exiting now.')
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
