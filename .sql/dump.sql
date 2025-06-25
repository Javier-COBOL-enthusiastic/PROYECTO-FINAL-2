
CREATE DATABASE IF NOT EXISTS tournament_system CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE tournament_system;

CREATE TABLE players (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE teams (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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

CREATE UNIQUE INDEX unique_team_leader ON team_members(team_id)
WHERE is_leader = TRUE;

CREATE TABLE tournaments (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    status ENUM('Pending', 'Started', 'Finished') NOT NULL DEFAULT 'Pending',
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    team_a_id INT UNSIGNED NOT NULL,
    team_b_id INT UNSIGNED NOT NULL,
    team_a_score INT UNSIGNED DEFAULT 0,
    team_b_score INT UNSIGNED DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (team_a_id) REFERENCES teams(id) ON DELETE RESTRICT,
    FOREIGN KEY (team_b_id) REFERENCES teams(id) ON DELETE RESTRICT,
    CHECK (start_date <= end_date),
    CHECK (team_a_id <> team_b_id)
);
