# 12. Orden con el que se ejecuta una sentencia SQL

Como hemos visto, y cómo veremos en la Parte II de este tema, la sentencia
**SELECT** es muy completa y muy potente. Puede hacer muchas cosas.

Quizás nos convenga saber en qué orden se ejecutan las cláusulas de las que se
compone, porque esto puede prevenirnos de posibles errores en el momento de
construir una sentencia de cierta envergadura. El orden de ejecución es el
siguiente:

  * Primero se cogen los datos desde la tabla o las tablas especificadas en el **FROM**. No podremos tratar información que no tengamos en ese origen de datos.
  * Después se eliminan las filas que no cumplen la condición del **WHERE** , en caso de que tengamos esta cláusula.
  * Después las filas resultantes se agrupan por el o por los campos especificados en el **GROUP BY** , en caso de que tengamos esta cláusula.
  * Una vez hechos los grupos, se eliminan los que no cumplan la condición del **HAVING** , en caso de que tengamos esta cláusula.
  * Después se selecciona la información especificada en las columnas, que en caso de haber alguna función de agregado actuará sobre los grupos que quedan (si teníamos cláusula GROUP BY) o sobre el total del origen de datos.
  * Posteriormente se ordena por los campos especificados en el **ORDER BY** , en caso de que tengamos esta cláusula.
  * Después se aplica los predicados **DISTINCT** en caso de tenerlo especificado.
  * Por último se toman tantas filas como indica la cláusula **LIMIT** , desplazadas tantas como indique **OFFSET** , si es que tenemos esta cláusula especificada.
  * Si tenemos cláusula**INTO** se procederá a crear una nueva tabla con el resultado anterior.

Tener claro este orden puede clarificarnos algo, y poder evitar algunos
errores. El error de la siguiente sentencia se había explicado ya en el apartado de la cláusula GROUP BY.

    SELECT nombre_c, COUNT(*), cod_m  
      FROM POBLACIONES  
      GROUP BY nombre_c

> nos dará el siguiente error:

![](T6_1_19_1.png)

> Pero si analizamos el orden en el que se ejecutan es lógico: cuando llegamos a mostrar
> los campos (entre ellos **cod_m**) los grupos ya se han realizado, y para valores
> iguales de **nombre_c**. En este momento no puedo sacar algo individual de
> cada grupo como es el código de municipio, porque ya se ha agrupado. En este
> momento sólo se puede intentar sacar el nombre de la comarca (ya que tiene el
> mismo valor para todo el grupo, es el campo por el que hemos agrupado), o alguna
> función de agregado, que calcula sobre el grupo. Y de eso nos intenta avisar
> PostgreSQL.

> Para solucionarlo podemos incluir el **cod_m** en el **GROUP BY** , y
> entonces haremos un grupo por cada comarca y población diferente, pero
> seguramente esto no nos valdrá de nada en este ejemplo, porque cada grupo
> sólo contendrá un elemento (un municipio), aunque en otros ejemplos sí
> que puede tener sentido. O si no era eso lo que pretendíamos, sencillamente levantamos
> el campo cod_m de la sentencia, y nos funcionará bien.

Otro ejemplo ilustrativo (que ya lo pusimos muy parecido en el apartado de la cláusula GROUP BY) puede ser el siguiente: podríamos intentar sacar la altura máxima de todos los
pueblos, y la población que tiene esa altura. Podríamos estar tentados de hacerlo
de esta forma:

    SELECT MAX(altura), nombre  
      FROM POBLACIONES;

> Nos dará el mismo error que antes, ya que cómo tenemos una función de agregado
> intentará hacer grupos, y como no tenemos cláusula GROUP BY toda la mesa será un
> grupo. Y podrá calcular el máximo sin problemas, pero no podrá sacar una
> cosa individual del grupo, como es el nombre. Y en este caso no se puede
> solucionar incluyendo el nombre en el GROUP BY, porque entonces haremos un grupo
> por cada población. Por el momento, antes de ver las subconsultas, sólo podemos
> resolver este ejemplo ordenando por la altura de forma descendente, y hacer
> **LIMITE 1**.

Podemos observar que si tenemos cláusula **GROUP BY** , a partir de ese momento
todos los campos que ponemos deben estar en el GROUP BY o en una función de agregado,
tanto en la condición del **HAVING**, como en las **columnas** como en el **ORDER
BY**. En cambio no será necesario para la cláusula **WHERE** , ya que ésta es
realiza antes que el **GROUP BY**



Licenciado bajo la [Licencia Creative Commons Reconocimiento NoComercial
CompartirIgual 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/)

