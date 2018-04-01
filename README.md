## Unit 11 | Mars Landing

Skills Tested: MongoDB, Flask application, HTML, Webscraping (BeautifulSoup4, Splinter, Selenium, Twitter API/Search)

This program demonstrates Webscraping information from multiple websites.  Information such as tweets, images, and news articles is customly collected according to my preferences and then loaded onto my own webpage.  Webscraping involved utilizing BeautifulSoup4 and Selenium, 
BeautifulSoup only reads the html file that is loaded first, but does not read the executed javascript.  Hence only some of the articles were loaded using BS4, so the article scraping was handled with Selenium, which does read the javascript after it is executed in the html page.  
BS4 was then used to read the html file that Selenium created.  In addition to news articles, images/links were scraped using Splinter, this program automatically clicks the webpage buttons to automate scraping.  Splinter aided in collecting the full sized images, Splinter was able to render 
an html file in which BS4 was used to collect the link.  Furthermore, tweets from the mars weather account from nasa, was used to add current weather conditions on Mars.  However, not all the tweets were about the Mars weather, so a filter was used to filter out only the latest tweet about weather.

Coding was initially done in Jupyter Notebooks, and then copied to a python (.py) file.  The python file was then rewritten into a function that returns a dictionary with all of the information collected.  A flask app was then created where a connection to MongoDB uploaded all of the data collected 
(Mongo Compass was used to check successful DB upload).  Flask application was then used to pull information from the Mongo Database, and loaded onto a local connection.  When the HTML file/structure was loading onto the local host connection, it pulled the data from the Flask app, and loaded the information 
according to the HTML structure. 

(Note: apikeys file required for access to Twitter API)


![](images/Capture1.png)
__________________________________________________________________________________________________________________________________________

