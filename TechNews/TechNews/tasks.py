from celery import shared_task
from scrapy.crawler import CrawlerProcess
import os
from CrawlTech.CrawlTech.spiders.TechSpider import CrawlTechSpider
import requests

@shared_task
def run_spider():
    os.system('scrapy runspider /scrapy/CrawlTech/spiders/TechSpider.py')


# @shared_task
# def run_crawler():
#     process = CrawlerProcess(settings={
#         "FEEDS": {
#             "output.json": {"format": "json"},
#         },
#     })
#     process.crawl(CrawlTechSpider)
#     process.start()
#
#     with open("output.json") as f:
#         data = f.read()
#         response = requests.post("http://django_app:8000/api/news/", data=data)
#         return response.status_code