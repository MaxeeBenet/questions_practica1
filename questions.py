import random
import string

words = {
    1 : {"nombre" : "programacion", 
         "palabras" : ["python","programa","variable","funcion","bucle","cadena","entero","lista",]
         },
    2 : {"nombre" : "animales", 
         "palabras" : ["elefante", "perro", "jirafa", "cocodrilo", "ballena", "delfin", "coyote", "hipopotamo"]
         },
    3 : {"nombre" : "marcas", 
         "palabras" : ["samsung", "toshiba", "ferrari", "mercedesbenz", "apple", "siam", "parsecs", "pizzini"]
         },
    4 : {"nombre" : "nombres", 
         "palabras" : ["constanza", "pedro", "axel", "cristina", "nestor", "juandomingo", "eva", "david"]
         }
    }

score = 0

print("¡Bienvenido al ahorcado!")
print()
print("Selecciona la categoria para empezar a jugar (Ingrese el numero): ")
print()

for key in words:
    print(key, words[key]["nombre"], end=". ")   
    
selection = int(input(": "))
print()

while selection not in words and selection != 0:
    print("Seleccione la categoria correcta o ingrese 0 para salir.")
    selection = int(input(": "))

if selection == 0:
    print("Saliste del juego.")
else:
    print(f"Seleccionaste la categoria: {words[selection]["nombre"]}")
    print()
    
    rounds = int(input('Ingrese la cantidad de rondas que desea jugar (entre 1 y 8): '))
    while rounds <= 1 or rounds >= 8:
        rounds = int(input('Por favor, ingrese un numero entre 1 y 8: '))

    print()
    new_words = random.sample(words[selection]["palabras"], rounds)
    
    for word in new_words:
        
        guessed = []
        attempts = 6
        score_round = 0
        
        while attempts > 0:
            # Mostrar progreso: letras adivinadas y guiones para las palabras que faltan
            progress = ""
            for letter in word:
                if letter in guessed:
                    progress += letter + " "
                else:
                    progress += "_ "
            print(progress)
                # Verificar si el jugador ya adivino la palabra completa
            if "_" not in progress:
                print("Ganaste!")
                score_round += 6
                print(f"Tu puntuacion es {score_round} en esta ronda.")
                break
                
            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")
                
            letter = input("Ingresa una letra: ").lower()
            
            
            if len(letter) > 1 or letter not in string.ascii_lowercase: 
                print("Entrada no valida")
                continue
                
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra esta en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                score_round -= 1
                print("Esa letra no esta en la palabra")
                
                
        else:
            score_round = 0
            print(f"¡Perdiste! la palabra era: {word}, tu puntaje es {score_round} en esta ronda.")
        score += score_round
    print()
    
    print(f"Tu puntuacion total es de {score}")
