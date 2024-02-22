# main.py
def sumar(a, b):
    return a + b

if __name__ == "__main__":
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))
    resultado = sumar(numero1, numero2)
    print(f"El resultado de la suma es: {resultado}")