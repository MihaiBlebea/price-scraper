
class Cleaner:
    items = {
        "ț":"t","Ț":"T",
        "Ș":"S","ș":"s",
        "ă":"a","Ă":"A",
        "â":"a","Â":"A",
        "î":"i","Î":"I",
        "\u0163":"t",
        "\u015f":"s",
        "\u0103":"a"
    }

    def getType(self, str):
        return type(str)

    def decode(self, str):
        return isinstance(str, basestring)

    def getKeys(self):
        return list(self.items.keys())

    def clean(self, str):
        keys = self.getKeys()
        for key in keys:
            str = str.replace(key, self.items[key]).strip()
        return str

    def cleanArray(self, payload):
        result = []
        for product in payload:
            name = self.clean(product["name"])
            price = self.clean(product["price"])

            item = {"name": name, "price": price}
            result.append(item)

        return result
