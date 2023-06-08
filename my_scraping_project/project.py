
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://us.shein.com/SHEIN-Toddler-Girls-Paperbag-Waist-Pants-p-2637486-cat-2121.html?src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dcat%60hz%3DhotZone_15%60ps%3D4_9%60jc%3Dreal_2031&src_module=Women&src_tab_page_id=page_home1686253555993&mallCode=1"
response = requests.get(url)

print(response.status_code)
print(response.headers)
print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
prices = soup.find_all('span', class_='product-intro__shipcheap')

# Write the prices to a text file
with open('output.txt', 'w') as file:
    for price in prices:
        file.write(price.text + '\n')

driver = webdriver.Chrome()
driver.get(url)

prices = driver.find_element_by_class_name('product-intro__shipcheap')
price = prices.text

driver.quit()

# Write the price to a text file
with open('output.txt', 'w') as file:
    file.write(price)






