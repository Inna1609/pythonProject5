from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
def test_about_sunn():
    driver = Chrome()
    driver.get('https://www.gomotionapp.com/team/sunn/page/home')
    about_sunn_locator = "//body/div[@id='globalContainer']/div[@id='headerPane']/div[@id='menuBar']/div[@id='cms_Section_menuBar']/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/span[1]"
    about_sunn_element = driver.find_element(by='xpath', value=about_sunn_locator)
    about_sunn_element.click()
    time.sleep(5)

def test_programs():
    driver = Chrome()
    driver.get('https://www.gomotionapp.com/team/sunn/page/home')
    programs_locator = "//body/div[@id='globalContainer']/div[@id='headerPane']/div[@id='menuBar']/div[@id='cms_Section_menuBar']/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]/span[1]"
    programs_element = driver.find_element(by='xpath', value=programs_locator)
    programs_element.click()
    time.sleep(5)

def test_safe_sport():
    driver = Chrome()
    driver.get('https://www.gomotionapp.com/team/sunn/page/home')
    safe_sport_locator = "//body/div[@id='globalContainer']/div[@id='headerPane']/div[@id='menuBar']/div[@id='cms_Section_menuBar']/div[1]/div[1]/div[1]/ul[1]/li[4]/a[1]/span[1]"
    safe_sport_element = driver.find_element(by='xpath', value=safe_sport_locator)
    safe_sport_element.click()
    time.sleep(5)

def test_events():
    driver = Chrome()
    driver.get('https://www.gomotionapp.com/team/sunn/page/home')
    events_locator = "//body/div[@id='globalContainer']/div[@id='headerPane']/div[@id='menuBar']/div[@id='cms_Section_menuBar']/div[1]/div[1]/div[1]/ul[1]/li[5]/a[1]/span[1]"
    events_element = driver.find_element(by='xpath', value=events_locator)
    events_element.click()
    time.sleep(5)

def test_join_our_team():
    driver = Chrome()
    driver.get('https://www.gomotionapp.com/team/sunn/page/home')
    join_our_team_locator = "//span[contains(text(),'Join our Team')]"
    join_our_team_element = driver.find_element(by='xpath', value=join_our_team_locator)
    join_our_team_element.click()
    time.sleep(5)

def test_find_store():
    driver = Chrome()
    driver.get('https://walmart.com')
    find_store_locator = "//div[contains(text(),'My Items')]"
    find_store = driver.find_element(by='xpath', value=find_store_locator)
    find_store.click()


'''def test_sign_in():
    driver = Chrome()
    driver.get('https://walmart.com')
    sign_in_locator = "//div[contains(text(),'Account')]"
    sign_in_element = driver.find_element(by='xpath', value=sign_in_locator)
    sign_in_element.click()

def test_basket():
    driver = Chrome()
    driver.get('https://walmart.com')
    basket_locator = "//header/div[4]/div[1]/div[1]/button[1]/i[1]"
    basket_element = driver.find_element(by='xpath', value=basket_locator)
    basket_element.click()
    driver.get ('https://www.walmart.com/cart')
    second_page_locator = "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/img[1]"
    second_page = driver.find_element(by='xpath', value=second_page_locator)
    time.sleep(5)
def test_services():
    driver = Chrome()
    driver.get('https://walmart.com')
    services_locator = "//header/section[2]/div[1]/a[1]"
    services = driver.find_element(by='xpath', value=services_locator)
    services.click()'''
