from models.product import Product


def select_products_by_category(products: list[Product], category: str) -> list[Product]:
    good_products = []
    for prod in products:
        if prod.category == category:
            good_products.append(prod)
    return good_products
