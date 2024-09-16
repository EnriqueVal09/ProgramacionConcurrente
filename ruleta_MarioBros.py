import time
import threading
import random
import sys, io

ELEMENTOS = ["⭐", "🍄", "🌼"]
PUNTAJES = [5, 3, 2]

tiros = 3
girar = True

def main():
    mostrar_puntajes(ELEMENTOS, PUNTAJES)
    inicio = threading.Event()
    hilo_girar = threading.Thread(target=girar_ruleta, daemon=False, args=(ELEMENTOS, inicio))
    hilo_tirar = threading.Thread(target=tirar, daemon=False, args=(inicio, ))
    hilo_girar.start()
    hilo_tirar.start()
    while True:
        if iniciar_juego():
            inicio.set()

            hilo_girar.join()
            hilo_tirar.join()
        else:
            break
        
        tiros = 3
        girar = True
        inicio.clear()


def girar_ruleta(elementos, inicio):
    while girar:
        inicio.wait()
        elemento = random.choice(elementos)
        sys.stdout.write(f'\r{elemento}')
        sys.stdout.flush()
        time.sleep(1)

def tirar(inicio):
    global tiros

    while tiros > 0:
        inicio.wait()
        input("Presiona ENTER")
        tiros -= 1
    global girar
    girar = False

def detener_ruleta(): 
    pass

def mostrar_puntajes(elementos, puntajes):
    for i in range(len(elementos)):
        print(f"{elementos[i]} = {puntajes[i]} pts")

def iniciar_juego():
    inicio = input("Deseas inciar la ruleta (s/n)...")
    if inicio == "s": return True
    else: return False

if __name__ == "__main__":
    main()