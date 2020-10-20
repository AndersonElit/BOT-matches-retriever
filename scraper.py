import urllib.request
from bs4 import BeautifulSoup
import pickle
from bash import bash

class Scraper:

    def __init__(self):
        
        self.page_content = ''
        self.teams = []

    def get_page_content(self, url):

        content = urllib.request.urlopen(url)
        self.page_content = BeautifulSoup(content, 'html5lib')

    def get_teams(self):

        content = self.page_content
        tableteams = content.find_all('table', attrs = {'id':'results18891_overall'})
        tds = tableteams[0].find_all('td', attrs = {'data-stat':'squad'})

        for td in tds:

            team = td.a.text
            self.teams.append(team)

        #serialize temas list
        team_list = self.teams
        binary_file = open("teams_2018_2019", "wb")
        pickle.dump(team_list, binary_file)
        binary_file.close()

        #verify if the teams were saved
        file = open("teams_2018_2019", "rb")
        list = pickle.load(file)
        print(list)

        #move file to teams dir
        bash('mv teams_2018_2019 premier_league/teams/')