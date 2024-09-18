import threading  # Permite crear y manejar hilos en Python

# Primer Programa con Hilos en Python

def Primer_Hilo():
    print("Mi Primer Programa con Hilos en Python")

if __name__ =='__main__': # para que se ejecute el script
    thread = threading.Thread(target=Primer_Hilo)
    # el código que se va ejecutar en segundo plano
    #  se genera un nuevo objeto, donde thread es una clase
    #  y a esta clase, podemos colocar diferentes valores a sus parámetros
    thread.start()  # utilizamos el método start y va ejecuta el targer en segundo plano