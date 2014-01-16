from scrapy.spider import BaseSpider

# this syntax means DmozSpider inherits from BaseSpider(?)
class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        # assigns to variable filename the substring of the URL between the 
        # last 2 occurences of '/' in the URL: 'Books', 'Resources'
        # uses that string to create a file with filename as name, to which
        # response.body is written
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)


# what's goign to happen?
# Scrapy creates scrapy.http.Request objects for each URL in the start_urls attribute of the Spider, and assigns them the parse method of the spider as their callback function.
# These Requests are scheduled, then executed, and scrapy.http.Response objects are returned and then fed back to the spider, through the parse() method.
