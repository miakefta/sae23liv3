"""
Insère des données de test dans la base CineMatch.
"""

from service import CineMatchService


def main():
    service = CineMatchService()

    humeur_rire = service.create_humeur("Drôle", "Pour les utilisateurs qui veulent rire.")
    humeur_action = service.create_humeur("Adrénaline", "Pour les utilisateurs qui veulent de l'action et de la tension.")
    humeur_detente = service.create_humeur("Détente", "Pour les utilisateurs qui veulent un film calme.")
    humeur_reflexion = service.create_humeur("Réflexion", "Pour les utilisateurs qui veulent réfléchir.")

    genre_comedie = service.create_genre("Comédie")
    genre_drame = service.create_genre("Drame")
    genre_scifi = service.create_genre("Science-fiction")
    genre_romance = service.create_genre("Romance")
    genre_action = service.create_genre("Action")
    genre_musical = service.create_genre("Musicale")

    service.create_film(
        "Intouchables",
        "L'amitié entre un aristocrate et son aide à domicile.",
        2011,
        112,
        8.5,
        "intouchables.jpg",
        humeur_rire,
        genre_comedie,
    )

    service.create_film(
        "Inception",
        "Un voleur entre dans les rêves pour voler des secrets.",
        2010,
        148,
        8.8,
        "inception.jpg",
        humeur_action,
        genre_scifi,
    )

    service.create_film(
        "La La Land",
        "Une histoire d'amour entre une actrice et un musicien.",
        2016,
        128,
        8.0,
        "lalaland.jpg",
        humeur_detente,
        genre_musical,
    )

    service.create_film(
        "Interstellar",
        "Une équipe traverse l'espace pour sauver l'humanité.",
        2014,
        169,
        8.7,
        "interstellar.jpg",
        humeur_reflexion,
        genre_scifi,
    )

    service.create_film(
        "Mad Max: Fury Road",
        "Une course-poursuite à grande vitesse dans un désert post-apocalyptique.",
        2015,
        120,
        8.1,
        "madmax.jpg",
        humeur_action,
        genre_action,
    )

    print("Données de test insérées avec succès.")


if __name__ == "__main__":
    main()
