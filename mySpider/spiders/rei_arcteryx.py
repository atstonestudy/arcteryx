import scrapy
import math
import json
from mySpider.items import ClothItem


class ReiArcteryxSpider(scrapy.Spider):
    name = "rei_arcteryx"
    allowed_domains = ["ren.com"]
  
    def start_requests(self):
        print('----------start_start_requests----------------')
        urls = [
            'https://www.rei.com/b/arcteryx/c/all',
        ]

        for url in urls:
            print('----------request url----------------')
            print(url)
            yield scrapy.Request(url=url, headers={}, callback=self.parse)

    def parse(self, response):
        print('-----------------start parse-----------')
        print(response.url)
 
        selectors1 = response.xpath('//*[@id="search-page-wrapper"]/div[2]/div[4]/div[1]/text()')
        print(selectors1)
        aa = selectors1[0].extract()
        bb = aa.split(' ')
        total_count = bb[-2]
        print(total_count)
        pages = math.ceil(int(total_count)/30)
        # print(pages)

        for page in range(pages):
            if page == 0:
                url = "https://www.rei.com/b/arcteryx/c/all"
            else:
                url = "https://www.rei.com/b/arcteryx/c/all?page=%s" %(page+1)
            print("request url")
            print(url)
            yield scrapy.Request(url=url,dont_filter=True, callback=self.parse1)

    def parse1(self, response):
        print('-----------------start parse1-----------')
        print(response.url)

        selectors = response.xpath('//*[@id="search-results"]/ul/li')
        for s in selectors:
            href = s.xpath("./a[1]/@href").get()
            print("----------------href---------------------")
            print(href)
            url = "https://www.rei.com%s" %(href)
            print(url)
            yield scrapy.Request(url=url, dont_filter=True,callback=self.parse2)

    def parse2(self, response):
        print('-----------------start parse2-----------')
        print(response.url)
        # //*[@id="modelData"]
        selectors = response.xpath('//*[@id="modelData"]/text()')
        for s in selectors:
            print("----------------s---------------------")
            d = s.extract()
            # print(d)
            # print(type(d))
            json_data = json.loads(d)
          
            titile = json_data["pageData"]["product"]["title"]
            print(titile)
            skus = json_data["pageData"]["product"]["skus"]
            # print(skus)
            for sku in skus:
                cloth_item = ClothItem()
                cloth_item["title"] = titile
                cloth_item["color"] = sku["color"]["code"]
                cloth_item["color_name"] = sku["color"]["name"]
                cloth_item["size"] = sku["size"]["name"]
                cloth_item["price"] = sku["price"]["price"]["value"]
                cloth_item["raw_price"] = sku["price"]["price"]["compValue"]
                cloth_item["savingsPercentage"] = sku["price"]["savingsPercentage"]
                cloth_item["status"] = sku["status"]
                cloth_item["link"] = response.url
                # print("------------- crawl cloth item----------")
                # print(cloth_item)
                yield cloth_item

            
