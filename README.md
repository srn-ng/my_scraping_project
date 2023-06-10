# my_scraping_project
#using requests and beautifulsoup4 :

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

5-Finds all elements with the CSS class "product-intro__shipcheap" and extracts their text.(To  find the CSS class, you should right-click and select 'Inspect' to open the inspection tool. Then, inspect the element and search for the desired class.)

6-the  prices is writen  to a text file named "output.txt".

################################

# using Selenium 
1-Opens the URL using a ChromeDriver-controlled browser.

2-Finds an element with the CSS class product-intro__shipcheap using Selenium and extracts its text.

3-Writes the extracted price to the same output.txt file.

################################
## Dockerfile Explanation
we use this step  to build a Docker image for running the `project.py` script. ( project of DATA_SCRAPING )

The Dockerfile provided performs the following actions:

- Uses the `python:3.7-alpine` as the base image.( alpine  is small size  Linux distribution.To execute the code quickly)
- Sets the working directory inside the container to `/app`.
- Copies the `requirements.txt`, `project.py`, and `README.md` (if present) files to the `/app` directory.
- Installs the dependencies specified in `requirements.txt` using pip.
- Sets the default command to execute as `python project.py` when the container starts.




