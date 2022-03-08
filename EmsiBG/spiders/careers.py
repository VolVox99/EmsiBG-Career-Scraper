import scrapy
import json


class CareersSpider(scrapy.Spider):
    name = 'careers'
    allowed_domains = ['lever.co']
    #use internal Talent Relationship Management API
    urls = ['https://api.lever.co/v0/postings/economicmodeling']

    def start_requests(self):
        for url in self.urls:
            #use JSON optimized request instead of default request
            yield scrapy.http.JsonRequest(url = url, callback = self.parse)


    def parse(self, response):
        data = json.loads(response.text)
        yield from data