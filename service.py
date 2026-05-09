"""
Couche métier de CineMatch.
Fournit les méthodes utilisées par l'interface en ligne de commande.
"""

from models import Film, Humeur, Genre
from db import (
    init_db,
    add_humeur,
    get_all_humeurs,
    get_humeur_by_id,
    delete_humeur,
    add_genre,
    get_all_genres,
    get_genre_by_id,
    delete_genre,
    add_film,
    get_all_films,
    get_film_by_id,
    update_film,
    delete_film,
    search_films,
    stats_films_by_humeur,
    stats_films_by_genre,
    stats_films_by_annee,
)


class CineMatchService:
    def __init__(self, db_path: str = "cinematch.db", schema_path: str = "schema.sql"):
        self.db_path = db_path
        self.schema_path = schema_path

    def create_database(self) -> None:
        init_db(self.db_path, self.schema_path)

    def create_humeur(self, nom: str, description: str) -> int:
        humeur = Humeur(None, nom, description)
        return add_humeur(humeur.nom, humeur.description, self.db_path)

    def list_humeurs(self) -> list[Humeur]:
        return get_all_humeurs(self.db_path)

    def get_humeur(self, humeur_id: int) -> Humeur | None:
        return get_humeur_by_id(humeur_id, self.db_path)

    def remove_humeur(self, humeur_id: int) -> bool:
        return delete_humeur(humeur_id, self.db_path)

    def create_genre(self, nom: str) -> int:
        genre = Genre(None, nom)
        return add_genre(genre.nom, self.db_path)

    def list_genres(self) -> list[Genre]:
        return get_all_genres(self.db_path)

    def get_genre(self, genre_id: int) -> Genre | None:
        return get_genre_by_id(genre_id, self.db_path)

    def remove_genre(self, genre_id: int) -> bool:
        return delete_genre(genre_id, self.db_path)

    def create_film(
        self,
        titre: str,
        synopsis: str,
        annee: int,
        duree: int,
        note: float,
        affiche: str,
        id_humeur: int,
        id_genre: int,
    ) -> int:
        if self.get_humeur(id_humeur) is None:
            raise ValueError("L'humeur sélectionnée n'existe pas.")
        if self.get_genre(id_genre) is None:
            raise ValueError("Le genre sélectionné n'existe pas.")

        film = Film(
            None,
            titre,
            synopsis,
            annee,
            duree,
            note,
            affiche,
            id_humeur,
            id_genre,
        )

        return add_film(
            film.titre,
            film.synopsis,
            film.annee,
            film.duree,
            film.note,
            film.affiche,
            film.id_humeur,
            film.id_genre,
            self.db_path,
        )

    def list_films(self) -> list[dict]:
        return get_all_films(self.db_path)

    def get_film(self, film_id: int):
        return get_film_by_id(film_id, self.db_path)
    
    def modify_film(
        self,
        film_id: int,
        titre: str,
        synopsis: str,
        annee: int,
        duree: int,
        note: float,
        affiche: str,
        id_humeur: int,
        id_genre: int,
    ) -> bool:
        if self.get_film(film_id) is None:
            return False

        if self.get_humeur(id_humeur) is None:
            raise ValueError("L'humeur sélectionnée n'existe pas.")

        if self.get_genre(id_genre) is None:
            raise ValueError("Le genre sélectionné n'existe pas.")

        film = Film(
            film_id,
            titre,
            synopsis,
            annee,
            duree,
            note,
            affiche,
            id_humeur,
            id_genre,
        )

        return update_film(
            film.id_film,
            film.titre,
            film.synopsis,
            film.annee,
            film.duree,
            film.note,
            film.affiche,
            film.id_humeur,
            film.id_genre,
            self.db_path,
        )

    def remove_film(self, film_id: int) -> bool:
        return delete_film(film_id, self.db_path)

    def find_films(
        self,
        titre: str = "",
        genre: str = "",
        annee: int | None = None,
        humeur_id: int | None = None,
        genre_id: int | None = None,
    ) -> list[dict]:
        return search_films(titre, genre, annee, humeur_id, genre_id, self.db_path)

    def get_stats_by_humeur(self) -> list[dict]:
        return stats_films_by_humeur(self.db_path)

    def get_stats_by_genre(self) -> list[dict]:
        return stats_films_by_genre(self.db_path)

    def get_stats_by_annee(self) -> list[dict]:
        return stats_films_by_annee(self.db_path)
