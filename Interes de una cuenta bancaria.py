class CuentaBancaria:
    def __init__(self, saldo: float, tasa_interes_anual: float):
        self.saldo = saldo
        self.tasa_interes_anual = tasa_interes_anual

    def calcular_interes(self, años: int):
        self.saldo *= (1 + self.tasa_interes_anual / 100) ** años

    def mostrar_saldo(self):
        print(f"Saldo después de {años} años: ${self.saldo:.2f}")


if __name__ == "__main__":
    # Ejemplo de uso
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    tasa_interes = float(input("Ingrese la tasa de interés anual (%): "))
    años = int(input("Ingrese el número de años: "))

    cuenta = CuentaBancaria(saldo_inicial, tasa_interes)
    cuenta.calcular_interes(años)
    cuenta.mostrar_saldo()