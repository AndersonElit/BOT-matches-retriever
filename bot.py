from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from utils import Utils
import time


class BOT():

    def __init__(self):

        self.page_content = ''
        self.years = []
        self.teams = []
        self.matches = []

    def get_matches(self, url):

        utl = Utils()

        driver = webdriver.Firefox()
        driver.get(url)
        time.sleep(20)

        # get temp
        content = driver.page_source
        self.page_content = BeautifulSoup(content, 'html5lib')
        page_content = self.page_content
        h1_tag = page_content.find_all('h1', attrs={'itemprop': 'name'})
        text = h1_tag[0].text
        self.years = utl.get_years(text)
        temps_years = self.years

        while temps_years[0] <= 2018 and temps_years[1] <= 2019:

            print(f"obteniendo los datos para la temporada {str(temps_years[0])}-{str(temps_years[1])}")

            #get teams
            content = driver.page_source
            self.page_content = BeautifulSoup(content, 'html5lib')
            page_content = self.page_content
            tableteams = page_content.find_all('table')
            tds = tableteams[9].find_all('td', attrs = {'data-stat':'squad'})

            for td in tds:
                team = td.a.text
                self.teams.append(team)

            #serialize and save teams
            teams_list = self.teams
            utl.serialize_teams(temps_years, teams_list)

            # click in scores and fixtures
            navbar = driver.find_elements_by_class_name('full')[1]
            navbar.click()
            time.sleep(20)

            # deploy menu
            action = ActionChains(driver)
            despl = driver.find_element_by_class_name('section_heading_text')
            despl2 = despl.find_element_by_class_name('hasmore')
            action.move_to_element(despl2).perform()
            time.sleep(20)

            # get csv format
            csv_btn = despl2.find_elements_by_class_name('tooltip')[3]
            csv_btn.click()
            time.sleep(20)

            # get matches list
            page_content = driver.page_source
            self.page_content = BeautifulSoup(page_content, 'html5lib')
            content = self.page_content
            pre_tag = content.find_all('pre')
            text = pre_tag[0].text
            self.matches = utl.matches_list(text, teams_list)

            # serialize an save matches list
            all_matches = self.matches
            utl.serialize_matches(temps_years, all_matches)

            print(f"datos {temps_years[0]}-{temps_years[1]} recuperados")

            # click in overview
            navbar2 = driver.find_elements_by_class_name('full')[0]
            navbar2.click()
            time.sleep(20)

            # click in next season button
            next_btn = driver.find_element_by_class_name('next')
            next_btn.click()
            time.sleep(20)

            # get next temp
            content = driver.page_source
            self.page_content = BeautifulSoup(content, 'html5lib')
            page_content = self.page_content
            h1_tag = page_content.find_all('h1', attrs={'itemprop': 'name'})
            text = h1_tag[0].text
            self.years = utl.get_years(text)
            temps_years = self.years
            self.teams = []
            self.matches = []
            self.page_content = ''

        return ''