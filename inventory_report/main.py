import sys

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Verifique os argumentos\n")
    else:
        path = sys.argv[1]
        report_type = sys.argv[2]

        inventory = InventoryRefactor(file_reader(path))
        sys.stdout.write(inventory.import_data(path, report_type))        


def file_reader(path):
    if path.endswith(".csv"):
        return CsvImporter
    elif path.endswith(".json"):
        return JsonImporter
    elif path.endswith(".xml"):
        return XmlImporter
