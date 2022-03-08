import scrapy
import json
from datetime import datetime


class CareersSpider(scrapy.Spider):
    name = 'careers'
    allowed_domains = ['lever.co']
    #use internal Talent Relationship Management API
    urls = ['https://api.lever.co/v0/postings/economicmodeling?group=team&mode=json']

    def start_requests(self):
        for url in self.urls:
            #use JSON optimized request instead of default request
            yield scrapy.http.JsonRequest(url = url, callback = self.parse)


    def parse(self, response):
        data = json.loads(response.text)
        for category in data:
            num_jobs = len(category['postings'])
            for posting in category['postings']:
                yield {
                    'Job Title': posting.get('text'),
                    'Job Description': posting.get('descriptionPlain'),
                    'Location': posting.get('categories', {}).get('location'),
                    'Department': posting.get('categories', {}).get('department'),
                    'Commitment': posting.get('categories', {}).get('commitment'),
                    'Team': posting.get('categories', {}).get('team'),
                    'Team Openings': num_jobs,
                    #convert timestamp to datetime object
                    'Date Posted': datetime.fromtimestamp(posting.get('createdAt', 0)//1000),
                    'URL': posting.get('hostedUrl'),
                    'ID': posting.get('id'),
                }
           