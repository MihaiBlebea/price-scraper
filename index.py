# Libraries for web scraping
from price_scraper import PriceScraper
from cleaner import Cleaner
from writer import Writer

input = input("Are you ready to scrape (yes/no): ")

if input == "yes":

    data = [
        {
            "url": "http://totulestefengshui.ro",
            "container": {"element": "a", "itentifier": "class", "value": "woocommerce-LoopProduct-link woocommerce-loop-product__link"},
            "items": {
                "name": {"element": "h2", "itentifier": "class", "value": "woocommerce-loop-product__title"},
                "price": {"element": "span", "itentifier": "class", "value": "woocommerce-Price-amount amount"}
            }
        },
        {
            "url": "https://www.fengshui4life.ro/",
            "container": {"element": "div", "itentifier": "class", "value": "product-item-details"},
            "items": {
                "name": {"element": "a", "itentifier": "class", "value": ""},
                "price": {"element": "span", "itentifier": "class", "value": "price"}
            }
        }
    ]

    for index, item in enumerate(data):
        price_scraper = PriceScraper(item)
        scraped = price_scraper.scrape()

        cleaner = Cleaner()
        clean_data = cleaner.cleanArray(scraped)

        writer = Writer("output/data_" + str(index) + ".csv")
        writer.write(clean_data)

        print("Job completed for " + item["url"])
else:
    print("Oki, no worries")
