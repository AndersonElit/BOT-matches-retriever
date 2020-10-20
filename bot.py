from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from utils import Utils

class BOT(Utils):

    def __init__(self):

        self.page_content = ''
        self.years = []
        super()

    def get_matches(self, url):

        driver = webdriver.Firefox()
        driver.get(url)

        # get temp
        content = driver.page_source
        self.page_content = BeautifulSoup(content, 'html5lib')
        page_content = self.page_content
        h1_tag = page_content.find_all('h1', attrs = {'itemprop':'name'})
        text = h1_tag[0].text
        self.years = self.get_years(text)

        # click in scores and fixtures
        navbar = driver.find_elements_by_class_name('full')[1]
        navbar.click()

        # deploy menu
        action = ActionChains(driver)
        despl = driver.find_element_by_class_name('section_heading_text')
        despl2 = despl.find_element_by_class_name('hasmore')
        action.move_to_element(despl2).perform()

        # get csv format
        csv_btn = despl2.find_elements_by_class_name('tooltip')[3]
        csv_btn.click()

        # get matches list
        page_content = driver.page_source
        self.page_content = BeautifulSoup(page_content, 'html5lib')
        content = self.page_content
        pre_tag = content.find_all('pre', attrs = {'id':'csv_sched_ks_26_1'})
        text = pre_tag[0].text