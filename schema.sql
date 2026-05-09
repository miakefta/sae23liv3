DROP TABLE IF EXISTS film;
DROP TABLE IF EXISTS genre;
DROP TABLE IF EXISTS humeur;

CREATE TABLE humeur (
    id_humeur INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL
);

CREATE TABLE genre (
    id_genre INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL UNIQUE
);

CREATE TABLE film (
    id_film INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    synopsis TEXT NOT NULL,
    annee INTEGER NOT NULL,
    duree INTEGER NOT NULL,
    note REAL NOT NULL,
    affiche TEXT NOT NULL,
    id_humeur INTEGER NOT NULL,
    id_genre INTEGER NOT NULL,
    FOREIGN KEY (id_humeur) REFERENCES humeur(id_humeur),
    FOREIGN KEY (id_genre) REFERENCES genre(id_genre)
);
