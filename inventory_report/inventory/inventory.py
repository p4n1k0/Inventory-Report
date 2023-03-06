from abc import ABC, abstractstaticmethod
from csv import reader
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from os import path


class FileRead(ABC):
    @abstractstaticmethod
    def read(path):
        pass


class CSV(FileRead):
    def read(path):
        header = []
        rows = []
        with open(path, 'r') as file:
            header, *rows = reader(file)
        products = []
        for product in rows:
            cache = {}
            for index in range(0, len(product)):
                cache[header[index]] = product[index]
            products.append(cache)
        return products


class Inventory:
    @staticmethod
    def import_data(data_path, type):
        x, *extension = path.splitext(data_path)[1]
        data = eval(''.join(extension).upper() + '.read(data_path)')
        if type == 'simples':
            report = SimpleReport.generate(data)
            return report
        elif type == 'completo':
            report = CompleteReport.generate(data)
            return report
