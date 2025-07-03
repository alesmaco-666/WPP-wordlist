import random
from colorama import Fore, init
init()

print(Fore.CYAN + """
__          __ _____   _____                               _  _  _       _
\ \        / /|  __ \ |  __ \                             | || |(_)     | |
 \ \  /\  / / | |__) || |__) | __      __  ___   _ __   __| || | _  ___ | |_
  \ \/  \/ /  |  ___/ |  ___/  \ \ /\ / / / _ \ | '__| / _` || || |/ __|| __|
   \  /\  /   | |     | |       \ V  V / | (_) || |   | (_| || || |\__ \| |_
    \/  \/    |_|     |_|        \_/\_/   \___/ |_|    \__,_||_||_||___/ \__| alesmaco-666

"""                                                                                                                  
)
idioma = str(input('\033[1m' + Fore.WHITE + "Language/lenguaje (es[español]/en[english]): " + '\033[0m'))

if idioma == "es":

    longitud = int(input('\033[1m' + Fore.WHITE + "cuantas contraseñas quieres en la wordlist: " + '\033[0m'))
    nombre = str(input('\033[1m' + Fore.WHITE + "Nombre de la wordlist: " + '\033[0m'))
    numeroAleatorio = str(input('\033[1m' + Fore.WHITE + "Numeros aleatorio si/no: " + '\033[0m'))
    Name1delavictima = str(input('\033[1m' + Fore.WHITE + "Primer Nombre de la victima: " + '\033[0m'))
    Name2delavictima = str(input('\033[1m' + Fore.WHITE + "Segundo Nombre de la victima: " + '\033[0m'))
    apellido1 = str(input('\033[1m' + Fore.WHITE + "Primer Apellido de la victima: " + '\033[0m'))
    apellido2 = str(input('\033[1m' + Fore.WHITE + "Segundo Apellido de la victima: " + '\033[0m'))
    Dia = str(input('\033[1m' + Fore.WHITE + "Dia de nacimiento de la victima (DD): " + '\033[0m'))
    Mes = str(input('\033[1m' + Fore.WHITE + "Mes de nacimiento de la victima (MM): " + '\033[0m'))
    Año = str(input('\033[1m' + Fore.WHITE + "Año de nacimiento de la victima (YYYY): " + '\033[0m'))
    Name1delpadre = str(input('\033[1m' + Fore.WHITE + "Primer Nombre del padre de la victima: " + '\033[0m'))
    Name2delpadre = str(input('\033[1m' + Fore.WHITE + "Segundo Nombre del padre de la victima: " + '\033[0m'))
    Name1delamadre = str(input('\033[1m' + Fore.WHITE + "Primer Nombre de la madre de la victima: " + '\033[0m'))
    Name2delamadre = str(input('\033[1m' + Fore.WHITE + "Segundo Nombre de la madre de la victima: " + '\033[0m'))
    Name1delhermano = str(input('\033[1m' + Fore.WHITE + "Primer Nombre del hermano de la victima: " + '\033[0m'))
    Name2delhermano = str(input('\033[1m' + Fore.WHITE + "Segundo Nombre del hermano de la victima: " + '\033[0m'))
    Name1delahermana = str(input('\033[1m' + Fore.WHITE + "Primer Nombre de la hermana de la victima: " + '\033[0m'))
    Name2delahermana = str(input('\033[1m' + Fore.WHITE + "Segundo Nombre de la hermana de la victima: " + '\033[0m'))
    Namedelamascota = str(input('\033[1m' + Fore.WHITE + "Nombre de la mascota de la victima: " + '\033[0m'))
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

# ...existing code...
elif idioma == "en":
    length = int(input('\033[1m' + Fore.WHITE + "How many passwords do you want in the wordlist: " + '\033[0m'))
    name = str(input('\033[1m' + Fore.WHITE + "Name of the wordlist: " + '\033[0m'))

    randomNumbers = str(input('\033[1m' + Fore.WHITE + "Random numbers? (yes/no): " + '\033[0m'))
    VictimFirstName = str(input('\033[1m' + Fore.WHITE + "Victim's first name: " + '\033[0m'))
    VictimMiddleName = str(input('\033[1m' + Fore.WHITE + "Victim's middle name: " + '\033[0m'))
    Surname1 = str(input('\033[1m' + Fore.WHITE + "Victim's first surname: " + '\033[0m'))
    Surname2 = str(input('\033[1m' + Fore.WHITE + "Victim's second surname: " + '\033[0m'))
    Day = str(input('\033[1m' + Fore.WHITE + "Victim's Birth Day (DD): " + '\033[0m'))
    Month = str(input('\033[1m' + Fore.WHITE + "Victim's Birth Month (MM): " + '\033[0m'))
    Year = str(input('\033[1m' + Fore.WHITE + "Victim's Birth Year (YYYY): " + '\033[0m'))
    FatherFirstName = str(input('\033[1m' + Fore.WHITE + "Victim's father's first name: " + '\033[0m'))
    FatherSecondName = str(input('\033[1m' + Fore.WHITE + "Victim's father's second name: " + '\033[0m'))
    MotherFirstName = str(input('\033[1m' + Fore.WHITE + "Victim's mother's first name: " + '\033[0m'))
    MotherSecondName = str(input('\033[1m' + Fore.WHITE + "Victim's mother's second name: " + '\033[0m'))
    BrotherFirstName = str(input('\033[1m' + Fore.WHITE + "Victim's brother's first name: " + '\033[0m'))
    BrotherSecondName = str(input('\033[1m' + Fore.WHITE + "Victim's brother's second name: " + '\033[0m'))
    SisterFirstName = str(input('\033[1m' + Fore.WHITE + "Victim's sister's first name: " + '\033[0m'))
    SisterSecondName = str(input('\033[1m' + Fore.WHITE + "Victim's sister's second name: " + '\033[0m'))
    PetName = str(input('\033[1m' + Fore.WHITE + "Victim's pet's name: " + '\033[0m'))
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