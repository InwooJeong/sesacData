import scrapy
from navernews.items import NavernewsItem

class MybotsSpider(scrapy.Spider):
    name = "mybots"
    allowed_domains = ["news.naver.com"]
    # start_urls = ["https://news.naver.com/main/list.naver?mode=LS2D&sid2=262&mid=shm&sid1=101&page=%d" % i for i in range (1,10)]
    start_urls = ["https://news.naver.com/main/list.naver?mode=LS2D&sid2=262&mid=shm&sid1=101"]

    def parse(self, response):
        titles = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt[2]/a/text()').extract()
        # authors = response.css('.writing::text').extract()
        # previews = response.css('.lede::text').extract()
        
        # items = []
        # for idx in range(len(titles)):
        #     item = NavernewsItem()
        #     item['title'] = str(titles[idx]).strip()
        #     item['author'] = str(authors[idx]).strip()
        #     item['preview'] = str(previews[idx]).strip()
        #     items.append(item)
        # return items
        
        item = NavernewsItem()
        for idx in range(len(titles)):
            item['title'] = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt[2]/a/text()').get()
            item['author'] = response.css('.writing::text').get()
            item['preview'] = response.css('.lede::text').get()
            
            yield item
            
        next_page = response.css('.paging a::attr(href)').extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
            
