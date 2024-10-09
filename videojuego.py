#primero se declara una lista como vjp (videojuego perfecto) para guardar las 
#caracteristicas deseadas en el juego por el usuario.
vdp=[]

#luego se crea un diccionario de listas de cada juego en la que se guardan las caracteristicas que
#corresponden al juego en la llave.
videogames_dictionary = {"minecraft" : ['P', 'xbox', 'pc', 'play', 'coop', 'aventura', 'low-poly', 'pixelado', \
'supervivencia', 'game pass'], "minecraft_dungeons" : ['P', 'xbox', 'pc', 'play', 'coop', 'aventura', 'pixelado', \
'dungeons', 'game pass'], "cod_warzone" : ['G', 'xbox', 'pc', 'play','multi', 'accion', 'realista', 'ninguno', \
'guerra', 'battle royal']}





#se da una introduccion al usuario para que sepa que hacer y para que sob las preguntas
#que tendra que responder.
print("Hola usuario, espero te encuentres bien. \nA continuacion se te pediran \
ciertas caracteristicas a tu gusto que definiran el videojuego mas apropiado \
para ti en tu proximo juego")

#se hace una funcion con el proceso de pedir las caracteristicas al usuario y guardarlas 
#en lista para que si el usuario al acabar su primer inteno quiere probar con distintas
#caracteriasticas le sea posible.
def lista_usu():
    vjp=[]
    #cada pregunta es sobre una caracteristica distinta que lo que responda el usuario
    #se va guardando como un nuevo dato en la lista vjp gracias a la funcion .append
    #que agrega el input recibido como un valor nuevo hasta el final de la lista vjp.
    vjp.append(input("\nPrimero.\n\n¿Prefieres un juego gratuito o de paga? (pon G o P)\n"))

    vjp.append(input("\n\nAhora bien dime, ¿Que plataforma de juego prefieres? \
(xbox, pc o play)\n"))

    vjp.append(input("\n\nEmpezamos con lo mas importante, ¿Prefieres jugar en solitario, \
un cooperativo o un multijugador? (solo, coop, multi)\n"))

    vjp.append(input("\n\n¿Y que hay del genero que te interesa mas?\n\
(Los generos son: plataformas, puzles, simulacion, RPG, accion, aventura, estrategia, \
deportes, terror, cifi, fantasia y carreras)\n"))

    vjp.append(input("\n\nTambien es importante la apariencia o estilo\
de un juego, ¿Cual te gusta mas?\n(pixelado, realista, retro, \
surrealista, dibujo a mano, multimedia, dibujo animado, noir o \
low-poly)\n"))


    vjp.append(input("\n\n¿Quieres que el juego se encuentre en el game pass, play plus \
o ninguno?\n"))
                    
    vjp.append(input("\n\nPor ultimo, pero no menos importante dime que tematica principal \
prefieres.\n(supervivencia, guerra, carros, aviones, espacio, superheroes, zombies, medieval,\
rutas multiples, granjas, robots, piratas, peleas, playground, escape, dungeons, \
football, basquet, golf, ciclismo, souls like, lego, battle royal, mundo abierto)\n"))
    return vjp


#la funcion agarra las dos listas elegidas, usa la funcion set para quitar valores repetidos
#en ambas y usa la funcion & para sacar la interseccion entre ambas listas para tener como
#resultado una lista de valores en comun entre ambas listas. Luego la funcion len cuenta la
#cantidad de valores en la lista de valores encontrados en ambas listas y devuelve ese conteo.
def num_valores_comun(lista1, lista2):
    return len(set(lista1) & set(lista2))

def valores_comparacion():
    vp=lista_usu()
    compa_dictionary = {}
    for i in videogames_dictionary:
        compa_dictionary.update({i : num_valores_comun(vp,videogames_dictionary[i])})
    return compa_dictionary

#se compara que videojuego tiene mas coincidencias en caracteristicas con las pedidas por
#el usuario y te da el resultado.
def comparar_resultados(a):
    c_dicc = a
    list_res = []
    temp = "minecraft"
    for x in c_dicc:
        if c_dicc[x] >= c_dicc[temp]:
            v_definitivo = x
            print(v_definitivo)
        elif c_dicc[temp] < c_dicc[x]:
            v_definitivo = temp
            print(v_definitivo)
        temp = x

    list_res.append(v_definitivo)
    for i in c_dicc:
        if c_dicc[v_definitivo] == c_dicc[i] and i != v_definitivo:
            list_res.append(i)
    
    return list_res


def respuesta(lista):
    if len(lista) == 1:
        return "El videojuego perfecto para ti es: ", lista
    else:
        return "Los videojuegos perfectos para ti son: ", lista

#funcion para volver a preguntar caracteristicas al usuario y hacer la comparacion si el
#usuario quiere repetir
def repetir():
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


print(respuesta(comparar_resultados(valores_comparacion())))
print(repetir())
