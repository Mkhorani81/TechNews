from scrapy.exporters import JsonItemExporter

class CrawlTechError(JsonItemExporter):
    def __init__(self, file, **kwargs):
        super().__init__(file, ensure_ascii=False, **kwargs)