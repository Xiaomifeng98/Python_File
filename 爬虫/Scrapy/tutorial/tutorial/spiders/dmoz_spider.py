import scrapy

from ..items import DmozItem

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domain = ['dmoztools.net']
    start_urls = [
        'http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/',
        'http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/'
        ]

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//*[@id="site-list-content"]/div/div[3]')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/div/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('div/text()').extract()
            items.append(item)

        return items
