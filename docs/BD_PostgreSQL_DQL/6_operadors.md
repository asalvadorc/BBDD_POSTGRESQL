# 4.1 Operadores

Los operadores que se gastan en el SQL de PostgreSQL son muchísimos. Cada tipo
de datos tiene una serie de operadores, y el propio operador, aplicado a tipos
distintos puede hacer cosas distintas.

Se pueden ver todos los operadores en la tabla **PG_OPERATOR** , donde tendremos el
nombre del operador, los tipos de datos de los operandos y del resultado y el
procedimiento que implementa el operador. Aquí tenemos una vista de esta mesa,
aunque hay tantísimos operadores que marea y todo (los que están repetidos
es para especificar la actuación sobre operandos de distintos tipos).

![](T6_1_6_1.png)

Podríamos incluso definir a nuestros operadores, con la sentencia **CREATE
OPERATOR** , donde definiríamos el tipo del operador de la izquierda, el de la
derecha, la función que implementa el operador, ... Lo intentaremos en el tema
siguiente, cuando ya sepamos crear funciones.

No realizaremos un repaso extenso de todos los operadores. Sólo los más habituales, y
alguno de un tipo de datos especial. Los tipos de datos los veremos en la
tercera parte de este tema, cuando las sentencias de creación de tablas.

Por tanto, fíjese sobre todo en los operadores **aritméticos** , de **cadena** y
de **comparación**.

**Operadores aritméticos**{.azul}


+ |  Suma |  - |  Resto |  * |  Multiplicación |  / |División  
---|---|---|---|---|---|---|---
^ |  Exponenciación |  \|/ |  Raíz cuadrada |  ! |  Factorial |  % |  Módulo (resto de la división)  
  
**<u>Ejemplos</u>**
```
SELECT |/16;

SELECT 5 ^ 3;

SELECT 5!;
```

**Operadores de cadena**{.azul}

\|\| |  Concatenación  
---|---  
  
**<u>Ejemplos</u>**
```
SELECT 'Data i hora actual: ' || Now();
```

**Operadores de comparación**{.azul}

= |  Igual | < > | Distinto | != |  Distinto | | |
---|---|---|---|---|---|---|---
\> |  Mayor |  > = |  Mayor o igual |  < |  Menor |  < = |  Menor o igual

  
Se utilizan principalmente en las condiciones. Vuelven siempre un valor booleano
(true o false)


**Operadores conversor de tipos**{.azul}

```
::tipus
```

Servirá para convertir algún dato a algún tipo de datos.

Así, por ejemplo,

  * **'25-4-2012'::date** estamos convirtiendo una cadena de texto en un dato de tipo date.
  * **'(0,0)'::point** estamos convirtiendo el texto a un punto.

La forma utilizada en los ejemplos anteriores es una forma muy habitual de
poner las constantes de un determinado tipo: la ponemos como cadena de caracteres
(entre comillas) y después la convertimos. La única restricción será que PostgreSQL
"entienda" lo que hay entre comillas para realizar la conversión.

Para ver que realmente existe un cambio nos aprovechamos de DBeaver que dice de cuál
tipos es un campo, si puede. Observe que en el primer campo no hemos puesto más que
una tira de caracteres, pero en el segundo intentamos reconvertir esta misma
tira de índoles al tipo POINT. En el resultado se observa cómo ha entendido que el
tipos del dato es POINT.

![](T6_1_6_2.png)

También nos serviría la función **point ('(0,0)')**

**<u>Operadores Geométricos</u>**

**Operador** |  **Descripción** |  **Utilización**  
---|---|---  
<-> |  Distancia (deben ser del mismo tipo) |  point '(1,0)' <-> point '(3,0)'  
<@ |  Està contingut en? |  '(1,1)'::point @ '((0,0),(2,2))'::box  
@> |  ¿Contiene? |  box '((0,0),(2,2))' @> point '(1,1)'  
  
La lista de operadores es mucho más larga, pero aquí sólo queremos mostrarlos
alguno a modo ilustrativo.

Podemos realizar comprobaciones de este tipo:
```
SELECT '(0,0)'::point <-> '(3,4)'::point;
```
que nos dará la **distancia** entre el punto **(0,0)** y el punto **(3,4)**.
Esta distancia debe ser 5.
```
SELECT '(1,1)'::point <@ '((0,0),2)'::circle;
```
que nos dirá si el **punto** **(1,1)** está **dentro** del **círculo con origen
(0,0) y radio 2**. Debido a que sí está devolverá el valor **true** (verdadero).



Licenciado bajo la [Licencia Creative Commons Reconocimiento NoComercial
CompartirIgual 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/)

