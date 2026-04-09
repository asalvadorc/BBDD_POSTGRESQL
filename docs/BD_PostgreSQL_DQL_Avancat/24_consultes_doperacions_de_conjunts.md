# 4 Consultas de operaciones de conjuntos

Agruparemos en este apartado las consultas que traten conjuntos de filas para
realizar operaciones de algebra de conjuntos: **unión** , **intersección** y
**diferencia** de conjuntos

Todas estas consultas juntan los resultados de dos o más consultas.

## 4.1 Unión

**<u>Sintaxi</u>**


    [TABLE] consulta1  
    UNION [ALL]  
    [TABLE] consulta2 ...

Cada una de las consultas puede ser una tabla (poniendo la palabra **TABLE**)
delante) o el nombre de una consulta ya guardada, aunque lo más habitual será
poner directamente la **sentencia SQL**.

Los requisitos son que las dos (o más) consultas devuelven el mismo número de
campos, y que sean sino del mismo tipo, sí de tipos compatibles

Al igual que en la unión de conjuntos, el resultado serán todas las filas de las
dos (o más) consultas individuales, pero sin repetir filas, es decir, si de
ambas consultas se obtienen filas iguales, éstas sólo saldrán una vez.
Lo anterior se puede evitar si ponemos el predicado ALL, y entonces sí saldrán
las filas repetidas.

Los nombres de los campos vendrán dados por la primera consulta.

Si queremos ordenar por algún campo, deberemos ponerlo al final de la última
consulta, pero refiriéndose en todo caso a los campos de la primera consulta (lo
podemos evitar poniendo el número de orden en el ORDER BY)

**<u>Ejemplos</u>**

  1) Queremos ver en un único resultado tanto el nombre de las comarcas como el nombre de las poblaciones, siempre con el nombre de la provincia al lado

    SELECT nombre_c, provincia  
      FROM COMARCAS  
    UNION  
    SELECT nombre, provincia  
      FROM COMARCAS INNER JOIN POBLACIONES USING (nombre_c)  
    ORDER BY nombre_c;

**Ex_55** Sacar el número de factura, fecha, código de cliente, total de la
factura (con el alias IMPORTE) y total de la factura aplicando descuentos
de artículo (con alias DESCUENTO_1), como en la consulta**Ex_33** , pero sin el
límite de las 10 líneas de factura. Ordena por número de factura.

## 4.2 Intersección

Es idéntica a la unión, pero poniendo la palabra **INTERSECT** , y servirá para
sacar únicamente las filas que están en ambas consultas.



**<u>Sintaxi</u>**

    [TABLE] consulta1  
    INTERSECT [ALL]  
    [TABLE] consulta2 ...

Al igual que antes, cada una de las consultas puede ser una mesa (poniendo la
palabra **TABLE** delante), y tenemos el requisito de que las dos (o más) consultas
devuelven el mismo número de campos, y de tipos compatibles.

En principio no saldrán filas repetidas, a menos que ponemos **ALL**

**Ejemplo**

  1) Dado que en el ejemplo de la unión habíamos visto que la fila Valencia Valencia salía en las 2 consultas, vamos a comprobar que aparece en la intersección:

    SELECT nombre_c, provincia  
      FROM COMARCAS  
    INTERSECT  
    SELECT nombre, provincia  
      FROM COMARCAS INNER JOIN POBLACIONES USING (nombre_c)  
    ORDER BY nombre_c;

## 4.3 Diferencia

Es idéntica a las anteriores, pero poniendo la palabra **EXCEPT** , y servirá para
a sacar las filas que están en la primera consulta pero que no están en la
segunda.

**<u>Sintaxi</u>**

    [TABLE] consulta1  
    EXCEPTO [ALL]  
    [TABLE] consulta2 ...

Al igual que antes, cada una de las consultas puede ser una mesa (poniendo la
palabra **TABLE** delante), y tenemos el requisito de que las dos (o más) consultas
devuelven el mismo número de campos, y de tipos compatibles.

En principio no saldrán filas repetidas, a menos que ponemos **ALL**

**<u>Ejemplo</u>**

  1) Aprovechamos el mismo ejemplo de antes para comprobar que con EXCEPT no saldrá la comarca Valencia, ya que existe una fila idéntica en la segunda consulta:

    SELECT nombre_c, provincia  
      FROM COMARCAS  
    EXCEPTO  
    SELECT nombre, provincia  
      FROM COMARCAS INNER JOIN POBLACIONES USING (nombre_c)  
    ORDER BY nombre_c;

## :pencil2: Ejercicios {: .ejercicios-header}

**Ex_75** Sacar el nombre de todos los clientes y vendedores implicados en alguna
venta del primer trimestre de 2015

**Ex_76a** Sacar mediante sentencias de operaciones de conjuntos los pueblos donde
tenemos algún vendedor o algún cliente. No queremos resultados repetidos, y lo queremos
ordenado por el nombre del pueblo.

**Ex_76b** Modificar lo anterior para sacar los pueblos donde tenemos al mismo
tiempo vendedores y clientes

**Ex_76c** Modificar lo anterior para sacar los pueblos donde tenemos vendedores pero
no tenemos clientes

Licenciado bajo la [Licencia Creative Commons Reconocimiento NoComercial
SinObraDerivada 2.5](http://creativecommons.org/licenses/by-nc-nd/2.5/)

