nombre1 = input("¿Cómo se llamará el jugador1?: ")
nombre2 = input("¿Cómo se llamará el jugador2?: ")

puntaje1 = 0
puntaje2 = 0

while  puntaje1 < 2 and puntaje2 < 2:
    jugador1 = input(f'¡Hola, {nombre1}! ¿Qué elegís? ¿Piedra, papel o tijeras?: ')
    jugador2 = input(f'¡Hola, {nombre2}! ¿Qué elegís? ¿Piedra, papel o tijeras?: ')

    condicion1 = jugador1.lower() == "piedra" and jugador2.lower() == "tijeras"
    condicion2 = jugador1.lower() == "papel" and jugador2.lower() == "piedra"
    condicion3 = jugador1.lower() == "tijeras" and jugador2.lower() == "papel"

    noerror = (jugador1 == "piedra" or jugador1 == "papel" or jugador1 == "tijeras") and (jugador2 == "piedra" or jugador2 == "papel" or jugador2 == "tijeras")
    
    if noerror is False:
        print('Palabra incorrecta! Ingresar solo "Piedra", "Papel" o "Tijeras"')
    else:
        if jugador1.lower() == jugador2.lower():
            print("ha sido un empate!")
        elif condicion1 or condicion2 or condicion3:
            print(f'ha ganado {nombre1}!')
            puntaje1 += 1
        else:
            print(f'ha ganado {nombre2}!')
            puntaje2 += 1
    
    print(f"Puntaje: {nombre1} {puntaje1} - {nombre2} {puntaje2}\n")

if puntaje1 == 2:
    print(f"🎉 ¡{nombre1} es el campeón del mejor de 3! 🎉")
else:
    print(f"🎉 ¡{nombre2} es el campeón del mejor de 3! 🎉")
