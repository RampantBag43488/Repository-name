# Tu Videojuego Ideal
### Iñaki Mancera Llano


Este proyecto tiene como objetivo ayudar a los jugadores de videojuegos a encontrar su próximo juego a conquistar. Como jugador, se debe saber lo difícil que es en contrar con qué videojuego seguir a la hora de acabar uno, ya que probablemente no se conozca muchos o se esté indeciso en la categoría de juegos en la que se quiera incursar. Por esto mismo, en este programa se busca definir cuál puede ser el próximo juego en el que incursarse en base a los tipos de juegos que más llamen la atención, qué categoría atrae más en el momento, si se quiere jugar una gran y emocional historia o  divertirse con amigos en un multijugador.

Este programa presenta una serie de preguntas en las que el usuario debe definir que caracteristicas tenga el juego que quiere jugar, para así el programa usar esta lista y compararla con la base de datos de videojuego que tiene disponibles y darle al usuario el juego con más similitudes a las caracteristicas definidas por el usuario. Iguelmente permite pepetir el codigo indefinidamente mientras el usuario así lo decida para así obtener otros juegos distintos.

Las principales limitaciones que tiene este programa son 2. La primera es que los videojuegos disponibles como base de datos en el programa algunos de los muchos que existen, por lo que puede no soltar lo deseado si este juego no esta en la base de datos. La segunda es que si a la hora de dar las caracteristicas, el usuario no pone el nombre de la caracteristica como es indicado esta practicamente no contaría, ya que cada caracteristica esta definida con un nombre especifico siendo que cualquier variación no se veria igual.

### Errores:
Sub-Competencia: El estilo cumple con las normas y estándares enunciadas en el documento de PEP 8

Error original: Todos mis comentarios estaban fuera de las funciones y escritos con un gato (#) en vez de comillas (").
#la funcion agarra las dos listas elegidas, usa la funcion set para quitar valores repetidos
#en ambas y usa la funcion & para sacar la interseccion entre ambas listas para tener como
#resultado una lista de valores en comun entre ambas listas. Luego la funcion len cuenta la
#cantidad de valores en la lista de valores encontrados en ambas listas y devuelve ese conteo.

Cambio realizado: Cambie y arregle los comentarios para cumplir con los estandares PEP 8
    """
    (uso de funciones, lista, diccionario)
    Recibe: la lista de caracteristicas que hizo el usuario y los valores de 
    uno de los juegos en el diccionario.
    Se comparan los valores de la lista hecha del usuarion y los de un juego de 
    el diccionario.
    Devuelve: la cantidad de valores iguales entre la lista del usuario y los 
    valores del juego en el diccionario.
    """

Líneas de código donde se ve la corrección: Todo el codigo, de 1 a 167

### Incorpora y aplica nuevas funciones en su programa e incluye su referencias al API de Python.
Las funciones que agregue a mi proyecto no vistas en clase fueron los diccionarios y la función set para las listas.
Los diccionarios los utilice para facilitar el guardado y llamado de cada videojuego y sus características, poniendo como llave el nombre del juego y como valor las características del juego. De igual manera más adelante los utilice para crear un segundo diccionario en el que tenga como llave el nombre del juego y como valor la cantidad de valores iguales a la lista hecha por el usuario, para así comparar la cantidad de valores iguales entre cada videojuego y poder dar en el resultado el nombre del juego o juegos que contengan más valores iguales. Aquí los diccionarios facilitan el poder poner el nombre del juego a la hora de dar el resultado al usuario en base a su valor, en este caso el que sea mayor.
Aprendi diccionarios de la pagina w3schools (https://www.w3schools.com/python/python_dictionaries.asp) y de un video de youtube (https://www.youtube.com/watch?v=v25-m1LOUiU).

La función set la use para convertir las listas de características del usuario y de un juego a un conjunto en el que no se repitan valores y así poder obtener un conjunto de los valores repetidos en ambas listas con la función && y luego sacar la cantidad de valores iguales con la función len.
Aprendí cómo funciona la función set mediante un video de youtube (https://www.youtube.com/watch?v=Mzfar-fxfHY).
