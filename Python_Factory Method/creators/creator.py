from abc import ABC, abstractmethod
from products.product import Product

class Creator(ABC):
    """Clase base abstracta para los creadores."""

    @abstractmethod
    def factory_method(self) -> Product:
        """Método fábrica que las subclases deben sobrescribir."""
        pass

    def some_operation(self) -> str:
        """Lógica que usa el producto creado por el método fábrica."""
        product = self.factory_method()
        return f"Creator: Trabajando con {product.operation()}"
