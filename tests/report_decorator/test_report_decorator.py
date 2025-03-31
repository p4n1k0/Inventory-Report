from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    mock_products = [
        {
            "id": 1,
            "nome_do_produto": "CADEIRA",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-04-04",
            "data_de_validade": "2025-08-19",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco"
        }
    ]

    report_type = ColoredReport(SimpleReport)
    report = report_type.generate(mock_products)

    frase_verde1 = "\033[32mData de fabricação mais antiga:\033[0m"
    frase_verde2 = "\033[32mData de validade mais próxima:\033[0m"
    frase_verde3 = "\033[32mEmpresa com mais produtos:\033[0m"

    data_azul1 = "\033[36m2022-04-04\033[0m"
    data_azul2 = "\033[36m2025-08-19\033[0m"

    empresa = "\033[31mForces of Nature\033[0m"

    assert frase_verde1 in report
    assert frase_verde2 in report
    assert frase_verde3 in report
    assert data_azul1 in report
    assert data_azul2 in report
    assert empresa in report
