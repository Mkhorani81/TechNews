import scrapy
from ..items import CrawltechItem

class CrawlTechSpider(scrapy.Spider):
    name = 'CrawlTechSpider'
    start_urls = ['https://www.zoomit.ir/', ]

    def parse(self, response):


        links = response.css('div.ArticleCard__ArticleContainer-sc-8cj56m-0 > a::attr(href)').getall()

        for link in links:
            link = response.urljoin(link)
            yield scrapy.Request(url=link, callback=self.news)

    def news(self, response):

        data = CrawltechItem()

        for info in response.css('article'):
            data['title'] = info.css('h1::text').get()
            data['text'] = info.css('p::text').getall()
            data['tags'] = info.css('div.flex__Flex-le1v16-0 > div.flex__Flex-le1v16-0 > a.link__CustomNextLink-sc-1r7l32j-0 > span::text').getall()
            data['resources'] = info.css('div.flex__Flex-le1v16-0 > a.link__CustomNextLink-sc-1r7l32j-0 > div.flex__Flex-le1v16-0 > span::text').get()

            data_dict = {
                'title': data['title'],
                'text': data['text'],
                'tags': data['tags'],
                'resources': data['resources'],
            }

            self.send_to_api(data_dict)

            yield data


    def send_to_api(self, data):
        api_url = 'http://127.0.0.1:80/api/news/'
        try:
            response = requests.post(api_url, data)
            response.raise_for_status()
            self.logger.info('Data successfully sent to API')

        except requests.exceptions.RequestException as e:
            self.logger.error(f'Failed to send data to API: {e}')