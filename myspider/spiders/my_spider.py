import scrapy

class myspider(scrapy.Spider):

    name = "myspider"
    
    start_urls = [
        'http://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89/%E7%AE%80%E5%8D%95%E7%89%88',
    ]

    def parse(self, response):
        
        r = response.xpath('//div[@class="mw-parser-output"]//tr')
        pmlist = []
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

                pmlist.append(newlist)
            except IndexError:
                continue
        self.log("pmlist: %s" % pmlist)

        with open('PMDEX.txt', 'w', encoding='utf-8') as f:
            for i in pmlist:
                nlist = []
                for each in i:
                    nlist.append(each[0])
                f.write(' '.join(nlist) + '\n')
            f.close()
        self.log("Write Finished!")
        
        '''
        r = response.xpath('//div[@class="mw-parser-output"]//tr')[5]
        rlist = r.xpath('td')

        newlist = []
        for i in range(4):
            if i == 0:
                newlist.append(rlist[i].xpath('text()').extract())
            else:
                newlist.append(rlist[i].xpath('a//text()').extract())

        self.log("list info: %s" % newlist)
        '''