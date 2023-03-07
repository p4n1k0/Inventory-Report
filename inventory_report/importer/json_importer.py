from inventory_report.importer.importer import Importer
from os.path import splitext
from json import load


class JsonImporter(Importer):
    def import_data(path):
        extension = splitext(path)[1]
        if extension != '.json':
            raise ValueError('Arquivo inválido')
        with open(path, 'r') as file:
            inventories = load(file)
            return inventories
