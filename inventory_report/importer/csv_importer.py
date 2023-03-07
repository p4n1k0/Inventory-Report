from inventory_report.importer.importer import Importer
from os.path import splitext
from csv import reader


class CsvImporter(Importer):
    def import_data(path):
        exension = splitext(path)[1]
        if exension != '.csv':
            raise ValueError('Arquivo inválido')
        header = []
        rows = []
        with open(path, 'r') as file:
            header, *rows = reader(file)
        inventories = []
        for product in rows:
            data = {}
            for index in range(0, len(product)):
                data[header[index]] = product[index]
            inventories.append(data)
        return inventories
