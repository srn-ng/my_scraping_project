# my_scraping_project
steps:

1- the fist step is to instal the following things : 
   -Python .

   -requests library (pip install requests).

   -BeautifulSoup library (pip install beautifulsoup4) .

   -Selenium library (pip install selenium) .

2- Update the url variable with the desired website URL
3-Sends a GET request to the specified URL using the requests library.
3- print ( response.status_code /response.headers / response.text)
4-Parses the HTML response using BeautifulSoup.
5-Finds all elements with the CSS class "product-intro__shipcheap" and extracts their text.(to find the class of css in the inspect) 
6-the  prices is writen  to a text file named "output.txt".

################################

# using Selenium 
1-Opens the URL using a ChromeDriver-controlled browser.
2-Finds an element with the CSS class product-intro__shipcheap using Selenium and extracts its text.
3-Writes the extracted price to the same output.txt file.

################################
#DOCKER :

