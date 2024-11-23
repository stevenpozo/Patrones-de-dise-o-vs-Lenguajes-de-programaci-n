from creators.creator import Creator
from products.concrete_product2 import ConcreteProduct2
from products.product import Product

class ConcreteCreator2(Creator):
    """Creador concreto que produce ConcreteProduct2."""

    def factory_method(self) -> Product:
        return ConcreteProduct2()
