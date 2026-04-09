# Ejercicios con los resultados (parte II) {: .ejercicios-header}

**Ex_51** Sacar el nombre de los clientes con el número de factura y la fecha
(individuales, sin agrupar nada) que tiene cada cliente. Saca el resultado ordenado
por cliente, y dentro de éste por fecha de la factura

![](Ex_6_51.png)

Un total de **105 filas**

**Ex_52** Sacar el nombre del socio, con el código y la descripción de cada
artículo que ha pedido. Ordena por nombre del socio y código del artículo.

![](Ex_6_52.png)

Un total de **541 filas**

**Ex_53** Modificar lo anterior para que no se repitan los resultados.

![](Ex_6_53.png)

Un total de ****532 filas****

Observa cómo ahora no se repite la fila 10 y 11, y antes sí

**Ex_54** Sacar el nombre de los clientes con la cantidad de facturas que
tienen, ordenadas por este número de mayor a menor

![](Ex_6_54.png)

Un total de **40 filas**

**Ex_55** Sacar el número de factura, fecha, código de cliente, total de la
factura (con el alias IMPORTE) y total de la factura aplicando descuentos
de artículo (con alias DESCUENTO_1), como en la consulta**Ex_33** , pero sin el
límite de las 10 líneas de factura. Ordena por número de factura.

![](Ex_6_55.png)

Un total de **105 filas**

**Ex_56** Modificar lo anterior para aplicar también el descuento de la
factura (con el sobrenombre DESCUENTO_2)

![](Ex_6_56.png)

Un total de **105 filas**

**Ex_57** Sacar el código y nombre de aquellos vendedores que supervisan a alguien
(consten como cabeza). Sacar también el número de supervisados de cada uno
de estos supervisores.

![](Ex_6_57.png)

**Ex_58** Sacar el código y descripción de los artículos junto con
el número de veces que se ha vendido, el total de unidades vendidas y la media
de unidades vendidas por factura. Ordenar por el número total de unidades vendidas de
forma descendente, y dentro de ésta por código de artículo de forma ascendente.

![](Ex_6_58.png)

Un total de **399 filas**

**Ex_59** Sacar el código y la descripción de las categorías, con la
cantidad de artículos vendidos de cada categoría, de aquellas categorías de las
que se han vendido más de 100 unidades. Ordenar por este número de forma
descendente.

![](Ex_6_59.png)

**Ex_60** Sacar el código y el nombre de los clientes que no tienen ninguna factura.

![](Ex_6_60.png)

**Ex_61** Sacar el código, descripción y total de unidades vendidas de todos
los artículos, incluso de aquellos que no se han vendido nada.

**Nota**

Para dejarlo más bonito, puesto que la suma de valores nulos no es 0 sino nulo,
para que nos aparezca el valor 0 podemos utilizar la función COALESCE(_valor_
,0), que si el valor es nulo devuelve un 0.

![](Ex_6_61.png)

Un total de **812 filas**

**Ex_62** Sacar el nombre de todos los pueblos y el número de clientes en
caso de que tengan. Ordena por número de clientes de forma descendente.

![](Ex_6_62.png)

Un total de **1663 filas**

**Ex_63** Sacar el código y la descripción de las categorías, con el
número de artículos de cada categoría y el número total de unidades vendidas de
cada categoría, de aquellas categorías de las que tenemos más de 15 artículos, y
ordenado por número de artículos de forma descendente. Esta sentencia ya es
bastante complicada. Concretamente tendrá que tener en cuenta que:

  * Querremos sacar el número de artículos de cada categoría, pero quizás algunos artículos no se han vendido, y por tanto no aparecerán en la tabla LINIA_FAC.
  * Y también tenemos el problema de que, como nos hace falta la tabla LINIA_FAC, un artículo vendido en más de una factura aparecerá más de una vez. Si contamos de forma normal, lo contaríamos más de una vez cada artículo. Por tanto queremos contar los diferentes artículos de cada categoría.

![](Ex_6_63.png)

**Ex_64** Sacar el número máximo de facturas hechas a un cliente

![](Ex_6_64.png)

**Ex_65** Sacar el importe que supone la factura más cara y el importe que
supone la más barata (sin considerar ni descuentos ni IVA)

![](Ex_6_65.png)

**Ex_66** Sacar el número de facturas más alto que se ha vendido por vendedor en
cada trimestre (no quitaremos quién es el vendedor, que sería aún más complicado).
Para poder agrupar por trimestre, nos hará falta la función
**TO_CHAR****(fecha,'Q')** , que saca el número de trimestre. El paso previo es
calcular el número de facturas de cada vendedor y en cada trimestre. Después,
con la información anterior, querremos calcular el máximo de cada trimestre.

![](Ex_6_66.png)

**Ex_67** Sacar los artículos más caros que la media. Sáquelos ordenados por
la categoría, y después por código de artículo.

![](Ex_6_67.png)

Un total de **164 filas**

**Ex_68** Modificar lo anterior para sacar los artículos más caros que la
promedio de su categoría. Sáquelos ordenados por la categoría

![](Ex_6_68.png)

Un total de **75 filas**

Es un resultado muy similar al anterior, pero observe que ahora no están los
productos de las filas 5, 14, 15, ...

**Ex_69** Sacar los pueblos donde tenemos clientes pero no tenemos vendedores. Debe ser
mediante subconsultas (en plural). Ordene por código del pueblo.

![](Ex_6_69.png)

**Ex_70** Sacar los pueblos donde tenemos más vendedores que clientes. Sacar el código
del pueblo, nombre y número de vendedores. Ordena por nombre del pueblo.

![](Ex_6_70.png)

**Ex_71** Sacar el importe de la factura más cara de cada trimestre. La
información previa es la factura con la fecha y el importe. A partir de ahí tendremos
de calcular el máximo del importe para cada trimestre (no será necesario sacar cuál
factura es).

![](Ex_6_71.png)

**Ex_72** Sacar el nombre del vendedor, el número de facturas que ha vendido y el
porcentaje que supone sobre el total. Puede que en el momento de calcular
el porcentaje, el número resultante deba convertirse a numérico para que
da bien el resultado, ya que al realizar una operación con enteros, el resultado será
entero. Entonces deberíamos obligar a que el número tenga decimales
(**::NUMERIC**). Y la función de redondear es **ROUND**. Ordene por el nombre.

![](Ex_6_72.png)

**Ex_73** Sacar toda la información (con el importe) de la factura más cara.
Debe ser por medio de subconsultas. Vea que seguramente habrá 2
subconsultas. En la más interna calculamos el importe de las facturas. En la otra
calculamos el máximo. Y en la consulta principal, buscamos la factura que
coincide con ese máximo.

![](Ex_6_73.png)

**Ex_74 (voluntario)** Obtener el vendedor que ha vendido más unidades de cada
categoría, sin considerar en la categoría el valor nulo. Esta consulta la
podríamos considerar ya como muy avanzada.

![](Ex_6_74.png)

**Ex_75** Sacar el nombre de todos los clientes y vendedores implicados en alguna
venta del primer trimestre de 2015. Intentar sacar en una segunda columna el
texto **Vendedor** para los vendedores, y **Client** para los clientes. Ordenado por
nombre.

![](Ex_6_75.png)

**Ex_76a** Sacar mediante sentencias de operaciones de conjuntos los pueblos donde
tenemos algún vendedor o algún cliente. No queremos resultados repetidos, y lo queremos
ordenado por el nombre del pueblo.

![](Ex_6_76a.png)

Un total de **31 filas**

**Ex_76b** Modificar lo anterior para sacar los pueblos donde tenemos al mismo
tiempo vendedores y clientes

![](Ex_6_76b.png)

**Ex_76c** Modificar lo anterior para sacar los pueblos donde tenemos vendedores pero
no tenemos clientes

![](Ex_6_76c.png)


Licenciado bajo la [Licencia Creative Commons Reconocimiento NoComercial
SinObraDerivada 2.5](http://creativecommons.org/licenses/by-nc-nd/2.5/)

