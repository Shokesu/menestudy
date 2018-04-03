import scrapy

from scraper.items.submission import  Submission

class MainSpider(scrapy.Spider):
    name = "main"

    start_urls =  [ 'https://www.meneame.net/?page=1',
                    'https://www.meneame.net/?page=2',
                  ]


    def parse(self, response):
        page = response.url.split("=")[-1]
        filename = 'main-{}.html'.format(page)
        #with open(filename, 'wb') as f:
        #    f.write(response.body)

        self.result = []


        for noticia in response.xpath("//div[@class='news-summary']"):
            id = noticia.xpath(".//div[@class='menealo']")[0].xpath("@id").extract_first()
            yield Submission(id=id)
