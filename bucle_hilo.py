import time

def print_even_numbers():
    for number in range(2, 201, 2):  # Comienza en 2 y avanza de 2 en 2 hasta 200
        print(f"Número par: {number}")
        time.sleep(0.5)  # Espera 0.5 segundos

def print_odd_numbers():
    for number in range(1, 200, 2):  # Comienza en 1 y avanza de 2 en 2 hasta 199
        print(f"Número impar: {number}")
        time.sleep(0.5)  # Espera 0.5 segundos

# Ejecutar ambas funciones secuencialmente
print_even_numbers()
print_odd_numbers()