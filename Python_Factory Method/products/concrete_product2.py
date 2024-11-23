from products.product import Product

class ConcreteProduct2(Product):
    """Clase concreta que implementa el producto 2."""

    def operation(self) -> str:
        return "Resultado del ConcreteProduct2"
