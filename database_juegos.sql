-- Crear base de datos
CREATE DATABASE videojuegos_db;
USE videojuegos_db;

-- =====================
-- TABLA DESARROLLADORES
-- =====================
CREATE TABLE DESARROLLADORES (
  id_desarrollador INT PRIMARY KEY,
  nombre VARCHAR(100),
  sede VARCHAR(100)
);

-- =====================
-- TABLA VIDEOJUEGOS
-- =====================
CREATE TABLE VIDEOJUEGOS (
  id_juego INT PRIMARY KEY,
  titulo VARCHAR(150),
  fecha_lanzamiento DATE,
  precio DECIMAL(6,2),
  id_desarrollador INT,
  FOREIGN KEY (id_desarrollador) 
    REFERENCES DESARROLLADORES(id_desarrollador)
);

-- =====================
-- TABLA GENEROS
-- =====================
CREATE TABLE GENEROS (
  id_genero INT PRIMARY KEY,
  nombre_genero VARCHAR(50)
);

-- =====================
-- TABLA USUARIOS
-- =====================
CREATE TABLE USUARIOS (
  id_usuario INT PRIMARY KEY,
  nombre_usuario VARCHAR(100),
  email VARCHAR(100),
  nivel INT
);

-- =====================
-- TABLA PLATAFORMAS
-- =====================
CREATE TABLE PLATAFORMAS (
  id_plataforma INT PRIMARY KEY,
  nombre VARCHAR(50)
);

-- =====================
-- RELACIÓN N:M VIDEOJUEGOS - GENEROS
-- =====================
CREATE TABLE VIDEOJUEGO_GENERO (
  id_juego INT,
  id_genero INT,
  PRIMARY KEY (id_juego, id_genero),
  FOREIGN KEY (id_juego) REFERENCES VIDEOJUEGOS(id_juego),
  FOREIGN KEY (id_genero) REFERENCES GENEROS(id_genero)
);

-- =====================
-- RELACIÓN N:M USUARIOS - VIDEOJUEGOS
-- =====================
CREATE TABLE JUEGA (
  id_usuario INT,
  id_juego INT,
  PRIMARY KEY (id_usuario, id_juego),
  FOREIGN KEY (id_usuario) REFERENCES USUARIOS(id_usuario),
  FOREIGN KEY (id_juego) REFERENCES VIDEOJUEGOS(id_juego)
);

-- =====================
-- RELACIÓN N:M VIDEOJUEGOS - PLATAFORMAS
-- =====================
CREATE TABLE DISPONIBLE_EN (
  id_juego INT,
  id_plataforma INT,
  PRIMARY KEY (id_juego, id_plataforma),
  FOREIGN KEY (id_juego) REFERENCES VIDEOJUEGOS(id_juego),
  FOREIGN KEY (id_plataforma) REFERENCES PLATAFORMAS(id_plataforma)
);


-- =====================
-- DESARROLLADORES
-- =====================
INSERT INTO DESARROLLADORES VALUES
(1, 'Avalanche Software', 'USA'),
(2, 'FromSoftware', 'Japan'),
(3, 'CD Projekt Red', 'Poland'),
(4, 'Epic Games', 'USA'),
(5, 'Nintendo', 'Japan'),
(6, 'Rockstar Games', 'USA'),
(7, 'Ubisoft', 'France');

-- =====================
-- VIDEOJUEGOS
-- =====================
INSERT INTO VIDEOJUEGOS VALUES
(1, 'Hogwarts Legacy', '2023-02-10', 59.99, 1),
(2, 'Elden Ring', '2022-02-25', 49.99, 2),
(3, 'Cyberpunk 2077', '2020-12-10', 39.99, 3),
(4, 'Fortnite', '2017-07-21', 0.00, 4),
(5, 'The Legend of Zelda: Breath of the Wild', '2017-03-03', 59.99, 5),
(6, 'GTA V', '2013-09-17', 29.99, 6),
(7, 'Assassin''s Creed Valhalla', '2020-11-10', 49.99, 7),
(8, 'Rocket League', '2015-07-07', 0.00, 4);

-- =====================
-- GENEROS
-- =====================
INSERT INTO GENEROS VALUES
(1, 'RPG'),
(2, 'Acción'),
(3, 'Aventura'),
(4, 'Battle Royale'),
(5, 'Deportes'),
(6, 'Simulación');

-- =====================
-- USUARIOS
-- =====================
INSERT INTO USUARIOS VALUES
(1, 'DragonPlayer', 'dragon@gmail.com', 15),
(2, 'NoobMaster', 'noob@hotmail.com', 8),
(3, 'ProGamer', 'pro@game.com', 25),
(4, 'MagicFan', 'magic@hogwarts.com', 12),
(5, 'ZeldaFan', 'zelda@nintendo.com', 18),
(6, 'SpeedRunner', 'speed@fast.com', 22),
(7, 'CasualPlayer', 'casual@mail.com', 5),
(8, 'HardcoreGamer', 'hardcore@pro.com', 30);

-- =====================
-- PLATAFORMAS
-- =====================
INSERT INTO PLATAFORMAS VALUES
(1, 'PC'),
(2, 'PlayStation 5'),
(3, 'Xbox Series X'),
(4, 'Nintendo Switch'),
(5, 'PlayStation 4'),
(6, 'Xbox One');

-- =====================
-- VIDEOJUEGO_GENERO
-- =====================
INSERT INTO VIDEOJUEGO_GENERO VALUES
(1, 1),
(1, 3),
(2, 1),
(2, 2),
(3, 1),
(4, 4),
(5, 3),
(5, 1),
(6, 2),
(6, 6),
(7, 1),
(7, 3),
(8, 5);

-- =====================
-- JUEGA
-- =====================
INSERT INTO JUEGA VALUES
(1, 1),
(1, 2),
(2, 4),
(3, 2),
(3, 3),
(4, 1),
(5, 5),
(6, 6),
(7, 4),
(8, 2),
(8, 6),
(6, 8);

-- =====================
-- DISPONIBLE_EN
-- =====================
INSERT INTO DISPONIBLE_EN VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 1),
(2, 2),
(3, 1),
(4, 1),
(4, 2),
(4, 3),
(5, 4),
(6, 1),
(6, 5),
(6, 6),
(7, 2),
(7, 3),
(8, 1),
(8, 2),
(8, 3);
