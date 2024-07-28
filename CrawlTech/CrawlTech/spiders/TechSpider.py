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
            data['title'] = info.css('div.BlockContainer__InnerArticleContainer-i5s1rc-1 > h1::text').get()
            data['text'] = info.css('div.article__StyledContainer-sc-3vhp3n-2 > div.box__BoxBase-sc-1ww1anb-0 > div.flex__Flex-le1v16-0 > div.BlockContainer__Root-i5s1rc-0 > div.BlockContainer__InnerArticleContainer-i5s1rc-1 > p::text').getall()
            data['tags'] = info.css('div.BlockContainer__InnerArticleContainer-i5s1rc-1 > div.flex__Flex-le1v16-0 > div.flex__Flex-le1v16-0 > a.link__CustomNextLink-sc-1r7l32j-0 > span::text').getall()
            data['resources'] = info.css('div.BlockContainer__InnerArticleContainer-i5s1rc-1 > div.flex__Flex-le1v16-0 > a.link__CustomNextLink-sc-1r7l32j-0 > div.flex__Flex-le1v16-0 > span::text').get()
            yield data
