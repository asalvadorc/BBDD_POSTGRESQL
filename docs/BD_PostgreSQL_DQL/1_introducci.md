# 1. Introducción


**SQL** es un lenguaje para organizar, gestionar y recuperar datos
almacenadas en una Base de Datos. El nombre "**SQL**" es una abreviatura de
_**Structured Query Language**_ (Lenguaje Estructurado de Consultas), y cómo
su nombre indica, es un lenguaje informático que se puede utilizar para
interacciones con una Base de Datos de tipo relacional.

SQL se utiliza para controlar todas las funciones que un SGBD proporciona a
sus usuarios, incluyendo:

  * **_Definición de datos_**. SQL permite a un usuario definir la estructura y organización de los datos almacenados y las relaciones existentes entre sí (claves externas).

  * **_Recuperación de datos_**. SQL permite a un usuario o programa de aplicación recuperar los datos almacenados de la base de datos y utilizarlos.

  * **_Manipulación de datos_**. SQL permite a un usuario oa un programa de aplicación actualizar la base de datos añadiendo nuevos datos, suprimiendo datos antiguos y modificando datos previamente almacenados.

  * **_Control de acceso_**. SQL puede ser utilizado para restringir la capacidad de un usuario para recuperar, añadir y modificar datos, protegiendo así los datos guardados frente a accesos no autorizados.

  * **_Compartición de datos_**. SQL se utiliza para coordinar la compartición de datos por parte de usuarios concurrentes, asegurando que no interfieren entre sí.

  * **_Integridad de datos_**. SQL define restricciones de integridad en la base de datos, protegiéndola contra corrupciones causadas por actualizaciones inconsistentes o por fallos del sistema.

SQL no es realmente un lenguaje informático completo tal como JAVA, C o Python.
SQL no dispone de la sentencia _IF_ para examinar condiciones, ni de las
sentencias _WHILE_ o _FOR_ para hacer bucles, por ejemplo. En lugar de eso,
SQL es un sublenguaje de base de datos, que consta de unas treinta sentencias
especializadas para tareas de gestión de bases de datos, pero **sólo 7 son
las principales sentencias**.

También se dice que es un lenguaje de **cuarta generación** porque en él se llama
qué información se quiere, sin especificar exactamente cómo se consigue
esta información.

También se dice que es un lenguaje orientado a **conjunto de registros**, ya que
una sentencia puede devolver un conjunto de registros. Esto es una gran ventaja con
los lenguajes de tercera generación, que sólo podían trabajar registro en
registro.

Dos son las formas de ejecutar sentencias SQL.

  * **De forma interactiva** : se escribe una sentencia SQL, y se ejecuta, devolviendo normalmente un conjunto de registros que se presentarán en forma tabular.  
  
  * **Dentro de un programa** escrito en otro lenguaje, que actuará como lenguaje anfitrión (y el SQL sería el lenguaje host, "_huesped_ "). 
  
SQL es el lenguaje estándar de acceso y manipulación de Bases de Datos de los
Sistemas Gestores de Bases de Datos Relacionales. A todos, absolutamente a todos
los SGBD Relacionales comerciales se puede acceder por SQL.


## DDL, DQL y DML

Como se ha comentado en la pregunta anterior, SQL nos permite definir, controlar y
acceder a una Base de Datos.

Haremos una distinción principal entre estas funciones, separando lo que son las
estructuras de las tablas y el contenido de las tablas. En este sentido
tendremos 3 subtipos de lenguajes:

  * **DDL** (_Data Definition Language_ o _Lenguaje de Definición de Datos_): permite definir, modificar o borrar las estructuras, como pueden ser tablas, vistas, índice, ... e incluso Bases de Datos. 
  Básicamente las sentencias son 3:   


  |    |    |     
---|---  
**CREATE** | para crear la estructura   
**ALTER** | para modificarla  
**DROP** | para borrarla  

* **DQL** (_Data Query Language_ o _Lenguaje de Consulta de Datos_): permite consultar datos de una base de datos.


**SELECT** | para consultar datos 
---|---

* **DML** (_Data Manipulation Language_ o _Lenguaje de Manipulación de Datos_): permite acceder al contenido de las estructuras, a los datos. Este acceso puede ser de dos tipos: para consultar o modificar los datos  

  |    |    |     
---|---  
**INSERT** | inserta nuevas filas  
**UPDATE** | modifica el contenido de filas ya existentes  
**DELETE** | borra filas  

El lenguaje SQL es más extenso que las sentencias anteriores, incorporando
también lo que se llama **DCL** (_Data Control Language_ o _Lenguaje de
Control de Datos_), que permite controlar los datos para dar permisos o
quitarlos sobre los datos, o controlar las transacciones, ..., pero de momento
nos conformaremos con las sentencias de DML y DDL, y estas últimas,
sobre todo, para definir tablas.

Licenciado bajo la [Licencia Creative Commons Reconocimiento NoComercial
CompartirIgual 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/)

