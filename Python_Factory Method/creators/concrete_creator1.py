from creators.creator import Creator
from products.concrete_product1 import ConcreteProduct1
from products.product import Product

class ConcreteCreator1(Creator):
    """Creador concreto que produce ConcreteProduct1."""

    def factory_method(self) -> Product:
        return ConcreteProduct1()
