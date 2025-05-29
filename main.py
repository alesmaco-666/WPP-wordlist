import random

print("""
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
    Name1delpadre = str(input("Primer Nombre del padre de la victima: "))
    Name2delpadre = str(input("Segundo Nombre del padre de la victima: "))
    Name1delamadre = str(input("Primer Nombre de la madre de la victima: "))
    Name2delamadre = str(input("Segundo Nombre de la madre de la victima: "))
    Name1delhermano = str(input("Primer Nombre del hermano de la victima: "))
    Name2delhermano = str(input("Segundo Nombre del hermano de la victima: "))
    Name1delahermana = str(input("Primer Nombre de la hermana de la victima: "))
    Name2delahermana = str(input("Segundo Nombre de la hermana de la victima: "))
    Namedelamascota = str(input("Nombre de la mascota de la victima: "))
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
                # Familiares y mascota
                [Name1delavictima, Name1delpadre, apellido1],
                [Name1delavictima, Name1delamadre, apellido2],
                [Name1delavictima, Name1delhermano, Dia],
                [Name1delavictima, Name1delahermana, Mes],
                [Name1delavictima, Namedelamascota, Año],
                [Name1delpadre, apellido1, Dia],
                [Name2delpadre, apellido2, Mes],
                [Name1delamadre, apellido1, Año],
                [Name2delamadre, apellido2, Dia],
                [Name1delhermano, apellido1, Mes],
                [Name2delhermano, apellido2, Año],
                [Name1delahermana, apellido1, Dia],
                [Name2delahermana, apellido2, Mes],
                [Namedelamascota, apellido1, Año],
                [Name1delavictima, Name1delpadre, Name1delamadre, Dia, Mes],
                [Name1delavictima, Name1delhermano, Name1delahermana, Año],
                [Name1delavictima, Namedelamascota, Dia, Mes, Año],
                [Name1delavictima, Name1delpadre, Name1delamadre, Name1delhermano, Name1delahermana, Namedelamascota, apellido1, apellido2, Dia, Mes, Año, str(random.randint(0, 100))]
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
                # Familiares y mascota
                [Name1delavictima, Name1delpadre, apellido1],
                [Name1delavictima, Name1delamadre, apellido2],
                [Name1delavictima, Name1delhermano, Dia],
                [Name1delavictima, Name1delahermana, Mes],
                [Name1delavictima, Namedelamascota, Año],
                [Name1delpadre, apellido1, Dia],
                [Name2delpadre, apellido2, Mes],
                [Name1delamadre, apellido1, Año],
                [Name2delamadre, apellido2, Dia],
                [Name1delhermano, apellido1, Mes],
                [Name2delhermano, apellido2, Año],
                [Name1delahermana, apellido1, Dia],
                [Name2delahermana, apellido2, Mes],
                [Namedelamascota, apellido1, Año],
                [Name1delavictima, Name1delpadre, Name1delamadre, Dia, Mes],
                [Name1delavictima, Name1delhermano, Name1delahermana, Año],
                [Name1delavictima, Namedelamascota, Dia, Mes, Año],
                [Name1delavictima, Name1delpadre, Name1delamadre, Name1delhermano, Name1delahermana, Namedelamascota, apellido1, apellido2, Dia, Mes, Año]
            ]
        else:
            print("Error: opción invalida")
            break

        partes = random.choice(opciones)
        random.shuffle(partes)
        contraseña = "".join(partes)
        # Aleatoriamente minúsculas o mayúsculas
        if random.choice([True, False]):
            contraseña = contraseña.lower()
        else:
            contraseña = contraseña.upper()
        contraseñas.append(contraseña)

    with open(f"wordlist_{nombre}.txt", "w") as archivo:
        archivo.write("\n".join(contraseñas))

    print(f"Wordlist guardada como wordlist_{nombre}.txt")

elif idioma == "english":
    length = int(input("How many passwords do you want in the wordlist: "))
    name = str(input("Name of the wordlist: "))

    randomNumbers = str(input("Random numbers? (yes/no): "))
    VictimFirstName = str(input("Victim's first name: "))
    VictimMiddleName = str(input("Victim's middle name: "))
    Surname1 = str(input("Victim's first surname: "))
    Surname2 = str(input("Victim's second surname: "))
    Day = str(input("Victim's Birth Day (DD): "))
    Month = str(input("Victim's Birth Month (MM): "))
    Year = str(input("Victim's Birth Year (YYYY): "))
    FatherFirstName = str(input("Victim's father's first name: "))
    FatherSecondName = str(input("Victim's father's second name: "))
    MotherFirstName = str(input("Victim's mother's first name: "))
    MotherSecondName = str(input("Victim's mother's second name: "))
    BrotherFirstName = str(input("Victim's brother's first name: "))
    BrotherSecondName = str(input("Victim's brother's second name: "))
    SisterFirstName = str(input("Victim's sister's first name: "))
    SisterSecondName = str(input("Victim's sister's second name: "))
    PetName = str(input("Victim's pet's name: "))
    passwords = []

    for _ in range(length):
        if randomNumbers == "yes":
            options = [
                [VictimFirstName, Day],
                [VictimFirstName, VictimMiddleName, Surname1],
                [VictimMiddleName, Surname1, Day],
                [VictimMiddleName, Surname1],
                [VictimFirstName, Surname1],
                [VictimFirstName, VictimMiddleName, Surname2],
                [VictimMiddleName, Surname2, Day],
                [VictimMiddleName, Surname2],
                [VictimFirstName, Surname2],
                [VictimMiddleName, Day],
                [VictimFirstName, Month],
                [VictimMiddleName, Surname1, Month],
                [VictimMiddleName, Surname2, Month],
                [VictimFirstName, Year],
                [VictimMiddleName, Surname1, Year],
                [VictimMiddleName, Surname2, Year],
                [VictimFirstName, Day, Month],
                [VictimMiddleName, Surname1, Day, Month],
                [VictimMiddleName, Surname2, Day, Month],
                [VictimFirstName, Day, Month, Year],
                [VictimMiddleName, Surname1, Day, Month, Year],
                [VictimMiddleName, Surname2, Day, Month, Year],
                [VictimFirstName, VictimMiddleName, Surname1, Surname2, str(random.randint(0, 100))],
                # Family and pet
                [VictimFirstName, FatherFirstName, Surname1],
                [VictimFirstName, MotherFirstName, Surname2],
                [VictimFirstName, BrotherFirstName, Day],
                [VictimFirstName, SisterFirstName, Month],
                [VictimFirstName, PetName, Year],
                [FatherFirstName, Surname1, Day],
                [FatherSecondName, Surname2, Month],
                [MotherFirstName, Surname1, Year],
                [MotherSecondName, Surname2, Day],
                [BrotherFirstName, Surname1, Month],
                [BrotherSecondName, Surname2, Year],
                [SisterFirstName, Surname1, Day],
                [SisterSecondName, Surname2, Month],
                [PetName, Surname1, Year],
                [VictimFirstName, FatherFirstName, MotherFirstName, Day, Month],
                [VictimFirstName, BrotherFirstName, SisterFirstName, Year],
                [VictimFirstName, PetName, Day, Month, Year],
                [VictimFirstName, FatherFirstName, MotherFirstName, BrotherFirstName, SisterFirstName, PetName, Surname1, Surname2, Day, Month, Year, str(random.randint(0, 100))]
            ]
        elif randomNumbers == "no":
            options = [
                [VictimFirstName, Day],
                [VictimFirstName, VictimMiddleName, Surname1],
                [VictimMiddleName, Surname1, Day],
                [VictimMiddleName, Surname1],
                [VictimFirstName, Surname1],
                [VictimFirstName, VictimMiddleName, Surname2],
                [VictimMiddleName, Surname2, Day],
                [VictimMiddleName, Surname2],
                [VictimFirstName, Surname2],
                [VictimMiddleName, Day],
                [VictimFirstName, Month],
                [VictimMiddleName, Surname1, Month],
                [VictimMiddleName, Surname2, Month],
                [VictimFirstName, Year],
                [VictimMiddleName, Surname1, Year],
                [VictimMiddleName, Surname2, Year],
                [VictimFirstName, Day, Month],
                [VictimMiddleName, Surname1, Day, Month],
                [VictimMiddleName, Surname2, Day, Month],
                [VictimFirstName, Day, Month, Year],
                [VictimMiddleName, Surname1, Day, Month, Year],
                [VictimMiddleName, Surname2, Day, Month, Year],
                # Family and pet
                [VictimFirstName, FatherFirstName, Surname1],
                [VictimFirstName, MotherFirstName, Surname2],
                [VictimFirstName, BrotherFirstName, Day],
                [VictimFirstName, SisterFirstName, Month],
                [VictimFirstName, PetName, Year],
                [FatherFirstName, Surname1, Day],
                [FatherSecondName, Surname2, Month],
                [MotherFirstName, Surname1, Year],
                [MotherSecondName, Surname2, Day],
                [BrotherFirstName, Surname1, Month],
                [BrotherSecondName, Surname2, Year],
                [SisterFirstName, Surname1, Day],
                [SisterSecondName, Surname2, Month],
                [PetName, Surname1, Year],
                [VictimFirstName, FatherFirstName, MotherFirstName, Day, Month],
                [VictimFirstName, BrotherFirstName, SisterFirstName, Year],
                [VictimFirstName, PetName, Day, Month, Year],
                [VictimFirstName, FatherFirstName, MotherFirstName, BrotherFirstName, SisterFirstName, PetName, Surname1, Surname2, Day, Month, Year]
            ]
        else:
            
            print("Error: invalid option for random numbers.")
            break

        parts = random.choice(options)
        random.shuffle(parts)
        password = "".join(parts)

        # Randomly lowercase or uppercase
        
        if random.choice([True, False]):
        
            password = password.lower()
        
        else:
        
            password = password.upper()
        
        passwords.append(password)

    with open(f"wordlist_{name}.txt", "w") as file:
        file.write("\n".join(passwords))

    print(f"Wordlist saved as wordlist_{name}.txt")

else:
    print("Error: invalid option for language. / Error: opción invalida para idioma.")