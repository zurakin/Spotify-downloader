from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import time


class Miner():
    def __init__(self, playlist_link):
        self.link = playlist_link
        self.titles_list = []
        self.driver = webdriver.Chrome('chromedriver.exe')
    def scrape(self):
        # r = requests.get(self.link)
        # c = r.content
        self.driver.get(self.link)
        time.sleep(2)
        c = self.driver.page_source
        cont = bs(c, "html.parser")
        all = cont.find('ol', {"class":"tracklist"})
        titles = all.find_all('div', {"class":"tracklist-name ellipsis-one-line"})
        artists = all.find_all('a', {"class":"tracklist-row__artist-name-link"})
        for t,a in zip(titles, artists):
            title = t.text.strip()
            artist = a.text.strip()
            self.titles_list.append([title,artist])
        # for s in songs_list:
            # title = s.find('div', {"class":"tracklis-name ellipsis-one-line"}).text.strip()
            # title = s.find('span', {"class":"track-name"}).text.strip()
            # artist = s.find('div', {"class":"TrackListRow__artists ellipsis-one-line"}).text.strip()
            # artist = s.find('span', {"class":"artists-albums"}).find('span').text.strip()

            # self.titles_list.append([title, artist])
        # print(len(songs_list))
