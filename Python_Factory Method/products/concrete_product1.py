from products.product import Product

class ConcreteProduct1(Product):
    """Clase concreta que implementa el producto 1."""

    def operation(self) -> str:
        return "Resultado del ConcreteProduct1"
