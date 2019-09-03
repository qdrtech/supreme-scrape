import scrapy
import time

class SupremeSpier(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'file:C:\\Users\\Q\\QRXCRK\\Projects\\Web\\python_selenium\\supreme-scrape\\spiders\\pants.html',
    ]

    def parse(self, response):
        i = 0
        articles = response.css('article > div > a')
        arcticleArray = [0]*len(articles)
        for article in articles:
            arcticleArray[i] = {
                'href': article.attrib['href'],
                'data': article.attrib['href']
            }
            i += 1
        print(arcticleArray[0])
        