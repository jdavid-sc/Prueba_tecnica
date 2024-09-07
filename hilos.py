import threading
import time

def print_even_numbers():
    for number in range(2, 201, 2):
        print(f"Número par: {number}")
        time.sleep(0.5)

def print_odd_numbers():
    for number in range(1, 200, 2):
        print(f"Número impar: {number}")
        time.sleep(0.5)

# Crear los hilos
even_thread = threading.Thread(target=print_even_numbers)
odd_thread = threading.Thread(target=print_odd_numbers)

# Iniciar los hilos
even_thread.start()
odd_thread.start()

# Esperar a que ambos hilos terminen
even_thread.join()
odd_thread.join()
