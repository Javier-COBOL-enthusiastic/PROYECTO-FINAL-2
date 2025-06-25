CREATE DATABASE IF NOT EXISTS tournament_system CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE tournament_system;

CREATE TABLE players (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    points INT UNSIGNED DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE teams (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE team_members (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    team_id INT UNSIGNED NOT NULL,
    player_id INT UNSIGNED NOT NULL,
    is_leader BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (team_id, player_id),
    FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE
);

-- Tabla de deportes y videojuegos
CREATE TABLE sports (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    category ENUM('Sport', 'VideoGame', 'Esport') NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE tournaments (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    sport_id INT UNSIGNED NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status ENUM('Pending', 'Started', 'Finished', 'Cancelled') NOT NULL DEFAULT 'Pending',
    tournament_type ENUM('Individual', 'Team') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (sport_id) REFERENCES sports(id) ON DELETE RESTRICT,
    CHECK (start_date <= end_date)
);

CREATE TABLE tournament_participants (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    tournament_id INT UNSIGNED NOT NULL,
    participant_type ENUM('Player', 'Team') NOT NULL,
    player_id INT UNSIGNED NULL,
    team_id INT UNSIGNED NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tournament_id) REFERENCES tournaments(id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE CASCADE,
    CHECK (
        (participant_type = 'Player' AND player_id IS NOT NULL AND team_id IS NULL) OR
        (participant_type = 'Team' AND team_id IS NOT NULL AND player_id IS NULL)
    )
);

CREATE TABLE tournament_rounds (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    tournament_id INT UNSIGNED NOT NULL,
    round_number INT UNSIGNED NOT NULL,
    status ENUM('Pending', 'In_Progress', 'Completed') NOT NULL DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (tournament_id) REFERENCES tournaments(id) ON DELETE CASCADE,
    UNIQUE (tournament_id, round_number)
);

CREATE TABLE matches (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    tournament_id INT UNSIGNED NOT NULL,
    round_id INT UNSIGNED NOT NULL,
    match_number INT UNSIGNED NOT NULL,
    home_participant_type ENUM('Player', 'Team') NOT NULL,
    home_participant_id INT UNSIGNED NOT NULL,
    away_participant_type ENUM('Player', 'Team') NOT NULL,
    away_participant_id INT UNSIGNED NOT NULL,
    winner_type ENUM('Player', 'Team') NULL,
    winner_id INT UNSIGNED NULL,
    is_unbalanced BOOLEAN DEFAULT FALSE,
    status ENUM('Pending', 'In_Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (tournament_id) REFERENCES tournaments(id) ON DELETE CASCADE,
    FOREIGN KEY (round_id) REFERENCES tournament_rounds(id) ON DELETE CASCADE,
    UNIQUE (tournament_id, round_id, match_number)
);

-- Índices para mejorar el rendimiento
CREATE INDEX idx_tournaments_status ON tournaments(status);
CREATE INDEX idx_tournaments_dates ON tournaments(start_date, end_date);
CREATE INDEX idx_tournaments_sport ON tournaments(sport_id);
CREATE INDEX idx_matches_tournament_round ON matches(tournament_id, round_id);
CREATE INDEX idx_matches_status ON matches(status);
CREATE INDEX idx_participants_tournament ON tournament_participants(tournament_id);
CREATE INDEX idx_rounds_tournament ON tournament_rounds(tournament_id);
CREATE INDEX idx_sports_category ON sports(category);
CREATE INDEX idx_sports_active ON sports(is_active);

-- Insertar deportes y videojuegos populares
INSERT INTO sports (name, category, description) VALUES
('Fútbol', 'Sport', 'El deporte más popular del mundo, jugado entre dos equipos de 11 jugadores'),
('Baloncesto', 'Sport', 'Deporte de equipo donde se anota encestando una pelota en un aro'),
('Tenis', 'Sport', 'Deporte de raqueta jugado individualmente o en parejas'),
('Voleibol', 'Sport', 'Deporte de equipo donde se golpea una pelota por encima de una red'),
('Béisbol', 'Sport', 'Deporte de bate y pelota con 9 jugadores por equipo'),
('Hockey', 'Sport', 'Deporte de equipo jugado con palos y un disco o pelota'),
('Rugby', 'Sport', 'Deporte de contacto físico jugado con una pelota ovalada'),
('Cricket', 'Sport', 'Deporte de bate y pelota popular en países de la Commonwealth'),
('Golf', 'Sport', 'Deporte individual donde se golpea una pelota hacia un hoyo'),
('Boxeo', 'Sport', 'Deporte de combate donde dos oponentes se enfrentan con guantes'),
('MMA', 'Sport', 'Artes marciales mixtas, combate cuerpo a cuerpo'),
('Atletismo', 'Sport', 'Conjunto de disciplinas deportivas de pista y campo'),
('Natación', 'Sport', 'Deporte acuático individual o por relevos'),
('Ciclismo', 'Sport', 'Deporte que se practica en bicicleta'),
('Ping Pong', 'Sport', 'Tenis de mesa, deporte de raqueta en mesa pequeña'),
('League of Legends', 'VideoGame', 'MOBA multijugador donde equipos de 5 luchan por destruir la base enemiga'),
('Counter-Strike 2', 'VideoGame', 'FPS táctico donde terroristas y contra-terroristas se enfrentan'),
('Dota 2', 'VideoGame', 'MOBA complejo con más de 100 héroes jugables'),
('Valorant', 'VideoGame', 'FPS táctico 5v5 con agentes con habilidades únicas'),
('Overwatch 2', 'VideoGame', 'FPS de equipos con héroes con roles específicos'),
('Rocket League', 'VideoGame', 'Fútbol con coches, combinación única de deporte y conducción'),
('FIFA 24', 'VideoGame', 'Simulador de fútbol con licencias oficiales'),
('NBA 2K24', 'VideoGame', 'Simulador de baloncesto con modo carrera y multijugador'),
('Call of Duty: Warzone', 'VideoGame', 'Battle Royale FPS con 150 jugadores'),
('Fortnite', 'VideoGame', 'Battle Royale con construcción y eventos especiales'),
('PUBG', 'VideoGame', 'Battle Royale realista con 100 jugadores'),
('Apex Legends', 'VideoGame', 'Battle Royale con héroes y habilidades únicas'),
('Rainbow Six Siege', 'VideoGame', 'FPS táctico de asedio con operadores especializados'),
('Hearthstone', 'VideoGame', 'CCG digital con cartas del universo Warcraft'),
('Magic: The Gathering Arena', 'VideoGame', 'CCG digital basado en el juego de cartas físico'),
('Pokémon GO', 'VideoGame', 'Juego de realidad aumentada para capturar Pokémon'),
('Minecraft', 'VideoGame', 'Juego de construcción y supervivencia en mundo abierto'),
('Among Us', 'VideoGame', 'Juego de deducción social multijugador'),
('Fall Guys', 'VideoGame', 'Battle Royale de obstáculos con personajes adorables'),
('Genshin Impact', 'VideoGame', 'RPG de acción de mundo abierto con elementos anime');