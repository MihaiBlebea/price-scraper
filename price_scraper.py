import urllib.request as urllib
from bs4 import BeautifulSoup

class PriceScraper:
    url = "http://totulestefengshui.ro"
    soup = None
    products = None

    def __init__(self):
        self.page = urllib.urlopen(self.url)
        self.soup = BeautifulSoup(self.page, "html.parser")
        self.products = self.soup.findAll("a", attrs = {"class": "woocommerce-LoopProduct-link woocommerce-loop-product__link"})

    def scrape(self):
        if self.products != None:
            result = []
            for product in self.products:
                product_name = product.find("h2", attrs = {"class": "woocommerce-loop-product__title"})
                name = product_name.text
                product_image = product.find("img", attrs = {"class": "attachment-shop_catalog size-shop_catalog wp-post-image"})
                image = product_image["src"]
                product_price = product.find("span", attrs = {"class": "woocommerce-Price-amount amount"})
                price = product_price.text

                item = {"name": name, "image": image, "price": price}
                result.append(item)

            return result

        else:
            return None
