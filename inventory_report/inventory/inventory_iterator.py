from collections.abc import Iterator


class InventoryIterator(Iterator):

    def __init__(self, products):
        self.products = products
        self.index = 0

    def __next__(self):
        product = self.products[self.index]
        if not product:
            raise StopIteration()
        self.index += 1
        return product
