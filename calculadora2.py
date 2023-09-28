# Función para sumar dos números
def suma(num1, num2):
    return num1 + num2

# Función para restar dos números
def resta(num1, num2):
    return num1 - num2

# Función para multiplicar dos números
def multiplicacion(num1, num2):
    return num1 * num2

# Función para dividir dos números
def division(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir entre cero."
    return num1 / num2

# Función principal
def calculadora():
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    # Solicitar al usuario que elija una operación
    opcion = input("Ingrese el número de la operación deseada: ")

    # Solicitar al usuario que ingrese dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print("Resultado:", suma(num1, num2))
    elif opcion == '2':
        print("Resultado:", resta(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == '4':
        print("Resultado:", division(num1, num2))
    else:
        print("Opción no válida")

# Llamar a la función principal de la calculadora
calculadora()
