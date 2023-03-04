from datetime import date, timedelta
from collections import Counter


class SimpleReport:
    @staticmethod
    def get_dates(products):
        fabrication_date = products[0]['data_de_fabricacao']
        expiration_date = str(date.today() + timedelta(days=366))
        for product in products:
            fabrication = product['data_de_fabricacao']
            expiration = product['data_de_validade']
            if fabrication < fabrication_date:
                fabrication_date = fabrication
            if expiration > str(date.today()) and expiration < expiration_date:
                expiration_date = expiration
        return (fabrication_date, expiration_date)

    @staticmethod
    def get_company(companies):
        products = Counter(
            company['nome_da_empresa'] for company in companies
            )
        return products.most_common()[0][0]

    @staticmethod
    def generate(product):
        dates = SimpleReport.get_dates(product)
        fabrication_date = dates[0]
        expiration_date = dates[1]
        company = SimpleReport.get_company(product)
        return (
            f'Data de fabricação mais antiga: {fabrication_date}\n' +
            f'Data de validade mais próxima: {expiration_date}\n' +
            f'Empresa com mais produtos: {company}'
        )
