"""
Proyecto TC1028
Cuestionario para el videojuego perfecto.
El cuestionario realiza una serie de preguntas para definir las caracteristicas
en un juego que más prefiere el usuario y compara estas caracteristicas con las
que tienen distintos juegos para hallar el que tenga más coincidencia y por
consiguiente sea el juego indicado para el usuario.
Le da al usuario el o los juegos que más coincidencias tuvieran con sus 
preferencias.
"""

"""
=================Diccionario de videojuegos con caracteristicas=================
"""
videogames_dictionary = {"Minecraft" : ['p', 'xbox', 'pc', 'play', 'coop', 
'aventura', 'low-poly', 'pixelado', 'supervivencia', 'game pass'], 
"Minecraft Dungeons" : ['p', 'xbox', 'pc', 'play', 'coop', 'aventura', 
'pixelado', 'dungeons', 'game pass'], "Cod Warzone" : ['g', 'xbox', 'pc', 
'play','multi', 'accion', 'realista', 'ninguno', 'guerra', 'battle royal'],
"Hollow Knight" : ['p', 'xbox', 'pc', 'play', 'solo', 
'plataformas', 'low-poly', 'dibujo a mano', 'souls like', 'game pass'], 
"Fortnite" : ['g', 'xbox', 'pc', 'play','multi', 'accion', 'caricaturesco', 
'ninguno', 'guerra', 'battle royal'], "Moonlighter" : ['p', 'xbox', 'pc', 
'play', 'solo', 'accion', 'rpg', 'pixelado', 'dungeons', 'game pass'], 
"Human Fall Flat" : ['p', 'xbox', 'pc', 'play', 'coop', 'plataformas', 
'low-poly', 'puzzles', 'supervivencia', 'game pass'], "Gang Beasts" : ['p', 
'xbox', 'pc', 'play', 'multi', 'plataformas', 'low-poly', 'accion', 
'peleas', 'game pass'], "Detroit Become Human" : ['p', 'play', 'pc', 'accion', 
'solo', 'realista', 'cifi', 'rutas multiples', 'play plus', 'robots'], 
"The Last Of Us" : ['p', 'play', 'pc', 'accion', 'solo', 'realista', 'terror', 
'zombies', 'play plus'], "The Witcher 3" : ['p', 'play', 'pc', 'rpg', 'solo', 
'realista', 'medieval', 'mundo abierto', 'play plus'], "Ghost of Tsushima" : 
['p', 'play', 'pc', 'rpg', 'solo', 'realista', 'souls like', 'mundo abierto', 
'play plus'], "Uncharted" : ['p', 'play', 'pc', 'accion', 'solo', 'realista', 
'tesoros', 'aventura', 'play plus'], "Spiderman" : ['p', 'play', 'pc', 'accion',
'solo', 'realista', 'superheroes', 'aventura', 'play plus', 'mundo abierto'],
"COD Black Ops saga" : ['p', 'play', 'pc', 'xbox','solo', 'realista', 
'coop', 'accion', 'game pass', 'zombies', 'terror', 'guerra', 'supervivencia'],
"Halo" : ['p', 'espacio', 'pc', 'xbox','solo', 'realista', 'coop', 'accion', 
'game pass', 'cifi', 'guerra'], "Forza" : ['p', 'carros', 'pc', 'xbox','solo', 
'realista', 'accion', 'game pass', 'carreras'], "GTA V" : ['p', 'play', 'pc',
'xbox','solo', 'multi', 'accion', 'realista', 'ninguno', 'mundo abierto',
'rutas multiples'], "Roblox" : ['g', 'play', 'pc','xbox','solo', 'coop', 
'accion', 'plataformas', 'ninguno', 'playgorund'], "For Honor" : ['p', 'play', 
'pc','xbox','solo', 'multi', 'accion', 'realista', 'ninguno', 'guerra',
'medieval'], "Sea of Thieves" : ['p', 'piratas', 'pc', 'xbox', 'solo', 'multi', 
'accion', 'caricaturesco', 'game pass', 'mundo abierto', 'tesoros']}


print("Hola usuario, espero te encuentres bien. \nA continuacion se te pediran \
ciertas caracteristicas a tu gusto que definiran el videojuego mas apropiado \
para ti en tu proximo juego")

print("Tenga en cuenta que si la respuesta dada no es una de las indicadas \
entre parentesis en cada pregunta esta no contara, ya que no coincidira con\
las registradas en la base de datos.")
"""
==============================Funcion de preguntas==============================
"""
def lista_usu():
    """
    (uso de listas, funciones)
    Recopila las caracteristicas que el usuario quiere en un juego en una lista.
    Crea una lista con las caracteristicas que el usuario desee en su juego en
    base a siete preguntas.
    Devuelve: la lista con las caracteristicas que el usuario decide.
    """
    video_juego_usu=[]
    video_juego_usu.append((input("\nPrimero.\n\n¿Prefieres un juego gratuito o de paga? \
(pon G o P)\n")).lower())

    video_juego_usu.append(input("\n\nAhora bien dime, ¿Que plataforma de juego prefieres? \
(xbox, pc o play)\n").lower())

    video_juego_usu.append(input("\n\nEmpezamos con lo mas importante, ¿Prefieres jugar en \
solitario, un cooperativo o un multijugador? (solo, coop, multi)\n").lower())

    video_juego_usu.append(input("\n\n¿Y que hay del genero que te interesa mas?\n\
(Los generos son: plataformas, puzzles, simulacion, RPG, accion, aventura, \
estrategia, deportes, terror, cifi, fantasia y carreras)\n").lower())

    video_juego_usu.append(input("\n\nTambien es importante la apariencia o estilo\
de un juego, ¿Cual te gusta mas?\n(pixelado, realista, retro, \
surrealista, dibujo a mano, multimedia, dibujo animado, caricaturesco, noir o \
low-poly)\n").lower())


    video_juego_usu.append(input("\n\n¿Quieres que el juego se encuentre en el game pass, \
play plus o ninguno?(game pass, play plus, ninguno)\n").lower())
                    
    video_juego_usu.append(input("\n\nPor ultimo, pero no menos importante dime que \
tematica principal prefieres.\n(supervivencia, guerra, carros, aviones, \
espacio, superheroes, zombies, medieval, rutas multiples, granjas, \
robots, piratas, peleas, playground, escape, dungeons, souls like, battle royal, \
mundo abierto, tesoros)\n").lower())
    return video_juego_usu

"""
=======================Funciones principales del programa=======================
"""
def num_valores_comun(lista1, lista2):
    """
    (uso de funciones, lista, diccionario)
    Recibe: la lista de caracteristicas que hizo el usuario y los valores de 
    uno de los juegos en el diccionario.
    Se comparan los valores de la lista hecha del usuarion y los de un juego de 
    el diccionario.
    Devuelve: la cantidad de valores iguales entre la lista del usuario y los 
    valores del juego en el diccionario.
    """
    return len(set(lista1) & set(lista2))

def valores_comparacion():
    """
    (uso de funciones, lista,diccionarios, ciclos, condicionales)
    Recibe: lista creada por el usuario de caracteristicas deseadas y 
    diccionario de videojuegos con sus caracteristicas.
    Usa la funcion num_valores_comun(lista1, lista2) y pasa por cada juego 
    en el diccionario para que se haga la comparación con todos y el resultado
    de la comparacion se guarda en un diccionario nuevo con el nombre del juego
    como llave y la cantidad de coincidencias como valor.
    Devuelve: diccionario con el nombre de los videojuegos como llave y de valor
    la cantidad de coincidencias de caracteristicas de ese juego con la lista 
    hecha por el usuario.
    """
    juego_perfecto=lista_usu()
    comparation_dic = {}
    for i in videogames_dictionary:
        comparation_dic.update({i : num_valores_comun(juego_perfecto,videogames_dictionary[i])})
    return comparation_dic


def comparar_resultados(dicc_comparation):
    """
    (uso de funciones, ciclos, ciclos anidados, diccionarios, lista, 
    condicionales)
    Recibe: El diccionario de cantidad de coincidencias con la lista del usuario
    respecto a cada juego resultante de la funcion valores_comparacion().
    Guarda en una variable el nombre de el juego con más coincidencias y 
    luego por si hay más juegos con la misma cantidad de coincidencias 
    se guardan todos los juegos con mayor numero de coincidencias en una lista.
    Devuelve: Una lista con el o los nombres de los juegos con mayor cantidad
    de coincidencias que la lista creada por el usuario.
    """
    c_dicc = dicc_comparation
    list_res = []
    temp = "Minecraft"
    for x in c_dicc:
        if c_dicc[x] >= c_dicc[temp]:
            v_definitivo = x
        elif c_dicc[temp] < c_dicc[x]:
            v_definitivo = temp
        temp = x

    list_res.append(v_definitivo)
    for i in c_dicc:
        if c_dicc[v_definitivo] == c_dicc[i] and i != v_definitivo:
            list_res.append(i)
    
    return list_res

def respuesta(lista):
    """
    (Uso de funciones, lista, condicionales)
    Recibe: La lista con el o los nombres de los juegos con mayor cantidad
    de coincidencias que la lista creada por el usuario, resultante de la 
    funcion comparar_resultados(a).
    Devuelve: La respuesta sobre que juego o juegos son los más indicados 
    para el usuario.
    """
    if len(lista) == 1:
        return "El videojuego perfecto para ti es: ", lista
    else:
        return "Los videojuegos perfectos para ti son: ", lista


def repetir():
    """
    (uso de funciones, ciclos, condicionales)
    Recibe: Si el usuario quiere repetir o no la selección de caracteristicas y
    así obtener un resultado distinto dependioendo de la selección.
    Devuelve: La funcion lista_usu() para volver a hacer selección de 
    caracteristicas en caso de responde si y en caso de responder no, se le 
    desea un buen dia al usuario y acaba el programa.
    """
    answer=str((input("¿Quieres poner distintas caracteristicas y obtener \
otro juego como resultado? \n(si, no)\n"))).lower()

    while not(answer == "si" or answer == "no"):
        answer=str((input("¿Quieres poner distintas caracteristicas y obtener \
otro juego como resultado? \n(si, no)\n"))).lower()
    if answer=="si":
        print(respuesta(comparar_resultados(valores_comparacion())))
        return repetir()
    else:
        return "ten un buen dia usuario!"

#Se muestra el cuestionario de caracteristicas con su resultado y repetir().
print(respuesta(comparar_resultados(valores_comparacion())))
print(repetir())
