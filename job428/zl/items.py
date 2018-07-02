import scrapy


class ZhaopinzhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()
    loc = scrapy.Field()
    xueli = scrapy.Field()
    time = scrapy.Field()
    jy = scrapy.Field()
    info = scrapy.Field()
    link=scrapy.Field()