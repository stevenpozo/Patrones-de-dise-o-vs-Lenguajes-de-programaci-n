from abc import ABC, abstractmethod

class Product(ABC):
    """Clase base abstracta para todos los productos."""

    @abstractmethod
    def operation(self) -> str:
        """Método que todas las clases concretas deben implementar."""
        pass
