import urllib.request as urllib
from bs4 import BeautifulSoup

class PriceScraper:

    payload = None
    soup = None
    products = None

    def __init__(self, payload):
        self.payload = payload

    def scrape(self):
        page = urllib.urlopen(self.payload["url"])
        soup = BeautifulSoup(page, "html.parser")
        products = soup.findAll(self.payload["container"]["element"], attrs = { self.payload["container"]["itentifier"]: self.payload["container"]["value"]})

        return self.resolve(products)

    def resolve(self, products):
        if len(products) > 0:
            result = []
            for product in products:
                product_name = product.find(self.payload["items"]["name"]["element"], attrs = {self.payload["items"]["name"]["itentifier"]: self.payload["items"]["name"]["value"]})
                name = product_name.text
                product_price = product.find(self.payload["items"]["price"]["element"], attrs = {self.payload["items"]["price"]["itentifier"]: self.payload["items"]["price"]["value"]})
                price = product_price.text

                item = {"name": name, "price": price}
                result.append(item)

            return result

        else:
            return None
