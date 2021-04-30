import scrapy

class UserSpider(scrapy.Spider):
    name = 'user'
    start_urls = ['https://lordsmobilemaps.com/en/player/ranking/power/36499']

    def parse(self, response, **kwargs):
        baseURL = 'https://lordsmobilemaps.com'
        for user in response.css('div.toptabrow'):
            yield {
                'name': user.css('div a::text').get()
            }

        next_page_options = response.css('div.container div.paginator div')
        next_page = next_page_options[len(next_page_options)-1].css('div').attrib['onclick']
        ext_url = next_page.replace("\'", "")
        ext_url = ext_url.replace("location=", "")
        next_page_url = baseURL + ext_url
        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse)