import random
from colorama import init, Fore



CATEGORIAS = {
    "Comidas": ["hamburguesa", "pizza", "milanesa", "empanada", "papas fritas", "fideos", "asado", "ñoquis", "torta", "tortilla", "flan", "alfajor"],

    "Deportes": ["futbol", "tenis", "natacion", "basquet", "voley", "rugby", "atletismo", "ciclismo"],
    
    "Clima": ["tormenta", "lluvia", "viento", "granizo", "nevada", "neblina", "soleado", "sequia"],
    
    "Cine": ["pelicula", "actor", "director", "aventura", "comedia", "terror", "guion", "estreno"],
    
    "Paises": ["argentina", "brasil", "italia", "francia", "uruguay", "japon", "canada", "mexico"],
    
    "Animales": ["elefante", "jirafa", "delfin", "caballo", "tortuga", "murcielago", "cocodrilo", "leon", "perro", "gato"],
    
    "Frutas": ["manzana", "banana", "frutilla", "durazno", "naranja", "sandia", "cereza", "anana"],
    
    "Trabajos": ["medico", "abogado", "ingeniero", "arquitecto", "bombero", "profesor", "panadero", "electricista"],
    
    "Tecnologia": ["teclado", "monitor", "internet", "programas", "celular", "computadora", "wifi", "pantalla"],
    
    "Musica": ["guitarra", "bateria", "piano", "violin", "trompeta", "flauta", "concierto", "cantante"],
    
    "Transporte": ["bicicleta", "colectivo", "avion", "camion", "moto", "tren", "barco", "subte"],
    
    "Cuerpo humano": ["corazon", "pulmon", "cerebro", "rodilla", "hombro", "columna", "estomago", "pierna"]
}

NOMBRES_CATEGORIAS = ("Comidas", "Deportes", "Clima", "Cine", "Paises", "Animales", "Frutas", "Trabajos", "Tecnologia", "Musica", "Transporte", "Cuerpo humano")

DIFICULTADES = (("Facil", 10), ("Medio", 7), ("Extremo", 5))

MIN_VIDAS = 1
MAX_VIDAS = 24
PARTES_CUERPO = 6
ABECEDARIO = "abcdefghijklmnopqrstuvwxyz"



def elegir_categoria(opcion):
    if opcion > len(NOMBRES_CATEGORIAS):
        return random.choice(NOMBRES_CATEGORIAS)
    return NOMBRES_CATEGORIAS[opcion - 1]


def elegir_palabra(categoria):
    return random.choice(CATEGORIAS[categoria])



def pedir_opcion(mensaje, minimo, maximo):
    while True:
        try:
            opcion = int(input(mensaje))
        except ValueError:
            print("Oops! No era valido. Ingresa un numero.")
        else:
            if opcion >= minimo and opcion <= maximo:
                return opcion
            print(f"Opcion fuera de rango. Elegi un numero entre {minimo} y {maximo}.")


def pedir_letra():
    while True:
        letra = input("Ingresa una letra: ").lower()
        if len(letra) == 1 and ABECEDARIO.find(letra) != -1:
            return letra
        print("Ingresa solamente una letra de la A a la Z.")


def pedir_si_no(mensaje):
    while True:
        respuesta = input(mensaje).lower()
        if respuesta == "s" or respuesta == "si":
            return True
        if respuesta == "n" or respuesta == "no":
            return False
        print("Responde con s (si) o n (no).")



def elegir_vidas(opcion):
    if opcion > len(DIFICULTADES):
        mensaje = f"Cuantas vidas queres? ({MIN_VIDAS} a {MAX_VIDAS}): "
        return pedir_opcion(mensaje, MIN_VIDAS, MAX_VIDAS)
    return DIFICULTADES[opcion - 1][1]



def contiene(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False


def armar_palabra_oculta(palabra, letras_usadas):
    resultado = ""
    for i in range(len(palabra)):
        if contiene(letras_usadas, palabra[i]):
            resultado = resultado + palabra[i] + " "
        else:
            resultado = resultado + "_ "
    return resultado


def palabra_completa(palabra, letras_usadas):
    for i in range(len(palabra)):
        if not contiene(letras_usadas, palabra[i]):
            return False
    return True



def dibujar_muneco(errores, vidas_totales):
    partes = PARTES_CUERPO - (errores * PARTES_CUERPO) // vidas_totales

    cabeza = " "
    torso = " "
    brazo_izq = " "
    brazo_der = " "
    pierna_izq = " "
    pierna_der = " "

    if partes >= 1:
        cabeza = "O"
    if partes >= 2:
        torso = "|"
    if partes >= 3:
        brazo_izq = "-"
    if partes >= 4:
        brazo_der = "-"
    if partes >= 5:
        pierna_izq = "|"
    if partes >= 6:
        pierna_der = "|"

    print(Fore.RED + "  +-------+")
    print(Fore.RED + "  |       |")
    print(Fore.RED + "  |       " + cabeza)
    print(Fore. RED+ "  |      " + brazo_izq + torso + brazo_der)
    print(Fore.RED + "  |       " + torso)
    print(Fore.RED + "  |      " + pierna_izq + " " + pierna_der)
    print(Fore.RED + "  |")
    print(Fore.RED + "==+==")



def jugar(categoria, vidas):
    palabra = elegir_palabra(categoria)
    vidas_totales = vidas
    letras_usadas = []
    letras_incorrectas = []

    print("\nCategoria:", categoria)

    while vidas > 0 and not palabra_completa(palabra, letras_usadas):
        print()
        dibujar_muneco(vidas_totales - vidas, vidas_totales)
        print("\nPalabra:", armar_palabra_oculta(palabra, letras_usadas))
        print("Vidas:", vidas)
        print("Letras usadas:", letras_usadas)
        print("Letras incorrectas:", letras_incorrectas)

        letra = pedir_letra()

        if contiene(letras_usadas, letra):
            print("Ya utilizaste esa letra.")
        elif palabra.find(letra) == -1:
            letras_usadas.append(letra)
            letras_incorrectas.append(letra)
            vidas = vidas - 1
            print(Fore.RED + "Letra incorrecta. Perdiste una vida.")
        else:
            letras_usadas.append(letra)
            print(Fore.GREEN + "Bien! Esa letra SI esta en la palabra.")

    print()
    dibujar_muneco(vidas_totales - vidas, vidas_totales)

    if vidas > 0:
        print(Fore.GREEN + "\nfelicidades por esa victoria :D !")
        print("La palabra era:", palabra)
        print("Vidas restantes:", vidas)
    else:
        print(Fore.RED + "\nGAME OVER 😂 ")
        print("La palabra era:", palabra)



def menu_categoria():
    print(Fore.YELLOW + "\n=== JUEGO DEL AHORCADO ===")
    for i in range(len(NOMBRES_CATEGORIAS)):
        print(f"{i + 1} - {NOMBRES_CATEGORIAS[i]}")
    print(f"{len(NOMBRES_CATEGORIAS) + 1} - ETC (categoria aleatoria)")

    opcion = pedir_opcion("Elegi una categoria: ", 1, len(NOMBRES_CATEGORIAS) + 1)
    return elegir_categoria(opcion)


def menu_dificultad():
    print()
    for i in range(len(DIFICULTADES)):
        nombre = DIFICULTADES[i][0]
        cantidad = DIFICULTADES[i][1]
        print(f"{i + 1} - {nombre} ({cantidad} vidas)")
    print(f"{len(DIFICULTADES) + 1} - Personalizado (elegis cuantas vidas)")

    opcion = pedir_opcion("Elegi la dificultad: ", 1, len(DIFICULTADES) + 1)
    return elegir_vidas(opcion)



def main():
    init(autoreset=True)
    try:
        jugando = True
        while jugando:
            categoria = menu_categoria()
            vidas = menu_dificultad()
            jugar(categoria, vidas)
            jugando = pedir_si_no("\nQueres jugar otra vez? (s/n): ")
    except KeyboardInterrupt:
        print("\nPartida finalizada.")
    except EOFError:
        print("\nSe cerro la entrada de datos. Partida finalizada.")
    finally:
        print("Gracias por jugar...                                                                     (JUEGO CREADO POR GINO LASPINA.)")



if __name__ == '__main__':
    main()
