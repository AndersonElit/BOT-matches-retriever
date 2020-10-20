from scraper import Scraper

sc = Scraper()

print('getting page content..............................')

url = 'https://fbref.com/en/comps/9/1889/2018-2019-Premier-League-Stats'
sc.get_page_content(url)

print('saving teams')
sc.get_teams()










