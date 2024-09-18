import threading
import time

def tarea(numero):
    inicio = time.time()
    print(f"Realizando la tarea {numero}...")
    time.sleep(5)
    duracion = time.time() - inicio
    print(f"Tarea finalizada con duracion de: {duracion:.2f}")

hilo1 = threading.Thread(target=tarea, args=(1,))
hilo2 = threading.Thread(target=tarea, args=(2,))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print("Todos los hilos han terminado")