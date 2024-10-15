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
videogames_dictionary = {"minecraft" : ['P', 'xbox', 'pc', 'play', 'coop', 
'aventura', 'low-poly', 'pixelado', 'supervivencia', 'game pass'], 
"minecraft_dungeons" : ['P', 'xbox', 'pc', 'play', 'coop', 'aventura', 
'pixelado', 'dungeons', 'game pass'], "cod_warzone" : ['G', 'xbox', 'pc', 
'play','multi', 'accion', 'realista', 'ninguno', 'guerra', 'battle royal']}


print("Hola usuario, espero te encuentres bien. \nA continuacion se te pediran \
ciertas caracteristicas a tu gusto que definiran el videojuego mas apropiado \
para ti en tu proximo juego")

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
    vjp=[]
    vjp.append(input("\nPrimero.\n\n¿Prefieres un juego gratuito o de paga? \
(pon G o P)\n"))

    vjp.append(input("\n\nAhora bien dime, ¿Que plataforma de juego prefieres? \
(xbox, pc o play)\n"))

    vjp.append(input("\n\nEmpezamos con lo mas importante, ¿Prefieres jugar en \
solitario, un cooperativo o un multijugador? (solo, coop, multi)\n"))

    vjp.append(input("\n\n¿Y que hay del genero que te interesa mas?\n\
(Los generos son: plataformas, puzles, simulacion, RPG, accion, aventura, \
estrategia, deportes, terror, cifi, fantasia y carreras)\n"))

    vjp.append(input("\n\nTambien es importante la apariencia o estilo\
de un juego, ¿Cual te gusta mas?\n(pixelado, realista, retro, \
surrealista, dibujo a mano, multimedia, dibujo animado, noir o \
low-poly)\n"))


    vjp.append(input("\n\n¿Quieres que el juego se encuentre en el game pass, \
play plus o ninguno?\n"))
                    
    vjp.append(input("\n\nPor ultimo, pero no menos importante dime que \
tematica principal prefieres.\n(supervivencia, guerra, carros, aviones, \
espacio, superheroes, zombies, medieval, rutas multiples, granjas, \
robots, piratas, peleas, playground, escape, dungeons, football, basquet, \
golf, ciclismo, souls like, lego, battle royal, mundo abierto)\n"))
    return vjp

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
    vp=lista_usu()
    compa_dictionary = {}
    for i in videogames_dictionary:
        compa_dictionary.update({i : num_valores_comun(vp,videogames_dictionary[i])})
    return compa_dictionary


def comparar_resultados(a):
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
    c_dicc = a
    list_res = []
    temp = "minecraft"
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
    answer=int(input("pon un 1 si quieres poner distintas caracteristicas y obtener \
otro juego y 0 si no "))

    while answer>1:
        answer=int(input("pon un 1 si quieres poner distintas caracteristicas y obtener \
otro juego y 0 si no "))
    if answer==1:
        print(respuesta(comparar_resultados(valores_comparacion())))
        return repetir()
    else:
        return "ten un buen dia usuario!"

#Se muestra el cuestionario de caracteristicas con su resultado y repetir().
print(respuesta(comparar_resultados(valores_comparacion())))
print(repetir())
