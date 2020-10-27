import scrapy

with open("Expose.txt","r") as f:
    exposes = f.read()
exposes = "exposes="+exposes
exec(exposes)

url_root = 'https://www.immowelt.de/expose/'
start_urls = [url_root+a for a in exposes]

class QuotesSpider(scrapy.Spider):
    name = "expose"
    start_urls = start_urls

    def parse(self, response):
        filename = '2wj2541'
        
        #with open(filename, 'wb') as f:
         #   f.write(response.body)
        yield {
            'titel' : response.xpath('//title/text()').get(),
            'ort' : response.xpath('//div[@class="location"]/span/text()').get(),
            'merkmale' :  response.xpath('//div[@class="merkmale"]/text()').get(),
            'stadteilbewertung' :  response.xpath('//div[contains(@id,"divRating")]').get(),
            'energielabel' : response.xpath('//div[@class="datatable energytable clear"]/div/span[@class="datalabel"]/text()').getall(),
            'energiemerkmale' : response.xpath('//div[@class="datatable energytable clear"]/div/span[@class="datacontent"]/text()').getall(),
            'kaufpreis' : response.xpath('//div[@id="statusFacts"]').xpath('//div[@class="hardfact"]/strong/strong/text()').getall()[0],
            'anzahl_raeume': response.xpath('//div[@id="statusFacts"]').xpath('//div[@class="hardfact rooms"]/text()').get(),
            'wohnflaeche' : response.xpath('//div[@id="statusFacts"]').xpath('//div[@class="hardfact "]/text()').getall()[3],
            'grundstuecksflaeche' : response.xpath('//div[@id="statusFacts"]').xpath('//div[@class="hardfact "]/text()').getall()[5],  
        }