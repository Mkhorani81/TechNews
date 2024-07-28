import scrapy


class CrawltechItem(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()
    tags = scrapy.Field()
    resources = scrapy.Field()
