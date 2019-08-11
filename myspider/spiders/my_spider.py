import scrapy
from myspider.items import MyspiderItem

class myspider(scrapy.Spider):

    name = "myspider"
    domain = 'https://wiki.52poke.com'
    start_urls = [
        'http://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89/%E7%AE%80%E5%8D%95%E7%89%88',
    ]

    def parse(self, response):
        r = response.xpath('//div[@class="mw-parser-output"]//tr')
        pmItem = MyspiderItem()
        for i in range(len(r)):
            try:
                rlist = r[i].xpath('td')
                newlist = []
                for j in range(4):
                    if j == 0:
                        templist = []
                        templist.append(rlist[j].xpath('text()').extract()[0].strip('\n'))
                        newlist.append(templist)
                    else:
                        newlist.append(rlist[j].xpath('a//text()').extract())
                pmItem["pm_dexId"] = newlist[0][0]
                pmItem["pm_name_cn"] = newlist[1][0]
                pmItem["pm_name_jp"] = newlist[2][0]
                pmItem["pm_name_en"] = newlist[3][0]
                pmItem["pm_url"] = self.domain + r[i].xpath('td/a/@href').extract_first()
                yield scrapy.Request(pmItem["pm_url"], callback=self.parse_detail, meta=pmItem)
            except IndexError:
                continue
            
    def parse_detail(self, response):
        pmItem = response.meta
        r1 = response.xpath('//td/b/a[@title="属性"]/../following-sibling::table')[0]
        r2 = response.xpath('//td/b/a[@title="特性"]/../following-sibling::table')[0]
        typelist = r1.xpath('tbody//span/a/text()').extract()
        typelist = list(map(str.strip, typelist))
        pmItem["pm_Type"] = typelist
        pmItem["pm_Abi"] = r2.xpath('tbody//td/a/text()').extract()
        pmItem["pm_HP"] = int(response.xpath('//th[@class="bgl-HP"]/text()').extract_first().strip())
        pmItem["pm_Atk"] = int(response.xpath('//th[@class="bgl-攻击"]/text()').extract_first().strip())
        pmItem["pm_Def"] = int(response.xpath('//th[@class="bgl-防御"]/text()').extract_first().strip())
        pmItem["pm_SAtk"] = int(response.xpath('//th[@class="bgl-特攻"]/text()').extract_first().strip())
        pmItem["pm_SDef"] = int(response.xpath('//th[@class="bgl-特防"]/text()').extract_first().strip())
        pmItem["pm_Spd"] = int(response.xpath('//th[@class="bgl-速度"]/text()').extract_first().strip())
        yield pmItem


