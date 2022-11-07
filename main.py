#Marjori - Richard - Felipe
import requests

class Pokemon:

    def __init__(self, name, habilidad, url_imagen):
        self.name = name
        self.habilidad:list[any] = habilidad
        self.url_imagen = url_imagen

    def mostrar_datos(self):
        print(f"Pokemon: {self.name}",
              f"\nHabilidades: {self.habilidad}",
              f"\nUrl_Imagen: {self.url_imagen}"
              )

def mostrar_menu(opciones):
    print('Opciones del Menú:')
    for clave in opciones:
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Selecciona una opción: ')) not in opciones:
        print('Opción incorrecta,volver a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def menu_principal():
    opciones = {
        '1': ('Opción 1: Listar pokemons por generación.', opcion1),
        '2': ('Opción 2: Listar pokemons por forma.', opcion2),
        '3': ('Opción 3: Listar pokemons por habilidad.', opcion3),
        '4': ('Opción 4: Listar pokemons por habitat.', opcion4),
        '5': ('Opción 5: Listar pokemons por tipo.', opcion5),
        '6': ('Salir', salir)
    }

    generar_menu(opciones, '6')

def lee_entero(msg):
    while True:
        valor = input(f"{msg}")
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print ("Ingresar un número")
            
# *** Definicion de funciones ****
api_pokemon = "https://pokeapi.co/api/v2/pokemon/"
def opcion1():
    generacion = lee_entero("Ingrese una generación (1-8):")
    while (int(generacion) == 0) or (int(generacion) > 8):
        print("¡Ha escrito un numero de generación fuera del rango")
        generacion = lee_entero("Ingrese una generación (1-8):")
    api_generacion = "https://pokeapi.co/api/v2/generation/" + str(generacion) + "/"
    response = requests.get(api_generacion)
    data = response.json()
    print(f"****Lista de Pokemones****")
    for pokemon in data['pokemon_species']:
        response_pokemon = requests.get(api_pokemon + pokemon['name'])
        data_pokemon = response_pokemon.json()
        MiPokemon = Pokemon(
            data_pokemon["name"],
            list(habilidad["ability"]["name"] for habilidad in data_pokemon["abilities"]),
            data_pokemon["sprites"]['front_default']
        )
        MiPokemon.mostrar_datos()
        print("-"*50)

def opcion2():
    print('Elejiste la opción 2')

def opcion3():
    print('Elejiste la opción 3')

def opcion4():
    print('Elejiste la opción 4')

def opcion5():
    print('Elejiste la opción 5')

def salir():
    print('Salir')


if __name__ == '__main__':
    menu_principal()
print ("Ojala funcione")
print ("Hola soy Richard")
print ("Hola soy Richard Ore")