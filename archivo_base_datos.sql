DROP DATABASE IF EXISTS gestion_videojuegos;

create database gestion_videojuegos;

use gestion_videojuegos;

create table videojuegos(
id_juego int primary key auto_increment,
nombre_videojuego varchar(100)
);

#Tabla de fases del torneo#
create table fases_torneo(
id_fase int primary key auto_increment,
fase varchar(20) not null
);

insert into fases_torneo values
(1, "fase de grupos"),
(2, "octavos de final"),
(3, "cuartos de final"),
(4, "semifinal"),
(5, "final");

select * from fases_torneo;


#Tabla de torneos#
CREATE TABLE torneos (
id_torneo INT PRIMARY KEY AUTO_INCREMENT,
nombre_torneo VARCHAR(100) NOT NULL,
fecha_inicio DATE NOT NULL,
fecha_finalizacion DATE NOT NULL,
id_fase INT,
tipo_participante ENUM('equipo', 'jugador') NOT NULL,
CONSTRAINT fk_fase FOREIGN KEY (id_fase) REFERENCES fases_torneo(id_fase)
ON DELETE CASCADE
ON UPDATE CASCADE,
CONSTRAINT CH_validar_fecha_inicio CHECK (fecha_inicio < fecha_finalizacion)
);



#Tabla de niveles de equipos#
create table niveles_equipos (
id_nivel_equipo int primary key auto_increment,
nivel_equipo varchar(50) not null
);

#Tabla de niveles de equipos#
create table niveles_jugador (
id_nivel_jugador int primary key auto_increment,
nivel_jugador varchar(50) not null
);

#Tabla de equipos#
create table equipos (
id_equipo int primary key auto_increment,
nombre_equipo varchar(50) not null,
fecha_creacion DATE NOT NULL
);


#Tabla de jugadores#
CREATE TABLE jugadores (
id_jugador INT PRIMARY KEY AUTO_INCREMENT,
usuario VARCHAR(100) NOT NULL,
id_equipo INT,
CONSTRAINT u_equipo FOREIGN KEY (id_equipo) REFERENCES equipos(id_equipo)
ON DELETE CASCADE
ON UPDATE CASCADE,
CONSTRAINT u_usuario UNIQUE(usuario)
);



#Tabla que relaciona torneos, jugadores y equipos#
CREATE TABLE torneo_participantes (
  id_torneo_participante INT PRIMARY KEY AUTO_INCREMENT,
  id_torneo INT NOT NULL,
  id_equipo INT DEFAULT NULL,
  id_jugador INT DEFAULT NULL,
  CONSTRAINT fk_torneo FOREIGN KEY (id_torneo) REFERENCES torneos(id_torneo)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_equipo FOREIGN KEY (id_equipo) REFERENCES equipos(id_equipo)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_jugador FOREIGN KEY (id_jugador) REFERENCES jugadores(id_jugador)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CHECK (
    (id_equipo IS NOT NULL AND id_jugador IS NULL) OR
    (id_equipo IS NULL AND id_jugador IS NOT NULL)
  )
);

# Tabla para partidos
CREATE TABLE enfrentamientos (
  id_enfrentamiento INT PRIMARY KEY AUTO_INCREMENT,
  id_torneo INT NOT NULL,
  id_participante_local INT NOT NULL,
  id_participante_visitante INT NOT NULL,
  marcador_local INT DEFAULT NULL,
  marcador_visitante INT DEFAULT NULL,
  fecha_partido DATE NOT NULL,
  id_fase INT NOT NULL,
  CONSTRAINT fk_idtorneo FOREIGN KEY (id_torneo) REFERENCES torneos(id_torneo),
  CONSTRAINT fk_participante_local FOREIGN KEY (id_participante_local) REFERENCES torneo_participantes(id_torneo_participante),
  CONSTRAINT fk_participante_visitante FOREIGN KEY (id_participante_visitante) REFERENCES torneo_participantes(id_torneo_participante),
  CONSTRAINT fk_idfase FOREIGN KEY (id_fase) REFERENCES fases_torneo(id_fase),
  CHECK (id_participante_local <> id_participante_visitante)
);

