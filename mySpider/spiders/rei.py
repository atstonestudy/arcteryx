import scrapy
import random
import math
import json


class ReiSpider(scrapy.Spider):
    name = "rei"
    allowed_domains = ["rei.com"]
    # start_urls = ["https://www.rei.com/c/mens-casual-jackets"]

    def start_requests(self):
        urls = [
            'https://www.rei.com/c/mens-jackets',
            # "https://www.rei.com/c/mens-jackets?page=2",
            # "https://www.rei.com/c/mens-jackets?page=3"
        ]
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        # }

        # headers = {
        #     'User-Agent': random.choice(
        #                     [
        #                         'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
        #                         'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
        #                         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
        #                         'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        #                         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        #                         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        #                         'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
        #                         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        #                         'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)',
        #                         'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
        #                         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
        #                         'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
        #                         'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        #                         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
        #                         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
        #                         'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
        #                         'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        #                         'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)',
        #                         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
        #                         'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.3 Mobile/14E277 Safari/603.1.30',
        #                         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        #                     ]
        #                 )
        # }

        for url in urls:
            print('----------start_start_requests----------------')
            print(url)
            yield scrapy.Request(url=url, headers={}, callback=self.parse)

    def parse(self, response):
        print('-----------------start parse-----------')
        print(response.url)

        if "product" not in response.url:
            # selectors1 = response.xpath('//*[@id="search-page-wrapper"]/div[2]/div[3]/nav')
            selectors1 = response.xpath('//*[@id="search-page-wrapper"]/div[2]/div[4]/div[1]/text()')
            # //*[@id="search-page-wrapper"]/div[2]/div[4]/nav/a[1]
            # //*[@id="search-page-wrapper"]/div[2]/div[3]/div
            # //*[@id="search-page-wrapper"]/div[2]/div[3]
            print(selectors1)
            aa = selectors1[0].extract()
            bb = aa.split(' ')
            total_count = bb[-2]
            print(total_count)
            pages = math.ceil(int(total_count)/30)
            print(pages)

            for page in range(1,2):
                url = "https://www.rei.com/c/mens-jackets?page=%s" %(page+1)
                print(url)
                yield scrapy.Request(url=url, callback=self.parse1)
            


            
            # selectors1 = response.css('.Xmeb0HiaydoDNE3js2WD')

            # for s in selectors1:
            #     print("------------")
            #     aa = s.extract()
            #     print(aa)
            #     bb = aa.split(' ')
            #     print(bb[-2])
   
            # selectors = response.xpath('//*[@id="search-results"]/ul/li')
            # for s in selectors:
            #     aa = s.xpath("./a[1]/@href").get()
            #     print("----------------href---------------------")
            #     print(s)
            #     print("------------")
            #     print(aa)
            print("--------------end parse-------------------")

        else:
            return

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
            yield scrapy.Request(url=url, callback=self.parse2)
           
    def parse2(self, response):
        print('-----------------start parse2-----------')
        print(response.url)
        # //*[@id="modelData"]
        selectors = response.xpath('//*[@id="modelData"]/text()')
        for s in selectors:
            print("----------------s---------------------")
            d = s.extract()
            # print(d)
            print(type(d))
            json_data = json.loads(d)
            print(json_data["pageData"]["product"]["title"])
            # dd = eval(d)
            # print(dd["pageData"])


