from selenium import webdriver

characters = input('Que desea buscar?: ')

browser = webdriver.Chrome()
browser.get('https://google.com')
searchBar = browser.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')
searchBar.send_keys(characters)
searchBar = browser.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div[1]/div[3]/center/input[1]')
searchBar.click()

#browser.quit()