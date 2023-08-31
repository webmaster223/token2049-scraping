# First

# import requests
# from bs4 import BeautifulSoup
# # url = 'https://www.asia.token2049.com/speakers'
# url = 'https://www.payment.token2049.com/page/2484140?widget=true&'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.title)
# blog_titles = soup.select('.atom-fullname')
#
# for title in blog_titles:
#     print(title.text)

# Second
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
# Set up the Selenium webdriver
driver = webdriver.Chrome()  # You'll need to have the Chrome driver executable in your PATH
# Wait for the dynamic content to load
wait = WebDriverWait(driver, 10)
# url = 'https://www.asia.token2049.com/speakers'
url = 'https://www.payment.token2049.com/page/2484140?widget=true&'
driver.get(url)
dynamic_content = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.atom-fullname')))

# Get the page source with the dynamic content loaded
page_source = driver.page_source
driver.quit()  # Close the browser

# Now parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')
data_links = soup.select('.atom-fullname')
for link in data_links:
    print(link.text)


