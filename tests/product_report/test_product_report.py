from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        1,
        'café',
        'Minas Cafés',
        '2023-01-01',
        '2023-12-12',
        'cafe123',
        'em local fresco'
    )

    assert produto.__repr__() == (
        "O produto café"
        " fabricado em 2023-01-01"
        " por Minas Cafés com validade"
        " até 2023-12-12"
        " precisa ser armazenado em local fresco."
        )
