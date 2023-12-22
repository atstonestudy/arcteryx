# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# -*- coding: utf-8 -*-
import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ranking = scrapy.Field()
    movie_name = scrapy.Field()
    score = scrapy.Field()

class TorrentItem(scrapy.Item):
    serial = scrapy.Field()  # number
    name = scrapy.Field()
    url = scrapy.Field()  # detail page
    image_url = scrapy.Field()
    magnets = scrapy.Field()  
    info = scrapy.Field()  
    score = scrapy.Field()  
    desc = scrapy.Field()  

class ClothItem(scrapy.Item):
    title = scrapy.Field()  
    color = scrapy.Field()
    color_name = scrapy.Field()  # detail page
    size = scrapy.Field()  
    price = scrapy.Field()  
    raw_price = scrapy.Field()  
    status = scrapy.Field()  
    savingsPercentage = scrapy.Field() 
    link = scrapy.Field()  
    ischange = scrapy.Field()  
    

