from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from os import path
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def file_data(path, extension):
        if extension == '.csv':
            return CsvImporter.import_data(path)
        if extension == '.json':
            return JsonImporter.import_data(path)
        if extension == '.xml':
            return XmlImporter.import_data(path)

    @staticmethod
    def import_data(file, type):
        extension = path.splitext(file)[1]
        inventories = Inventory.file_data(file, extension)
        if type == 'simples':
            report = SimpleReport.generate(inventories)
            return report
        elif type == 'completo':
            report = CompleteReport.generate(inventories)
            return report
