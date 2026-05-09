"""
Modèles de données pour CineMatch.
Contient les classes utilisées par l'application en ligne de commande.
"""

from dataclasses import dataclass


@dataclass
class Humeur:
    id_humeur: int | None
    nom: str
    description: str

    def __post_init__(self):
        if not self.nom.strip():
            raise ValueError("Le nom de l'humeur ne peut pas être vide.")

    def __str__(self) -> str:
        return f"[{self.id_humeur}] {self.nom} - {self.description}"


@dataclass
class Genre:
    id_genre: int | None
    nom: str

    def __post_init__(self):
        if not self.nom.strip():
            raise ValueError("Le nom du genre ne peut pas être vide.")

    def __str__(self) -> str:
        return f"[{self.id_genre}] {self.nom}"


@dataclass
class Film:
    id_film: int | None
    titre: str
    synopsis: str
    annee: int
    duree: int
    note: float
    affiche: str
    id_humeur: int
    id_genre: int

    def __post_init__(self):
        if not self.titre.strip():
            raise ValueError("Le titre ne peut pas être vide.")
        if self.annee < 1888:
            raise ValueError("L'année est invalide.")
        if self.duree <= 0:
            raise ValueError("La durée doit être positive.")
        if self.note < 0 or self.note > 10:
            raise ValueError("La note doit être comprise entre 0 et 10.")
        if self.id_humeur <= 0:
            raise ValueError("L'identifiant de l'humeur doit être positif.")
        if self.id_genre <= 0:
            raise ValueError("L'identifiant du genre doit être positif.")

    def __str__(self) -> str:
        return (
            f"[{self.id_film}] {self.titre} ({self.annee}) | "
            f"{self.duree} min | Note : {self.note}/10 | "
            f"ID humeur : {self.id_humeur} | ID genre : {self.id_genre}"
        )
