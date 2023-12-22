import scrapy
from scrapy.linkextractors import LinkExtractor
from mySpider.items import TorrentItem


class Gaoqing888Spider(scrapy.Spider):
    name = 'gaoqing888'
    allowed_domains = ['www.gaoqing888.com']
    start_urls = ['https://www.gaoqing888.com/']
    link_extractor = LinkExtractor()

    def parse(self, response):
        if "detail" in response.url:
            torrent = TorrentItem()
            torrent['url'] = response.url
            torrent["serial"] = response.url.split("/")[-2]
            torrent["score"] = response.selector.xpath('//div/p[contains(@class, "rate-num")]/text()').get()
            torrent['name'] = response.selector.xpath("//div/h1[contains(@class, 'page-title')]/text()").get().strip()
            torrent['image_url'] = response.selector.xpath("//div[contains(@class, 'cover float-left')]/img/@src").get()
            torrent['info'] = "\n".join(item.replace("\xa0", ",") for item in response.selector.xpath("//div[contains(@class, 'info')]/ul/li/text()").getall())
            torrent['desc'] = '\n'.join(item.replace("\xa0", ",") for item in response.selector.xpath("//div/div/div[2]/p/text()").getall())
            selectors = response.xpath('//*[@id="download-list-standard"]/ul/li')
            magnets = []
            for s in selectors:
                magnets.append({
                    "name": s.xpath("//li/h6/text()").get(),
                    "size": s.xpath('//li/div/div/span[2]/text()').get(),
                    "quantity": s.xpath('//li/div/div/span[4]/text()').get(),
                    "link": s.xpath('//li/div/a/@href').get(),
                })
            torrent['magnets'] = magnets
            print("torrent-----------", torrent)
            yield torrent

        links = self.link_extractor.extract_links(response)
        for link in links:
            if "detail" in link.url:
                print("link--------------------", link)
                yield scrapy.Request(link.url)