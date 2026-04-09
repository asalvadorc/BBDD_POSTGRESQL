---
title: "Bases de Datos"
---

A lo largo de esta tercera parte, en el conjunto de ejercicios de DDL, crearemos
toda la estructura de la Base de Datos **FACTURA** , pero para no interferir
cada uno con los demás compañeros, cada uno se conectará a su Base de Datos
**factura_local**.

El esquema Entidad-Relación y el esquema relacional que implementaremos será el
siguiente:

![](factura.png)


!!!note "Nota"
      Durante todos estos ejercicios de DDL puede ser muy conveniente tener abiertas
      ambas conexiones: la de **FACTURA** (para ir consultando) y la de
      **factura_local** (para ir creando y modificando).
      
**Ex_1** - Cree la tabla **CATEGORÍA** , con los mismos campos y del mismo
tipos que en la tabla CATEGORÍA de **FACTURA** , pero de momento sin clave
principal ni ninguna otra restricción. 

**Ex_2** - Cree la tabla **ARTÍCULO** , también sin restricciones.

**Ex_3** - Crear la tabla **PROVINCIA** , con la clave principal.

**Ex_4** - Crear la tabla **PUEBLO** , con la clave principal y la restricción que
el campo **cod_pro** es clave externa que apunta a PROVINCIA.

**Ex_5** - Crear la tabla **VENEDOR** , con la clave principal y la clave externa
en PUEBLO (de momento no definimos la clave externa a VENDEDOR, que es reflexiva).

**Ex_6** - Crear la tabla **CLIENTE** , con la clave principal y la clave externa a
PUEBLO

**Ex_7** - Crear la tabla **FACTURA** , con la clave principal y las claves
externas a CLIENTE y VENDEDOR. También debe exigir que **cod_cli** sea no nulo.

**Ex_8** - Crear la tabla **LINIA_FAC** , con la clave principal (observa que
está formada por 2 campos) pero de momento sin la clave externa que apunta a
ARTÍCULO. Además **cod_a** debe ser no nulo.

**Ex_9** - Añadir un campo a la tabla **VENEDOR** llamado **alias** de tipo
texto, que debe ser no nulo y único.

**Ex_10** - Borrar el campo anterior, **alies** , de la tabla **VENEDOR**.

**Ex_11** - Añadir la clave principal de **CATEGORÍA**.

**Ex_12** - En la tabla **ARTÍCULO** añadir la clave principal y la clave externa a
CATEGORÍA.

**Ex_13** - En la tabla **LINIA_FAC** añadir la clave externa que apunta a
FACTURA, **exigiendo que se borre en cascada** (si se borra una factura,
se borrarán automáticamente sus líneas de factura). Y también la clave
externa que apunta a ARTÍCULO (esta normal, es decir NO ACTION)

**Ex_14** - Añadir un índice llamado **i_nombre_cli** a la tabla **CLIENTE** por el campo
**nombre**.

**Ex_15** - Añadir un índice llamado**i_adr_ven** a la tabla **VENEDOR** para
que esté ordenado por **cp** (ascendente) y **dirección**(descendente).

**Ex_16** - Crear la vista **RESUM_FACTURA** , que nos dé el total del dinero
de la factura, el total después del descuento de artículos, y el total después
del descuento de la factura, tal y como teníamos en la consulta **6.56**. En
partir de ese momento podremos utilizar la vista para sacar éstos
resultados

**Ex 17** - Crear la vista RESUMEN_VENEDOR, donde aparezca información del nombre del vendedor, del número total de artículos vendidos y del importe total facturado.

**Ex 18** - Crear la vista RESUMEN_CATEGORIAS, donde aparezca información del nombre de la categoría, del número total de artículos vendidos y del importe total facturado.

**Ex 19** - Tenemos creada la mesa VENDEDOR y se desea que la clave principal sea una secuencia autonumérica personalizada. 
Observa la información actual en la tabla VENDEDOR de la BD factura y analiza qué secuencia se ha utilizado.

![](Ex_18.png)

* A continuación realiza la inserción de un registro en esta tabla teniendo en cuenta la secuencia creada, para comprobar que funciona.
* Finalmente elimina los objetos creados. 
* Escribe las sentencias en el orden adecuado

**Ex 20** - Queremos crear una nueva tabla CLIENTE2 y se quiere que la clave principal sea una secuencia personalizada autonumerica. 
Observa la información actual en la tabla CLIENTE de la BD factura y analiza qué secuencia debería utilizarse.

![](Ex_20.png)

* Debes tener en cuenta que al crear la tabla CLIENTE2 para que el campo cod_cli, por defecto siempre tome el siguiente valor de la secuencia definida anteriormente. 
* A continuación realiza la inserción de un registro en esta tabla teniendo en cuenta los cambios realizados en la base de datos. 
* Finalmente elimina los objetos creados. 
Escribe las sentencias en el orden adecuado.

**Ex 21** - En la tabla FACTURA2 se quiere que la clave principal sea una secuencia autonumérica en serie.

* Crea la tabla FACTURA2 para que el campo num_f utilice una secuencia en serie.
* Además debes tener en cuenta que el iva de la factura solo puede ser el 10 o el 21 y que el descuento la factura debe ser inferior a 50.
* A continuación realiza la inserción de un registro en esta tabla para comprobar que funciona.
* Finalmente elimina los objetos creados.
* Escribe las sentencias en el orden adecuado.

**Ex 22** - Crea la tabla ARTÍCULO2 teniendo en cuenta lo siguiente;

* Comprobar que el precio, stock y stock_min no es negativo
* Crear un tipo de datos para el estado de un artículo, que puede tomar los valores "Disponible", "Agotado" o "En espera".
* Crea un tipo de dato para registrar el código de barras EAN-13 de un artículo. Teniendo en cuenta que el código de barras EAN-13 se observan 3 partes:
  
    * País de procedencia: son los dos o tres primeros dígitos y, en el caso de España, este prefijo es el 84.
    * Código del producto: siguientes 9 o 10 dígitos.
    * Dígito de control: es un solo número, el último, y sirve para corroborar que el código es correcto.
  
* Comprobar que stock no puede ser inferior a stock _min (TIENES QUE DEFINIR UNA CONSTRAINTO)
* A continuación realiza la inserción de un registro en esta tabla para comprobar que funciona.
* Finalmente elimina los objetos creados.
* Escribe las sentencias en el orden adecuado.


<!--
**Ex_17** Insertar en la tabla **CATEGORÍA** las siguientes filas:

**cod_cas** | **descripcion**  
---|---  
BjcOlimpia | Componentes Bjc Seria Olimpia  
Legrand | Componentes marca Legrand  
IntMagn | Interruptor Magnetotérmico  
Niessen | Componentes Niesen Serie Lisa  
  
**Ex_18** Insertar los siguientes artículos.

**cod_art** | **descrip** | **precio** | **stock** | **stock_min** | **cod_cas**  
---|---|---|---|---|---  
B10028B | Cruzamiento Bjc Serie Olimpia | 4.38 | 2 | 1 | BjcOlimpia  
B10200B | Cruzamiento Bjc Olimpia Cono Visor | 0.88 | 29 |  | BjcOlimpia  
L16550 | Cartucho Fusible Legrand T2 250 A | 5.89 | 1 | 1 | Legrand  
L16555 | Cartucho Fusible Legrand T2 315 A | 5.89 | 3 | 3 | Legrand  
IM2P10L | Interruptor Magnetotermico 2p, 4 | 14.84 | 2 | 1 | IntMagn  
N8008BA | Base Tt Lateral Niessen Trazo Bla | 4.38 | 6 | 6 | Niessen  
  
**Ex_19** Insertar en la tabla **CLIENTE** tres filas con los siguientes datos

**cod_cli** | **nombre** | **dirección** | **cp** | **cod_pob**  
---|---|---|---|---  
303 | MIRAVET SALA, MARIA MERCEDES | URBANIZACION EL BALCO, 84-11 |  |   
306 | SAMPEDRO SIMO, MARIA MERCEDES | FINELLO, 161 | 12217 |   
387 | TUR MARTIN, MANUEL FRANCISCO | CALLE PEDRO VIRUELA, 108-8 | 12008 |   
  
**Ex_20** Insertar la siguiente factura:

**num_f** | **fecha** | **cod_cli** | **cod_ven** | **iva** | **dto**  
---|---|---|---|---|---  
6535 | 2015-01-01 | 306 |  | 21 | 10  

**num_f** | **num_l** | **cod_art** | **cuánto** | **precio** | **dto**  
---|---|---|---|---|---  
6535 | 1 | L16555 | 2 | 5.89 | 25  
  
**Ex_21** Insertar la siguiente factura (ésta tiene más de una línea de factura).

**num_f** | **fecha** | **cod_cli** | **cod_ven** | **iva** | **dto**  
---|---|---|---|---|---  
6559 | 2015-02-16 | 387 |  | 10 | 10  

**num_f** | **num_l** | **cod_art** | **cuánto** | **precio** | **dto**  
---|---|---|---|---|---  
6559 | 1 | IM2P10L | 3 | 14.84 |   
6559 | 2 | N8008BA | 6 | 4.38 | 20  
  
**Ex_22** Borrar la factura **6559**. Comprobar que también se han borrado las
sus líneas de factura

**Ex_23** Borrar los artículos de los que **no** tenemos**stock mínimo**.

**Ex_24** Quitar todos los códigos postales de los clientes.

**Ex_25** Subir el precio de los artículos de la categoría **BjcOlimpia** un **5%**
(el resultado será que el único artículo de esta categoría habrá pasado de un
precio de 4.38 a **4.60€**)
-->

Licenciado bajo la [Licencia Creative Commons Reconocimiento NoComercial
CompartirIgual 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/)

