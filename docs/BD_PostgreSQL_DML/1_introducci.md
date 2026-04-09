# **1. Introducción**

Servirá para introducir nuevas filas en una determinada mesa. Hay dos
variantes de esta sentencia. La primera servirá para introducir nuevas filas
proporcionándole los datos, es decir, indicando expresamente los nuevos valores
de los campos. La otra podría servir para introducir nuevas filas de forma más
masiva, cogiendo los datos de las tablas ya existentes por medio de una sentencia
SELECT.

Las sentencias de **DML** (Data Manipulation Language) son aquellas que nos deben permitir alterar los datos, es decir, la estructura de las tablas quedará intancta, y sólo se modificará
su contenido: 


  * **INSERT** , para introducir filas nuevas en la tabla.
  

  * **DELETE** , para borrar filas enteras de la tabla.
  

  * **UPDATE** , para modificar el contenido de una o más filas ya existentes.


Durante toda esta parte de SQL realizaremos consultas para modificar los datos de las tablas.

No nos conviene en absoluto trabajar sobre la Base de Datos **geo** ni sobre
**factura** , ya que lo que haríamos sería "boicotearnos" entre nosotros.
Trabajaremos con dos Bases de Datos nuevos:

- **pruebas**: servirá para realizar pruebas, como su propio nombre indica. Todos los ejemplos del tema los realizaremos en esta BD.
- **factura_local**: tendrá una Base de Datos para cada uno en local. Es donde tendrá que trabajar los ejercicios.

!!!Warning "IMPORTANTE"
    Le recomiendo que se cree otra conexión para cada una de las Bases de Datos anteriores. De esta manera, seguramente tendrá tres conexiones: la de **postgres_local** , la de **factura_local** y la de **pruebas**, además de las conexiones al servidor en la nube, **geo** y **factura**.


Licenciado bajo la [Licencia Creative Commons Reconocimiento NoComercial
CompartirIgual 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/)

