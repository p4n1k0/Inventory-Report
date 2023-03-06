from abc import ABC, abstractstaticmethod
from csv import reader
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from os import path
from json import load
from xml.etree import ElementTree


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


class XML(FileRead):
    def read(path):
        xml_file = ElementTree.parse(path)
        admin = xml_file.getroot()
        products = []
        for reading in admin:
            reports = {}
            for file in reading:
                reports[file.tag] = file.text
            products.append(reports)
        return products


class Inventory:
    @staticmethod
    def import_data(file, type):
        x, *extension = path.splitext(file)[1]
        inventories = eval(''.join(extension).upper() + '.read(file)')
        if type == 'simples':
            report = SimpleReport.generate(inventories)
            return report
        elif type == 'completo':
            report = CompleteReport.generate(inventories)
            return report
