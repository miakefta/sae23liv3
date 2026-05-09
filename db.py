"""
Couche d'accès à la base de données pour CineMatch.
Gère la création SQLite et les opérations CRUD.
"""

import sqlite3
from pathlib import Path
from models import Film, Humeur, Genre


DEFAULT_DB_PATH = "cinematch.db"
DEFAULT_SCHEMA_PATH = "schema.sql"


def get_connection(db_path: str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(db_path: str = DEFAULT_DB_PATH, schema_path: str = DEFAULT_SCHEMA_PATH) -> None:
    if not Path(schema_path).exists():
        raise FileNotFoundError(f"Fichier de schéma introuvable : {schema_path}")

    with open(schema_path, "r", encoding="utf-8") as file:
        sql_script = file.read()

    conn = get_connection(db_path)
    conn.executescript(sql_script)
    conn.commit()
    conn.close()


# ============================================================
# CRUD HUMEUR
# ============================================================

def add_humeur(nom: str, description: str, db_path: str = DEFAULT_DB_PATH) -> int:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO humeur (nom, description) VALUES (?, ?)",
        (nom, description)
    )
    conn.commit()
    humeur_id = cursor.lastrowid
    conn.close()
    return humeur_id


def get_all_humeurs(db_path: str = DEFAULT_DB_PATH) -> list[Humeur]:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM humeur ORDER BY nom ASC")
    rows = cursor.fetchall()
    conn.close()

    return [Humeur(row["id_humeur"], row["nom"], row["description"]) for row in rows]


def get_humeur_by_id(humeur_id: int, db_path: str = DEFAULT_DB_PATH) -> Humeur | None:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM humeur WHERE id_humeur = ?", (humeur_id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None
    return Humeur(row["id_humeur"], row["nom"], row["description"])


def delete_humeur(humeur_id: int, db_path: str = DEFAULT_DB_PATH) -> bool:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) AS total FROM film WHERE id_humeur = ?", (humeur_id,))
    linked_films = cursor.fetchone()["total"]

    if linked_films > 0:
        conn.close()
        return False

    cursor.execute("DELETE FROM humeur WHERE id_humeur = ?", (humeur_id,))
    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return deleted


# ============================================================
# CRUD GENRE
# ============================================================

def add_genre(nom: str, db_path: str = DEFAULT_DB_PATH) -> int:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO genre (nom) VALUES (?)", (nom,))
    conn.commit()
    genre_id = cursor.lastrowid
    conn.close()
    return genre_id


def get_all_genres(db_path: str = DEFAULT_DB_PATH) -> list[Genre]:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM genre ORDER BY nom ASC")
    rows = cursor.fetchall()
    conn.close()

    return [Genre(row["id_genre"], row["nom"]) for row in rows]


def get_genre_by_id(genre_id: int, db_path: str = DEFAULT_DB_PATH) -> Genre | None:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM genre WHERE id_genre = ?", (genre_id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None
    return Genre(row["id_genre"], row["nom"])


def delete_genre(genre_id: int, db_path: str = DEFAULT_DB_PATH) -> bool:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) AS total FROM film WHERE id_genre = ?", (genre_id,))
    linked_films = cursor.fetchone()["total"]

    if linked_films > 0:
        conn.close()
        return False

    cursor.execute("DELETE FROM genre WHERE id_genre = ?", (genre_id,))
    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return deleted


# ============================================================
# CRUD FILM
# ============================================================

def add_film(
    titre: str,
    synopsis: str,
    annee: int,
    duree: int,
    note: float,
    affiche: str,
    id_humeur: int,
    id_genre: int,
    db_path: str = DEFAULT_DB_PATH,
) -> int:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO film (titre, synopsis, annee, duree, note, affiche, id_humeur, id_genre)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (titre, synopsis, annee, duree, note, affiche, id_humeur, id_genre),
    )
    conn.commit()
    film_id = cursor.lastrowid
    conn.close()
    return film_id


def get_all_films(db_path: str = DEFAULT_DB_PATH) -> list[dict]:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT f.*, h.nom AS humeur_nom, g.nom AS genre_nom
        FROM film f
        JOIN humeur h ON f.id_humeur = h.id_humeur
        JOIN genre g ON f.id_genre = g.id_genre
        ORDER BY f.titre ASC
        """
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_film_by_id(film_id: int, db_path: str = DEFAULT_DB_PATH) -> Film | None:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM film WHERE id_film = ?", (film_id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return Film(
        row["id_film"],
        row["titre"],
        row["synopsis"],
        row["annee"],
        row["duree"],
        row["note"],
        row["affiche"],
        row["id_humeur"],
        row["id_genre"],
    )

def update_film(
    film_id: int,
    titre: str,
    synopsis: str,
    annee: int,
    duree: int,
    note: float,
    affiche: str,
    id_humeur: int,
    id_genre: int,
    db_path: str = DEFAULT_DB_PATH,
) -> bool:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE film
        SET titre = ?, synopsis = ?, annee = ?, duree = ?, note = ?, affiche = ?, id_humeur = ?, id_genre = ?
        WHERE id_film = ?
        """,
        (titre, synopsis, annee, duree, note, affiche, id_humeur, id_genre, film_id),
    )
    updated = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return updated

def delete_film(film_id: int, db_path: str = DEFAULT_DB_PATH) -> bool:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM film WHERE id_film = ?", (film_id,))
    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return deleted


def search_films(
    titre: str = "",
    genre: str = "",
    annee: int | None = None,
    humeur_id: int | None = None,
    genre_id: int | None = None,
    db_path: str = DEFAULT_DB_PATH,
) -> list[dict]:
    conn = get_connection(db_path)
    cursor = conn.cursor()

    query = """
        SELECT f.*, h.nom AS humeur_nom, g.nom AS genre_nom
        FROM film f
        JOIN humeur h ON f.id_humeur = h.id_humeur
        JOIN genre g ON f.id_genre = g.id_genre
        WHERE 1=1
    """
    params = []

    if titre.strip():
        query += " AND f.titre LIKE ?"
        params.append(f"%{titre.strip()}%")

    if genre.strip():
        query += " AND g.nom LIKE ?"
        params.append(f"%{genre.strip()}%")

    if annee is not None:
        query += " AND f.annee = ?"
        params.append(annee)

    if humeur_id is not None:
        query += " AND f.id_humeur = ?"
        params.append(humeur_id)

    if genre_id is not None:
        query += " AND f.id_genre = ?"
        params.append(genre_id)

    query += " ORDER BY f.titre ASC"

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


# ============================================================
# STATISTIQUES
# ============================================================

def stats_films_by_humeur(db_path: str = DEFAULT_DB_PATH) -> list[dict]:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT h.nom AS humeur, COUNT(f.id_film) AS total
        FROM humeur h
        LEFT JOIN film f ON h.id_humeur = f.id_humeur
        GROUP BY h.id_humeur, h.nom
        ORDER BY total DESC, h.nom ASC
        """
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def stats_films_by_genre(db_path: str = DEFAULT_DB_PATH) -> list[dict]:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT g.nom AS genre, COUNT(f.id_film) AS total
        FROM genre g
        LEFT JOIN film f ON g.id_genre = f.id_genre
        GROUP BY g.id_genre, g.nom
        ORDER BY total DESC, g.nom ASC
        """
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def stats_films_by_annee(db_path: str = DEFAULT_DB_PATH) -> list[dict]:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT annee, COUNT(*) AS total
        FROM film
        GROUP BY annee
        ORDER BY annee ASC
        """
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
