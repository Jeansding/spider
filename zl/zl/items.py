import scrapy


class ZhaopinzhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()


    zwmc = scrapy.Field()
    gsmc = scrapy.Field()
    zwyx = scrapy.Field()
    gzdd = scrapy.Field()
    gsgm = scrapy.Field()
    minxueli = scrapy.Field()
    zprs = scrapy.Field()
    link=scrapy.Field()