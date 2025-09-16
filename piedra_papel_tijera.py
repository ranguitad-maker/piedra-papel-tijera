import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    usuario = input("Elige piedra, papel o tijera: ").lower()
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    if usuario == computadora:
        print("¡Empate!")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    elif usuario in opciones:
        print("¡Perdiste!")
    else:
        print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    jugar()