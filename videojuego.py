vjp=[]
minecraft=['P', 'xbox', 'pc', 'play', 'coop', 'aventura', 'low-poly', 'pixelado', \
'supervivencia']


print("Hola usuario, espero te encuentres bien. \nA continuacion se te pediran\
ciertas caracteristicas a tu gusto que definiran el videojuego mas apropiado\
 para ti en tu proximo juego")

vjp.append(input("\nPrimero.\n\n¿Prefieres un juego gratuito o de paga? (pon G o P)\n"))

vjp.append(input("\n\nAhora bien dime, ¿Que plataforma de juego prefieres? \
(xbox, pc o play)\n"))

vjp.append(input("\n\nEmpezamos con lo mas importante, ¿Prefieres jugar en solitario, \
un cooperativo o un multijugador? (solo, coop, multi)\n"))

vjp.append(input("\n\n¿Y que hay del genero que te interesa mas?\n\
(Los generos son: plataformas, puzles, simulacion, RPG, accion, aventura, estrategia \
deportes, terror, ciencia ficcion, fantasia y carreras)\n"))

vjp.append(input("\n\nTambien es importante la apariencia o estilo\
 de un juego, ¿Cual te gusta mas?\n (pixelado, realista, retro, \
surrealista, dibujo a mano, multimedia, dibujo animado, noir o \
low-poly)\n"))

vjp.append(input("\n\nPor ultimo, pero no menos importante dime que tematica principal\
 prefieres.\n(supervivencia, guerra, carros, aviones, espacio, heroes, zombies, medieval,\
 rutas multiples, granjas, robots, piratas, peleas, playground, escape, daungeons, \
football, basquet, golf, ciclismo, souls like, lego,)\n"))

def num_valores_comun(lista1, lista2):
    return len(set(lista1) & set(lista2))

print(num_valores_comun(vjp, minecraft))
