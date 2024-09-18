import threading
import time

 #  Programa de hilos con parametros

def Hilo_02(nombre, apellido): # función con parametros
    print("Hilos con argumentos en Python " + nombre + apellido)
    time.sleep(9)  # Se espera 9 segundos antes de seguir

if __name__ =='__main__':
    # Utilizamos el parametro args y colocamos los argumentos mediante una tupla
    thread = threading.Thread(target=Hilo_02, args=("Juan ", "Hernandez "))
    thread.start()  # Se crea un nuevo hilo
    thread.join()  # Le dice al thread principal que se detenga hasta que el thread nuevo termine

    print("Hilos con Python desde el hilo principal")