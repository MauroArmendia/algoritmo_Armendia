def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n - 1)

def Suma_Lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + Suma_Lista(lista[1:])

facto = int(input("Ingresa un número para saber su factorial: "))
lista_sumar = [1, 2, 3, 4]

print(f"Factorial de {facto}:, {Factorial(facto)}")
print(f"Suma de {lista_sumar}:, {Suma_Lista(lista_sumar)}\n")


class Medicamento:
    def __init__(self, nombre, categoria, stock, precio, codigo_barras):
        self.nombre = nombre
        self.categoria = categoria
        self.stock = stock
        self.precio = precio
        self.codigo_barras = codigo_barras

    def vender(self, cantidad):
        if cantidad > self.stock:
            print(f"No hay suficiente stock para vender {cantidad} unidades de {self.nombre}.")
        else:
            self.stock -= cantidad
            print(f"Se vendieron {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}")

    def reponer_stock(self, cantidad):
        self.stock += cantidad
        print(f"Se repusieron {cantidad} unidades. El Stock actual: {self.stock}\n")

    def esta_en_stock_critico(self):
        return self.stock < 10

paracetamol = Medicamento("Paracetamol", "Analgesico", 12, 2.5, "123456789")
paracetamol.vender(5)
paracetamol.reponer_stock(5)

if paracetamol.esta_en_stock_critico() == False:
    print(f"El stock no es crítico. Stock restante: {paracetamol.stock}")
else:
    print(f"El stock es crítico. Stock restante: {paracetamol.stock}")



