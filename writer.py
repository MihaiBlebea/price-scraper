from cleaner import Cleaner
import csv

class Writer:
    file = None

    def __init__(self, file):
        self.file = file

    def write(self, payload):
        for product in payload:
            with open(self.file, "a") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([ product["name"], product["price"] ])
