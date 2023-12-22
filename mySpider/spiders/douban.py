import scrapy


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250/"]


    def parse(self, response):
        print(response.body)
        movie_name = response.xpath("//div[@class='item']//a/span[1]/text()").extract()
        movie_core = response.xpath("//div[@class='star']/span[2]/text()").extract()
    #     yield {
    #         'movie_name':movie_name,
    #         'movie_core':movie_core
    #    }
        print("--------------------ret------------------")
        print(movie_name)
        print(movie_core)
        print("--------------------ret------------------")

