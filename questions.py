import random
import string

words = [
"python",
"programa",
"variable",
"funcion",
"bucle",
"cadena",
"entero",
"lista",
]

word = random.choice(words)
guessed = []
attempts = 6

print("¡Bienvenido al ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las palabras que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
        # Veriicar si el jugador ya adivinola palabra completa
    if "_" not in progress:
        print("Ganaste!")

        break
        
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
        
    letter = input("Ingresa una letra: ")
    
    if len(letter) > 1 or letter.lower() not in string.ascii_lowercase: 
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

        print("Esa letra no esta en la palabra")
        
        
else:
    print(f"¡Perdiste! la palabra era: {word}")