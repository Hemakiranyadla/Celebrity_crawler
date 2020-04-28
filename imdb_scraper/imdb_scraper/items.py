# -*- coding: utf-8 -*-

import scrapy


class ImdbScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field()
    Profession = scrapy.Field()
    Dob = scrapy.Field()
    Picture = scrapy.Field()
    Notable_work = scrapy.Field()
