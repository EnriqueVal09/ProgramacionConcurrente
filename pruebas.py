import threading
import time
import sys

# Lista de elementos a mostrar
elementos = ['Elemento 1', 'Elemento 2', 'Elemento 3', 'Elemento 4', 'Elemento 5']

# Variable para controlar la ejecución
mostrar = True

# Evento para sincronizar la impresión del mensaje antes de comenzar a mostrar los elementos
inicio_mostrar = threading.Event()

# Función que muestra los elementos de la lista en bucle en una sola línea
def mostrar_elementos():
    i = 0
    inicio_mostrar.wait()  # Espera a que el mensaje se muestre antes de empezar
    while mostrar:
        # Imprime el elemento en la misma línea y limpia el buffer de salida
        sys.stdout.write(f'\r{elementos[i % len(elementos)]}   ')
        sys.stdout.flush()
        i += 1
        time.sleep(1)  # Espera un segundo antes de mostrar el siguiente elemento

# Función para esperar a que el usuario presione Enter
def esperar_enter():
    print("\nPresiona Enter para detener...\n")  # Imprime el mensaje primero
    inicio_mostrar.set()  # Señala al otro hilo que puede comenzar
    input()  # Espera a que el usuario presione Enter
    global mostrar
    mostrar = False  # Cambia la variable para detener el otro hilo

# Crear los hilos
hilo_mostrar = threading.Thread(target=mostrar_elementos)
hilo_esperar = threading.Thread(target=esperar_enter)

hilo_esperar.start()
hilo_mostrar.start()

# Esperar a que ambos hilos terminen
hilo_esperar.join()
hilo_mostrar.join()

print("\nEjecución detenida.")

