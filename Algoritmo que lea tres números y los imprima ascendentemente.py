class OrdenadorNumeros:
    def __init__(self, numero1: int, numero2: int, numero3: int):
        self.numeros = [numero1, numero2, numero3]

    def ordenar(self):
        self.numeros.sort()

    def mostrar_numeros(self):
        print("Números ordenados:", self.numeros)


if __name__ == "__main__":
    # Ejemplo de uso
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    numero3 = int(input("Ingrese el tercer número: "))

    ordenador = OrdenadorNumeros(numero1, numero2, numero3)
    ordenador.ordenar()
    ordenador.mostrar_numeros()
