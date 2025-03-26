import random

print(""""
 ___       __   ________  ________        ___       __   ________  ________  ________  ___       ___  ________  _________       
|\  \     |\  \|\   __  \|\   __  \      |\  \     |\  \|\   __  \|\   __  \|\   ___ \|\  \     |\  \|\   ____\|\___   ___\     
\ \  \    \ \  \ \  \|\  \ \  \|\  \     \ \  \    \ \  \ \  \|\  \ \  \|\  \ \  \_|\ \ \  \    \ \  \ \  \___|\|___ \  \_|     
 \ \  \  __\ \  \ \   ____\ \   ____\     \ \  \  __\ \  \ \  \\\  \ \   _  _\ \  \ \\ \ \  \    \ \  \ \_____  \   \ \  \      
  \ \  \|\__\_\  \ \  \___|\ \  \___|      \ \  \|\__\_\  \ \  \\\  \ \  \\  \\ \  \_\\ \ \  \____\ \  \|____|\  \   \ \  \     
   \ \____________\ \__\    \ \__\          \ \____________\ \_______\ \__\\ _\\ \_______\ \_______\ \__\____\_\  \   \ \__\    
    \|____________|\|__|     \|__|           \|____________|\|_______|\|__|\|__|\|_______|\|_______|\|__|\_________\   \|__|  by alesmaco-666
                                                                                                        \|_________|            
                                                                                                                                
"""                                                                                                                  
)
idioma = str(input("Language/lenguaje (español/english): "))

if idioma == "español":

    longitud = int(input("cuantas contraseñas quieres en la wordlist: "))
    nombre = str(input("Nombre de la wordlist: "))

    numeroAleatorio = str(input("Numeros aleatorio si/no: "))
    Name1delavictima = str(input("Primer Nombre de la victima: "))
    Name2delavictima = str(input("Segundo Nombre de la victima:"))
    apellido1 = str(input("Primer Apellido de la victima: "))
    apellido2 = str(input("Segundo Apellido de la victima: "))
    Dia = str(input("Dia de nacimiento de la victima (DD): "))
    Mes = str(input("Mes de nacimiento de la victima (MM): "))
    Año = str(input("Año de nacimiento de la victima (YYYY): "))
    contraseñas = []

    for _ in range(longitud):
        if numeroAleatorio == "si":
            opciones = [
                [Name1delavictima, Dia],
                [Name1delavictima, Name2delavictima, apellido1],
                [Name2delavictima, apellido1, Dia],
                [Name2delavictima, apellido1],
                [Name1delavictima, apellido1],
                [Name1delavictima, Name2delavictima, apellido2],
                [Name2delavictima, apellido2, Dia],
                [Name2delavictima, apellido2],
                [Name1delavictima, apellido2],
                [Name2delavictima, Dia],
                [Name1delavictima, Mes],
                [Name2delavictima, apellido1, Mes],
                [Name2delavictima, apellido2, Mes],
                [Name1delavictima, Año],
                [Name2delavictima, apellido1, Año],
                [Name2delavictima, apellido2, Año],
                [Name1delavictima, Dia, Mes],
                [Name2delavictima, apellido1, Dia, Mes],
                [Name2delavictima, apellido2, Dia, Mes],
                [Name1delavictima, Dia, Mes, Año],
                [Name2delavictima, apellido1, Dia, Mes, Año],
                [Name2delavictima, apellido2, Dia, Mes, Año],
                [Name1delavictima, Name2delavictima, apellido1, apellido2, str(random.randint(0, 100))],
            ]

        elif numeroAleatorio == "no":
        
            opciones = [
                [Name1delavictima, Dia],
                [Name1delavictima, Name2delavictima, apellido1],
                [Name2delavictima, apellido1, Dia],
                [Name2delavictima, apellido1],
                [Name1delavictima, apellido1],
                [Name1delavictima, Name2delavictima, apellido2],
                [Name2delavictima, apellido2, Dia],
                [Name2delavictima, apellido2],
                [Name1delavictima, apellido2],
                [Name2delavictima, Dia],
                [Name1delavictima, Mes],
                [Name2delavictima, apellido1, Mes],
                [Name2delavictima, apellido2, Mes],
                [Name1delavictima, Año],
                [Name2delavictima, apellido1, Año],
                [Name2delavictima, apellido2, Año],
                [Name1delavictima, Dia, Mes],
                [Name2delavictima, apellido1, Dia, Mes],
                [Name2delavictima, apellido2, Dia, Mes],
                [Name1delavictima, Dia, Mes, Año],
                [Name2delavictima, apellido1, Dia, Mes, Año],
                [Name2delavictima, apellido2, Dia, Mes, Año],
            ]

        else:

            print("Error: opción invalida")
            break

        partes = random.choice(opciones)
        random.shuffle(partes)
        contraseña = "".join(partes)
        contraseñas.append(contraseña)

    with open(f"wordlist_{nombre}.txt", "w") as archivo:
        archivo.write("\n".join(contraseñas))

    print(f"Wordlist guardada como wordlist_{nombre}.txt")

elif idioma == "english":
 
 longitud = int(input("How many passwords do you want in the wordlist: "))
 nombre = str(input("Name of the wordlist: "))

 numeroAleatorio = str(input("Random numbers? (yes/no): "))
 Name1delavictima = str(input("Victim's first name: "))
 Name2delavictima = str(input("Victim's middle name: "))
 apellido1 = str(input("Victim's first surname: "))
 apellido2 = str(input("Victim's second surname"))
 Dia = str(input("Victim's Birth Day (DD): "))
 Mes = str(input("Victim's Birth Month (MM): "))
 Año =  str(input("Year of Birth of the victim (YYYY): "))
 contraseñas = []

 for _ in range(longitud):
    if numeroAleatorio == "yes":
        opciones = [ 
                [Name1delavictima, Dia],
                [Name1delavictima, Name2delavictima, apellido1],
                [Name2delavictima, apellido1, Dia],
                [Name2delavictima, apellido1],
                [Name1delavictima, apellido1],
                [Name1delavictima, Name2delavictima, apellido2],
                [Name2delavictima, apellido2, Dia],
                [Name2delavictima, apellido2],
                [Name1delavictima, apellido2],
                [Name2delavictima, Dia],
                [Name1delavictima, Mes],
                [Name2delavictima, apellido1, Mes],
                [Name2delavictima, apellido2, Mes],
                [Name1delavictima, Año],
                [Name2delavictima, apellido1, Año],
                [Name2delavictima, apellido2, Año],
                [Name1delavictima, Dia, Mes],
                [Name2delavictima, apellido1, Dia, Mes],
                [Name2delavictima, apellido2, Dia, Mes],
                [Name1delavictima, Dia, Mes, Año],
                [Name2delavictima, apellido1, Dia, Mes, Año],
                [Name2delavictima, apellido2, Dia, Mes, Año],
                [Name1delavictima, Name2delavictima, apellido1, apellido2, str(random.randint(0, 100))],
                ]
    elif numeroAleatorio == "no":
        opciones = [
                [Name1delavictima, Dia],
                [Name1delavictima, Name2delavictima, apellido1],
                [Name2delavictima, apellido1, Dia],
                [Name2delavictima, apellido1],
                [Name1delavictima, apellido1],
                [Name1delavictima, Name2delavictima, apellido2],
                [Name2delavictima, apellido2, Dia],
                [Name2delavictima, apellido2],
                [Name1delavictima, apellido2],
                [Name2delavictima, Dia],
                [Name1delavictima, Mes],
                [Name2delavictima, apellido1, Mes],
                [Name2delavictima, apellido2, Mes],
                [Name1delavictima, Año],
                [Name2delavictima, apellido1, Año],
                [Name2delavictima, apellido2, Año],
                [Name1delavictima, Dia, Mes],
                [Name2delavictima, apellido1, Dia, Mes],
                [Name2delavictima, apellido2, Dia, Mes],
                [Name1delavictima, Dia, Mes, Año],
                [Name2delavictima, apellido1, Dia, Mes, Año],
                [Name2delavictima, apellido2, Dia, Mes, Año],
                ]
    else:

        print("Error: invalid option for random numbers.")
        break
    
    partes = random.choice(opciones)
    random.shuffle(partes)
    contraseña = "".join(partes)
    contraseñas.append(contraseña)

 with open(f"wordlist_{nombre}.txt", "w") as archivo:
    archivo.write("\n".join(contraseñas))

 print(f"Wordlist saved as wordlist_{nombre}.txt")

else:
    print("Error: invalid option for language. / Error: opción invalida para idioma.")