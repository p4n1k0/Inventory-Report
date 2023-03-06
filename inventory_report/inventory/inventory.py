from abc import ABC, abstractstaticmethod
from csv import reader
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from os import path
from json import load


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
        inventories = []
        for product in rows:
            cache = {}
            for index in range(0, len(product)):
                cache[header[index]] = product[index]
            inventories.append(cache)
        return inventories


class JSON(FileRead):
    def read(path):
        with open(path, 'r') as file:
            inventories = load(file)
            return inventories


class Inventory:
    @staticmethod
    def import_data(inventory, type):
        x, *extension = path.splitext(inventory)[1]
        inventories = eval(''.join(extension).upper() + '.read(inventory)')
        if type == 'simples':
            report = SimpleReport.generate(inventories)
            return report
        elif type == 'completo':
            report = CompleteReport.generate(inventories)
            return report
