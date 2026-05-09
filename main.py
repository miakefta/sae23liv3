"""
Interface CLI pour CineMatch.
"""

from service import CineMatchService

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

RESET = "\033[0m"
RED = "\033[91m"
CYAN = "\033[96m"
GREEN = "\033[92m"


def print_separator():
    print("\n" + "=" * 60)


# ============================================================
# AFFICHAGES SIMPLES
# ============================================================

def display_humeurs(service: CineMatchService):
    print(RED + "=" * 50 + RESET)
    print("--- LISTE DES HUMEURS ---")
    humeurs = service.list_humeurs()

    if not humeurs:
        print("Aucune humeur trouvée.")
        return

    for humeur in humeurs:
        print(humeur)


def display_genres(service: CineMatchService):
    print(RED + "=" * 50 + RESET)
    print("--- LISTE DES GENRES ---")
    genres = service.list_genres()

    if not genres:
        print("Aucun genre trouvé.")
        return

    for genre in genres:
        print(genre)


def display_films(service: CineMatchService):
    print(RED + "=" * 50 + RESET)
    print("--- LISTE DES FILMS ---")
    films = service.list_films()

    if not films:
        print("Aucun film trouvé.")
        return

    for film in films:
        print(
            f"[{film['id_film']}] {film['titre']} ({film['annee']}) | "
            f"{film['genre_nom']} | {film['duree']} min | "
            f"Note : {film['note']}/10 | Humeur : {film['humeur_nom']}"
        )


def display_database(service: CineMatchService):
    """
    Affiche le contenu complet de la base de données :
    table humeur, table genre, table film.
    """
    print(RED + "=" * 50 + RESET)
    print("CONTENU COMPLET DE LA BASE DE DONNÉES".center(50))
    print( RED + "=" * 50 + RESET)

    print("\n--- TABLE HUMEUR ---")
    humeurs = service.list_humeurs()
    if not humeurs:
        print("Aucune humeur.")
    else:
        for humeur in humeurs:
            print(humeur)

    print("\n--- TABLE GENRE ---")
    genres = service.list_genres()
    if not genres:
        print("Aucun genre.")
    else:
        for genre in genres:
            print(genre)

    print("\n--- TABLE FILM ---")
    films = service.list_films()
    if not films:
        print("Aucun film.")
    else:
        for film in films:
            print(
                f"[{film['id_film']}] {film['titre']} ({film['annee']}) | "
                f"{film['genre_nom']} | {film['duree']} min | "
                f"Note : {film['note']}/10 | Humeur : {film['humeur_nom']}"
            )


# ============================================================
# AJOUTS
# ============================================================

def add_humeur_cli(service: CineMatchService):
    print( RED + "=" * 50 + RESET)
    print("--- AJOUTER UNE HUMEUR ---")

    nom = input("Nom de l'humeur : ").strip()
    description = input("Description : ").strip()

    try:
        humeur_id = service.create_humeur(nom, description)
        print(f"Humeur ajoutée avec succès avec l'ID {humeur_id}.")
    except ValueError as e:
        print(f"Erreur : {e}")


def add_genre_cli(service: CineMatchService):
    print( RED + "=" * 50 + RESET)
    print("--- AJOUTER UN GENRE ---")

    nom = input("Nom du genre : ").strip()

    try:
        genre_id = service.create_genre(nom)
        print(f"Genre ajouté avec succès avec l'ID {genre_id}.")
    except ValueError as e:
        print(f"Erreur : {e}")


def add_film_cli(service: CineMatchService):
    print( RED + "=" * 50 + RESET)
    print("--- AJOUTER UN FILM ---")

    display_humeurs(service)
    display_genres(service)

    try:
        titre = input("Titre : ").strip()
        synopsis = input("Synopsis : ").strip()
        annee = int(input("Année : ").strip())
        duree = int(input("Durée (minutes) : ").strip())
        note = float(input("Note (de 0 à 10) : ").strip())
        affiche = input("Nom du fichier de l'affiche : ").strip()
        id_humeur = int(input("ID de l'humeur : ").strip())
        id_genre = int(input("ID du genre : ").strip())

        film_id = service.create_film(
            titre, synopsis, annee, duree, note, affiche, id_humeur, id_genre
        )
        print(f"Film ajouté avec succès avec l'ID {film_id}.")

    except ValueError as e:
        print(f"Erreur de saisie : {e}")

def update_film_cli(service: CineMatchService):
    print( RED + "=" * 50 + RESET)
    print("--- MODIFIER UN FILM ---")
    display_films(service)

    try:
        film_id = int(input("ID du film à modifier : ").strip())
        film = service.get_film(film_id)

        if film is None:
            print("Film introuvable.")
            return

        print("\nLaissez vide pour conserver l'ancienne valeur.")
        display_humeurs(service)
        display_genres(service)

        titre = input(f"Titre [{film.titre}] : ").strip()
        synopsis = input(f"Synopsis [{film.synopsis}] : ").strip()
        annee_input = input(f"Année [{film.annee}] : ").strip()
        duree_input = input(f"Durée [{film.duree}] : ").strip()
        note_input = input(f"Note [{film.note}] : ").strip()
        affiche = input(f"Affiche [{film.affiche}] : ").strip()
        humeur_input = input(f"ID humeur [{film.id_humeur}] : ").strip()
        genre_input = input(f"ID genre [{film.id_genre}] : ").strip()

        titre = titre if titre else film.titre
        synopsis = synopsis if synopsis else film.synopsis
        annee = int(annee_input) if annee_input else film.annee
        duree = int(duree_input) if duree_input else film.duree
        note = float(note_input) if note_input else film.note
        affiche = affiche if affiche else film.affiche
        id_humeur = int(humeur_input) if humeur_input else film.id_humeur
        id_genre = int(genre_input) if genre_input else film.id_genre

        updated = service.modify_film(
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

        if updated:
            print("Film modifié avec succès.")
        else:
            print("Modification impossible.")

    except ValueError as e:
        print(f"Erreur de saisie : {e}")


# ============================================================
# SUPPRESSIONS
# ============================================================

def delete_humeur_cli(service: CineMatchService):
    print( RED + "=" * 50 + RESET)
    print("--- SUPPRIMER UNE HUMEUR ---")
    display_humeurs(service)

    try:
        humeur_id = int(input("ID de l'humeur à supprimer : ").strip())
        deleted = service.remove_humeur(humeur_id)

        if deleted:
            print("Humeur supprimée avec succès.")
        else:
            print("Suppression impossible. Humeur introuvable ou encore liée à des films.")
    except ValueError:
        print("ID invalide.")


def delete_genre_cli(service: CineMatchService):
    print( RED + "=" * 50 + RESET)
    print("--- SUPPRIMER UN GENRE ---")
    display_genres(service)

    try:
        genre_id = int(input("ID du genre à supprimer : ").strip())
        deleted = service.remove_genre(genre_id)

        if deleted:
            print("Genre supprimé avec succès.")
        else:
            print("Suppression impossible. Genre introuvable ou encore lié à des films.")
    except ValueError:
        print("ID invalide.")


def delete_film_cli(service: CineMatchService):
    print(RED + "=" * 50 + RESET)
    print("--- SUPPRIMER UN FILM ---")
    display_films(service)

    try:
        film_id = int(input("ID du film à supprimer : ").strip())
        deleted = service.remove_film(film_id)

        if deleted:
            print("Film supprimé avec succès.")
        else:
            print("Film introuvable.")
    except ValueError:
        print("ID invalide.")


# ============================================================
# RECHERCHE
# ============================================================

def search_films_cli(service: CineMatchService):
    print(RED + "=" * 50 + RESET)
    print(RED + "=== RECHERCHER DES FILMS ===" + RESET)
    print("Laissez un champ vide si vous ne voulez pas l'utiliser.")

    titre = input("Le titre contient : ").strip()
    genre = input("Le genre contient : ").strip()
    annee_input = input("Année : ").strip()
    humeur_input = input("ID de l'humeur : ").strip()
    genre_id_input = input("ID du genre : ").strip()

    annee = int(annee_input) if annee_input else None
    humeur_id = int(humeur_input) if humeur_input else None
    genre_id = int(genre_id_input) if genre_id_input else None

    results = service.find_films(
        titre=titre,
        genre=genre,
        annee=annee,
        humeur_id=humeur_id,
        genre_id=genre_id,
    )

    print_separator()
    print(f"RÉSULTATS : {len(results)} film(s) trouvé(s)")

    if not results:
        print("Aucun résultat.")
        return

    for film in results:
        print(
            f"[{film['id_film']}] {film['titre']} ({film['annee']}) | "
            f"{film['genre_nom']} | Humeur : {film['humeur_nom']} | Note : {film['note']}/10"
        )

# ============================================================
# STATISTIQUES
# ============================================================

def graph_films_par_humeur(service: CineMatchService):
    """
    Graphique du nombre de films par humeur.
    """
    if plt is None:
        print("Matplotlib n'est pas installé. Impossible d'afficher le graphique.")
        return

    data = service.get_stats_by_humeur()

    if not data:
        print("Aucune donnée pour le graphique des humeurs.")
        return

    humeurs = []
    totals = []

    for row in data:
        humeurs.append(row["humeur"])
        totals.append(row["total"])

    plt.plot(humeurs, totals)
    plt.title("Nombre de films par humeur")
    plt.xlabel("Humeur")
    plt.ylabel("Nombre de films")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graph_films_par_humeur.png")
    plt.show()


def graph_films_par_genre(service: CineMatchService):
    """
    Graphique du nombre de films par genre.
    """
    if plt is None:
        print("Matplotlib n'est pas installé. Impossible d'afficher le graphique.")
        return

    data = service.get_stats_by_genre()

    if not data:
        print("Aucune donnée pour le graphique des genres.")
        return

    genres = []
    totals = []

    for row in data:
        genres.append(row["genre"])
        totals.append(row["total"])

    plt.plot(genres, totals)
    plt.title("Nombre de films par genre")
    plt.xlabel("Genre")
    plt.ylabel("Nombre de films")
    plt.grid(True)
    plt.savefig("graph_films_par_genre.png")
    plt.show()


def graph_films_par_annee(service: CineMatchService):
    """
    Graphique du nombre de films par année.
    """
    if plt is None:
        print("Matplotlib n'est pas installé. Impossible d'afficher le graphique.")
        return

    data = service.get_stats_by_annee()

    if not data:
        print("Aucune donnée pour le graphique des années.")
        return

    annees = []
    totals = []

    for row in data:
        annees.append(row["annee"])
        totals.append(row["total"])

    plt.plot(annees, totals)
    plt.title("Nombre de films par année")
    plt.xlabel("Année")
    plt.ylabel("Nombre de films")
    plt.grid(True)
    plt.savefig("graph_films_par_annee.png")
    plt.show()

def display_statistics(service: CineMatchService):
    print(RED + "=" * 50 + RESET)
    print(RED + "=== STATISTIQUES ===" + RESET)

    print("\nFilms par humeur :")
    for row in service.get_stats_by_humeur():
        print(f"- {row['humeur']} : {row['total']}")

    print("\nFilms par genre :")
    for row in service.get_stats_by_genre():
        print(f"- {row['genre']} : {row['total']}")

    print("\nFilms par année :")
    for row in service.get_stats_by_annee():
        print(f"- {row['annee']} : {row['total']}")

    print_separator()
    print("Ouverture des graphiques...")

    graph_films_par_humeur(service)
    graph_films_par_genre(service)
    graph_films_par_annee(service)

# ============================================================
# SOUS-MENUS
# ============================================================

def manage_humeurs_menu(service: CineMatchService):
    while True:
        print(RED + "=" * 50 + RESET)
        print(RED + "=== GESTION DES HUMEURS ===" + RESET)
        print("1. Afficher les humeurs")
        print("2. Ajouter une humeur")
        print("3. Supprimer une humeur")
        print("0. Retour")

        choice = input("Votre choix : ").strip()

        if choice == "1":
            display_humeurs(service)
        elif choice == "2":
            add_humeur_cli(service)
        elif choice == "3":
            delete_humeur_cli(service)
        elif choice == "0":
            break
        else:
            print("Choix invalide.")


def manage_genres_menu(service: CineMatchService):
    while True:
        print_separator()
        print(RED + "=== GESTION DES GENRES ===" + RESET)
        print("1. Afficher les genres")
        print("2. Ajouter un genre")
        print("3. Supprimer un genre")
        print("0. Retour")

        choice = input("Votre choix : ").strip()

        if choice == "1":
            display_genres(service)
        elif choice == "2":
            add_genre_cli(service)
        elif choice == "3":
            delete_genre_cli(service)
        elif choice == "0":
            break
        else:
            print("Choix invalide.")


def manage_films_menu(service: CineMatchService):
    while True:
        print(RED + "=" * 50 + RESET)
        print(RED + "=== GESTION DES FILMS ===" + RESET)
        print("1. Afficher les films")
        print("2. Ajouter un film")
        print("3. Modifier un film")
        print("4. Supprimer un film")
        print("0. Retour")

        choice = input("Votre choix : ").strip()

        if choice == "1":
            display_films(service)
        elif choice == "2":
            add_film_cli(service)
        elif choice == "3":
            update_film_cli(service)
        elif choice == "4":
            delete_film_cli(service)
        elif choice == "0":
            break
        else:
            print("Choix invalide.")


# ============================================================
# MENU PRINCIPAL
# ============================================================

def main():
    service = CineMatchService()

    while True:
        print( RED + "=" * 50 + RESET)
        print("CINÉMATCH - OUTIL D'ADMINISTRATION CLI".center(50))
        print( RED + "=" * 50 + RESET)
        print( RED + "\n=== MENU ===" + RESET)
        print("1. Créer / réinitialiser la base de données")
        print("2. Afficher la base de données")
        print("3. Gérer les humeurs")
        print("4. Gérer les genres")
        print("5. Gérer les films")
        print("6. Rechercher des films")
        print("7. Afficher les statistiques")
        print("0. Quitter")

        choice = input("Votre choix : ").strip()

        if choice == "1":
            try:
                service.create_database()
                print("Base de données créée avec succès.")
            except ValueError as e:
                print(f"Erreur : {e}")

        elif choice == "2":
            display_database(service)
            print()

        elif choice == "3":
            manage_humeurs_menu(service)
            print()

        elif choice == "4":
            manage_genres_menu(service)
            print()

        elif choice == "5":
            manage_films_menu(service)
            print()


        elif choice == "6":
            search_films_cli(service)
            print()

        elif choice == "7":
            display_statistics(service)
            print()

        elif choice == "0":
            print("Au revoir.")
            print()
            break

        else:
            print()
            print("Choix invalide.")


if __name__ == "__main__":
    main()