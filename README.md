implementation for the tutorial on web scraping with the python scrapy
library.  


http://doc.scrapy.org/en/0.20/intro/tutorial.html  


when trying to scrape [tela-botanica](http://www.tela-botanica.org/appli:pictoflora?page=1&pas=12#page_recherche_images) the html code in response.body did not contain the images that can be
seen on the webpage. This may be because response only takes the
static html code, and since the images are contained in an iframe,
they are generated dynamically by the server and are not picked up by
response. next step would be to change reponse code such that it
returns the contents of the iframe as well.
