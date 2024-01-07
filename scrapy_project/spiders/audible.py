import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.com"]
    start_urls = ["https://www.audible.com/search"]

    def start_requests(self):
        # Editing the default headers (user-agent)
        yield scrapy.Request(
            url="https://www.audible.com/search/",
            callback=self.parse,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
            },
        )

    def parse(self, response, current_page=25):
        # pagination
        last_page = response.xpath(
            '//ul[contains(@class, "pagingElements")]//li[last()-1]//a//text() | //ul[contains(@class, "pagingElements")]//li[last()-1]//span//text()'
        ).get()

        product_container = response.xpath(
            '//div[@class="adbl-impression-container "]//li[contains(@class, "productListItem")]'
        )
        for product in product_container:
            title = product.xpath(
                './/li[contains(@class, "bc-list-item")]/h3/a/text()'
            ).get()
            author = product.xpath(
                './/li[contains(@class, "authorLabel")]/span/a/text()'
            ).get()
            length = (
                (
                    product.xpath(
                        './/li[contains(@class, "runtimeLabel")]/span/text()'
                    ).get()
                )
                .split(":")[1]
                .strip()
            )
            yield {
                "title": title,
                "author": author,
                "length": length,
                "page": current_page,
            }

        if current_page < int(last_page):
            next_page = current_page + 1
            yield response.follow(
                url=f"?page={next_page}",
                callback=self.parse,
                cb_kwargs={"current_page": next_page},
            )
