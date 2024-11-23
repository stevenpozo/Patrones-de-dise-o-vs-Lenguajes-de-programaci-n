from creators.concrete_creator1 import ConcreteCreator1
from creators.concrete_creator2 import ConcreteCreator2
from creators.creator import Creator

def client_code(creator: Creator):
    """Función cliente que trabaja con cualquier creador."""
    print(f"{creator.some_operation()}")

if __name__ == "__main__":
    print("App: Usando ConcreteCreator1.")
    client_code(ConcreteCreator1())

    print("\nApp: Usando ConcreteCreator2.")
    client_code(ConcreteCreator2())
