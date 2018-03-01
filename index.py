# Libraries for web scraping
from price_scraper import PriceScraper
from cleaner import Cleaner
from writer import Writer

input = input("Are you ready to scrape (yes/no): ")

if input == "yes":
    scraper = PriceScraper()
    data = scraper.scrape()

    cleaner = Cleaner()
    clean_data = cleaner.cleanArray(data)

    writer = Writer("output/data.csv")
    writer.write(clean_data)

    print("Job completed!")
else:
    print("Oki, no worries")
