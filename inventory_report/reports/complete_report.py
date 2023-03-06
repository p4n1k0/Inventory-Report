from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def products_company(companies_list):
        reports = {}
        num = 1
        for company in companies_list:
            try:
                reports[company['nome_da_empresa']] += num
            except Exception:
                reports[company['nome_da_empresa']] = num
        string = ''
        for company in reports:
            string += f'- {company}: {reports[company]}\n'
        return string

    @staticmethod
    def generate(reports):
        dates = CompleteReport._get_dates(reports)
        fabrication_date = dates[0]
        expiration_date = dates[1]
        company = CompleteReport._get_company(reports)
        products = CompleteReport.products_company(reports)
        return (
            f'Data de fabricação mais antiga: {fabrication_date}\n' +
            f'Data de validade mais próxima: {expiration_date}\n' +
            f'Empresa com mais produtos: {company}\n'
            + 'Produtos estocados por empresa:\n'
            + products
        )
