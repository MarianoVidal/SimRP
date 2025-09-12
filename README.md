# SIMulador de Redes de Petri (SIMRP)

## 1. Acerca del proyecto

    este proyecto tiene cuatro propósitos
    mas que nada: familiarizarse con Git,
    familiarizarse con Python, meterme en
    la labor de documentar un proyecto, y 
    sacarme una idea que viene respawnean-
    do en mi mente hace meses. si además
    termina siendo útil en algún respecto, 
    esto es meramente accidental.

    la ídea es crear un programa que, 
    dado un archivo escrito bajo cierta
    sintaxis, interprete eso como una Red
    de Petri y permita su simulación, por
    medio de comandos que introduzcan 
    tokens en la red.

    voy a servirme de lo que aprendí
    durante la cursada de Ingenería de
    Software 1 para modelar las estruc-
    turas de datos y algoritmos necesa-
    rios. y si algo lo requiere, iré a
    consultar mas bibliografía sobre el
    tema (toda la bibliografía que use
    y como la usé va a aparecer deta-
    llada en algún devlog quizás.

## 2. Especificación
    
### 2.1 Elementos

    un LUGAR se representa como
    P<NUM>{: <NOMBRE>}, donde NUM
    es un número natural mayor a 0 que
    sirve para identificar al LUGAR, y
    donde NOMBRE es una etiqueta que 
    se le puede colocar opcionalmente.
    
    una TRANSICION se representa
    como T<NUM>{: <NOMBRE>}, donde
    NUM es un número mayor a 0 que
    sirve para identificar a la TRAN-
    SICION, y donde NOMBRE es una
    etiqueta que se le puede colocar
    opcionalmente.

    un ARCO se representa como
    "-{peso: <PESO>}->", donde dentro
    suyo puede específicarse el valor
    del peso del ARCO, que por defecto
    es de 1. un ARCO siempre tiene
    que estar en el medio entre un
    LUGAR y una TRANSICION o
    viceversa. si la relación es del
    primer tipo, entonces el arco
    actuará como un ARCO DE ENTRADA
    para la *transición* de la relación.
    si es del segundo tipo, actuará 
    como un ARCO DE SALIDA.

    un TOKEN representa un item
    cualquiera que se va moviendo por
    los lugares de la red y habilita
    o deshabilita las transiciones
    correspondientes.

### 2.2 Punto de entrada y de salida

    si una TRANSICION es la primera
    en una cadena de relaciones entre
    LUGARES y TRANSICIONES, entonces
    esta TRANSICION será una TRANSICION
    FUENTE y se encargará de
    introducir los tokens en la red.
    
    si una TRANSICION es la última
    en una cadena de relaciones entre
    LUGARES y TRANSICIONES, entonces
    esta TRANSICION será una TRANSICION
    FINAL y se encargará de
    eliminar los tokens de la red.

### 2.3 Limitaciones
    
    no estoy seguro como voy a hacer
    para representar el elemento de
    indeterminismo en la simulación, ni
    si lo voy a hacer dado que se sale
    del alcance que tenía pretendido para
    el proyecto. si lo hago quizás sea
    valiéndome de un Math.random() o
    algo similar.

## 3. Bibliografía

    hasta el momento todo sale de
    las filminas de la cátedra de
    Ingeniería de Software 1 de la
    UNLP.
