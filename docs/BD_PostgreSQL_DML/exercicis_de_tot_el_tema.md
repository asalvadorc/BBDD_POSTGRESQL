# 2. Consultas de actualización (DML)

Como ya se ha comentado en la introducción, y por no interferir entre nosotros, cada uno se conectará a su Base de Datos **factura_local**.

Ejercicios de todo el tema

Como ya se ha comentado en la introducción, y por no interferir entre nosotros, cada uno se conectará a su Base de Datos **factura_local**.


El esquema Entidad-Relación y el esquema relacional es el siguiente:

![](factura.png)

En la Base de Datos llamada **factura_local**:

**Ex_1** - Insertar en la tabla **CATEGORÍA** las siguientes filas:

**cod_cas** | **descripcion**  
---|---  
BjcOlimpia | Componentes Bjc Seria Olimpia  
Legrand | Componentes marca Legrand  
IntMagn | Interruptor Magnetotérmico  
Niessen | Componentes Niesen Serie Lisa  
  
**Ex_2** - Insertar los siguientes artículos.

**cod_art** | **descrip** | **precio** | **stock** | **stock_min** | **cod_cas**  
---|---|---|---|---|---  
B10028B | Cruzamiento Bjc Serie Olimpia | 4.38 | 2 | 1 | BjcOlimpia  
B10200B | Cruzamiento Bjc Olimpia Cono Visor | 0.88 | 29 |  | BjcOlimpia  
L16550 | Cartucho Fusible Legrand T2 250 A | 5.89 | 1 | 1 | Legrand  
L16555 | Cartucho Fusible Legrand T2 315 A | 5.89 | 3 | 3 | Legrand  
IM2P10L | Interruptor Magnetotermico 2p, 4 | 14.84 | 2 | 1 | IntMagn  
N8008BA | Base Tt Lateral Niessen Trazo Bla | 4.38 | 6 | 6 | Niessen  
  
**Ex_3** - Insertar en la tabla **CLIENTE** tres filas con los siguientes datos

- **pruebas**: servirá para realizar pruebas, como su propio nombre indica. Todos los ejemplos del tema los realizaremos en esta BD.
- **factura_local**: tendrá una Base de Datos para cada uno en local. Es donde tendrá que trabajar los ejercicios.

**num_f** | **fecha** | **cod_cli** | **cod_ven** | **iva** | **dto**  
---|---|---|---|---|---  
6535 | 2015-01-01 | 306 |  | 21 | 10  

**num_f** | **num_l** | **cod_art** | **cuánto** | **precio** | **dto**  
---|---|---|---|---|---  
6535 | 1 | L16555 | 2 | 5.89 | 25  
  
**Ex_5** - Insertar la siguiente factura (esta tiene más de una línea de factura).

**num_f** | **fecha** | **cod_cli** | **cod_ven** | **iva** | **dto**  
---|---|---|---|---|---  
6559 | 2015-02-16 | 387 |  | 10 | 10  

**num_f** | **num_l** | **cod_art** | **cuánto** | **precio** | **dto**  
---|---|---|---|---|---  
6559 | 1 | IM2P10L | 3 | 14.84 |   
6559 | 2 | N8008BA | 6 | 4.38 | 20  
  
**Ex_6** - Borrar la factura **6559**. Comprobar que también se han borrado las
sus líneas de factura

**Ex_7** - Borrar los artículos de los que **no** tenemos**stock mínimo**.

**Ex_8** - Quitar todos los códigos postales de los clientes.

**Ex_9** - Subir el precio de los artículos de la categoría **BjcOlimpia** un **5%**
(el resultado será que el único artículo de esta categoría habrá pasado de un
precio de 4.38 a **4.60€**)


Licenciado bajo la [Licencia Creative Commons Reconocimiento NoComercial
CompartirIgual 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/)

