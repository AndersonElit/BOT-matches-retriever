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
        page_content = BeautifulSoup(content, 'html5lib')
        h1_tag = page_content.find_all('h1', attrs={'itemprop': 'name'})
        text = h1_tag[0].text
        years = utl.get_years(text)

        while years[0] < 2019 and years[1] < 2020:

            print(f"obteniendo los datos para la temporada {str(years[0])}-{str(years[1])}")

            #get teams
            content = driver.page_source
            page_content = BeautifulSoup(content, 'html5lib')
            tableteams = page_content.find_all('table')
            tds = tableteams[9].find_all('td', attrs = {'data-stat':'squad'})
            teams_list = []

            for td in tds:
                team = td.a.text
                teams_list.append(team)

            #serialize and save teams
            utl.serialize_teams(years, teams_list)

            # refresh page
            driver.refresh()
            time.sleep(20)

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
            page_content = BeautifulSoup(page_content, 'html5lib')
            pre_tag = page_content.find_all('pre')
            text = pre_tag[0].text
            matches = utl.matches_list(text, teams_list)

            # serialize an save matches list
            utl.serialize_matches(years, matches)

            print(f"datos {years[0]}-{years[1]} recuperados")

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
            page_content = BeautifulSoup(content, 'html5lib')
            h1_tag = page_content.find_all('h1', attrs={'itemprop': 'name'})
            text = h1_tag[0].text
            years = utl.get_years(text)

        return ''