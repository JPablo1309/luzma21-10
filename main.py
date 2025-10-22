def celsius_a_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    print("Conversor de Temperatura")
    valor = float(input("Ingresa el valor: "))
    tipo = input("¿Convertir a (C/F)? ").upper()

    if tipo == "F":
        print(f"{valor}°C = {celsius_a_fahrenheit(valor):.2f}°F")
    elif tipo == "C":
        print(f"{valor}°F = {fahrenheit_a_celsius(valor):.2f}°C")
    else:
        print("Opción no válida.")
