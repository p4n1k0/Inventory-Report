from inventory_report.inventory.product import Product


def test_cria_produto():
    p = Product(
        1,
        'produto',
        'empresa',
        2023,
        2025,
        12,
        'em qualquer lugar',
    )

    res = (
        'O produto produto fabricado em 2023 por empresa com'
        ' validade até 2025 precisa ser armazenado em qualquer lugar.'
    )
    assert repr(p) == res
