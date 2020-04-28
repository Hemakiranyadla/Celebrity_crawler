# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

SEARCH_QUERY = (
    'https://www.imdb.com/search/name/?'
    'gender=male,female&'
    'has=awards&'
    'ref_=rlm'
)


class MovieSpider(CrawlSpider):
    name = 'celeb'
    allowed_domains = ['imdb.com']
    start_urls = [SEARCH_QUERY]

    rules = (Rule(
        LinkExtractor(restrict_css=('div.desc a')),
        follow=True,
        callback='parse_query_page',
    ),)

    def parse_query_page(self, response):
        links = response.css('h3.lister-item-header a::attr(href)').extract()
        for link in links:
            yield response.follow(link, callback=self.parse_celeb_detail_page)

    def parse_celeb_detail_page(self, response):
        data = {}
        data['Name'] = response.css('span.itemprop::text').extract_first()
        data['Profession'] = response.css('span.itemprop::text')[1].extract().strip()
        data['Dob'] = response.css('time::attr(datetime)').extract_first()
        data['picture'] = response.css('img#name-poster::attr(src)').extract_first()
        works = response.css('div.knownfor-title-role > a::attr(title)').extract()
        data['notable_work'] = [work.strip() for work in works]

        yield data
