import scrapy


class JogosSpider(scrapy.Spider):
    name = 'jogos'
    start_urls = ['https://boardgamegeek.com/browse/boardgame/page/1']

    def parse(self, response):
         for jogo in response.css('#row_'):
             yield{
                'rank': jogo.css('.collection_rank a::attr(name)').get(),
                'nome': jogo.css('.primary ::text').get(),
                'avaliacao': jogo.css('#row_ .collection_bggrating:nth-child(5) ::text').get().split()[0]  # split para trazer somente o valor da nota (item 0 da lista)
             }

         proxima_pagina = response.xpath('//*[@id="maincontent"]/form/div/div[1]/a[5]').attrib['href']
         if proxima_pagina is not None:
            yield  response.follow(proxima_pagina, callback=self.parse)
