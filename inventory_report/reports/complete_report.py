from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def products_company(companies):
        reports = {}
        for company in companies:
            try:
                reports[company['nome_da_empresa']] += 1
            except Exception:
                reports[company['nome_da_empresa']] = 1
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
