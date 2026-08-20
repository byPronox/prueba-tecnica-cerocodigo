# Prueba tecnica - Cerocodigo.com

Este repo tiene la solucion de la prueba tecnica que pidieron para la
vacante de Desarrollador Python/Django.

## Que hay aca

- ejercicio1.py - funcion que agrupa las ventas por cliente y las
  ordena de mayor a menor segun el total comprado.
- ejercicio2.py - formulario de Django con las validaciones que
  pidieron para el modelo Producto, sin modificar el modelo. Ahi mismo
  explico la contradiccion que encontre en los requisitos.
- ejercicio3.py - la funcion calcular_total corregida, el bug era que
  usaban "=" en vez de "+=" asi que se perdia la suma de los productos
  anteriores en cada vuelta del for.

## Como correrlo

Los ejercicios 1 y 3 se corren directo:

python3 ejercicio1.py
python3 ejercicio3.py

El ejercicio 2 no se puede correr solo porque necesita un proyecto
Django con el modelo Producto ya armado usa un import de .models,
lo deje como esta para mostrar como lo resolveria.

## Explicacion rapida de cada ejercicio

Ejercicio 1: use un diccionario para ir sumando el total y contando
las compras de cada cliente mientras recorro la lista una sola vez, y
al final lo paso a una lista para poder ordenarlo con sort().

Ejercicio 2: el problema es que el campo codigo tiene unique=True
en el modelo, y eso hace que la base de datos rechace codigos
duplicados para cualquier usuario, sin excepcion. Entonces pedir que
el admin si pueda duplicar codigos no se puede cumplir sin tocar el
modelo, y el enunciado dice que no se puede modificar. Lo que hice fue
dejarlo documentado en el codigo y armar las demas validaciones
nombre obligatorio, precio mayor a 0, stock no negativo ya que si se
pueden hacer sin tocar el modelo.

Ejercicio 3: el bug principal era el "=" que debia ser "+=",
porque asi como estaba, cada vuelta del for pisaba el total anterior
en vez de sumarlo. Tambien le agregue una validacion para que si un
producto no tiene "cantidad" o "precio", simplemente lo salte y siga
con los demas en vez de que se caiga todo.

## Herramientas que use

Python 3, y busque un poco en documentacion de Django para el tema de
las validaciones en el formulario. Cualquier cosa la puedo explicar
sin problema en la entrevista.