from inventory_report.importer.importer import Importer
from os.path import splitext
from xml.etree import ElementTree


class XmlImporter(Importer):
    def import_data(path):
        extension = splitext(path)[1]
        if extension != '.xml':
            raise ValueError('Arquivo inválido')
        xml = ElementTree.parse(path)
        admin = xml.getroot()
        products = []
        for reading in admin:
            data = {}
            for file in reading:
                data[file.tag] = file.text
            products.append(data)
        return products
