import os
import cherrypy

from mako.lookup import TemplateLookup
from service import CineMatchService


os.makedirs("res/tmp/mako_modules", exist_ok=True)

mylookup = TemplateLookup(
    directories=["res/templates"],
    input_encoding="utf-8",
    output_encoding="utf-8",
    default_filters=["h"],
    module_directory="res/tmp/mako_modules"
)


def to_int(value, default=None):
    """Convertit une valeur de formulaire en entier sans déclencher d'erreur 500."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def to_float(value, default=None):
    """Convertit une valeur de formulaire en nombre décimal sans erreur 500."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


class CineMatchWeb:
    def __init__(self):
        self.service = CineMatchService()

    @cherrypy.expose
    def default(self, *args, **kwargs):
        """Redirige les URLs inconnues au lieu d'afficher une page d'erreur."""
        raise cherrypy.HTTPRedirect("/")

    # ============================================================
    # FRONT OFFICE PUBLIC
    # ============================================================

    @cherrypy.expose
    def index(self):
        films = self.service.list_films()
        humeurs = self.service.list_humeurs()

        template = mylookup.get_template("public_index.html")
        return template.render(films=films, humeurs=humeurs)

    @cherrypy.expose
    def moods(self):
        humeurs = self.service.list_humeurs()

        template = mylookup.get_template("public_moods.html")
        return template.render(humeurs=humeurs)

    @cherrypy.expose
    def mood(self, humeur_id=None):
        humeur_id = to_int(humeur_id)
        if humeur_id is None:
            raise cherrypy.HTTPRedirect("/moods")

        humeur = self.service.get_humeur(humeur_id)
        films = self.service.find_films(humeur_id=humeur_id) if humeur else []

        template = mylookup.get_template("public_mood_films.html")
        return template.render(humeur=humeur, films=films)

    @cherrypy.expose
    def film_detail(self, film_id=None):
        film_id = to_int(film_id)
        if film_id is None:
            raise cherrypy.HTTPRedirect("/")

        film = self.service.get_film(film_id)

        if film is None:
            raise cherrypy.HTTPRedirect("/")

        humeur = self.service.get_humeur(film.id_humeur)
        genre = self.service.get_genre(film.id_genre)

        template = mylookup.get_template("public_film_detail.html")
        return template.render(film=film, humeur=humeur, genre=genre)

    # ============================================================
    # BACK OFFICE ADMIN
    # ============================================================

    @cherrypy.expose
    def admin(self):
        films = self.service.list_films()
        humeurs = self.service.list_humeurs()
        genres = self.service.list_genres()

        template = mylookup.get_template("admin_index.html")
        return template.render(films=films, humeurs=humeurs, genres=genres)

    # ============================================================
    # CRUD FILMS
    # ============================================================

    @cherrypy.expose
    def admin_films(self):
        films = self.service.list_films()

        template = mylookup.get_template("admin_films.html")
        return template.render(films=films)

    @cherrypy.expose
    def add_film_form(self):
        humeurs = self.service.list_humeurs()
        genres = self.service.list_genres()

        template = mylookup.get_template("admin_film_form.html")
        return template.render(
            title="Ajouter un film",
            action="/add_film",
            film=None,
            humeurs=humeurs,
            genres=genres
        )

    @cherrypy.expose
    def add_film(self, titre="", synopsis="", annee="", duree="", note="", affiche="", id_humeur="", id_genre=""):
        annee_value = to_int(annee)
        duree_value = to_int(duree)
        note_value = to_float(note)
        humeur_value = to_int(id_humeur)
        genre_value = to_int(id_genre)

        if None not in (annee_value, duree_value, note_value, humeur_value, genre_value):
            try:
                self.service.create_film(
                    titre,
                    synopsis,
                    annee_value,
                    duree_value,
                    note_value,
                    affiche,
                    humeur_value,
                    genre_value
                )
            except ValueError:
                pass

        raise cherrypy.HTTPRedirect("/admin_films")

    @cherrypy.expose
    def edit_film_form(self, film_id=None):
        if film_id is None:
            raise cherrypy.HTTPRedirect("/admin_films")

        film = self.service.get_film(to_int(film_id))
        if film is None:
            raise cherrypy.HTTPRedirect("/admin_films")

        humeurs = self.service.list_humeurs()
        genres = self.service.list_genres()

        template = mylookup.get_template("admin_film_form.html")
        return template.render(
            title="Modifier un film",
            action="/edit_film",
            film=film,
            humeurs=humeurs,
            genres=genres
        )

    @cherrypy.expose
    def edit_film(self, film_id="", titre="", synopsis="", annee="", duree="", note="", affiche="", id_humeur="", id_genre=""):
        film_value = to_int(film_id)
        annee_value = to_int(annee)
        duree_value = to_int(duree)
        note_value = to_float(note)
        humeur_value = to_int(id_humeur)
        genre_value = to_int(id_genre)

        if None not in (film_value, annee_value, duree_value, note_value, humeur_value, genre_value):
            try:
                self.service.modify_film(
                    film_value,
                    titre,
                    synopsis,
                    annee_value,
                    duree_value,
                    note_value,
                    affiche,
                    humeur_value,
                    genre_value
                )
            except ValueError:
                pass

        raise cherrypy.HTTPRedirect("/admin_films")

    @cherrypy.expose
    def delete_film(self, film_id=None):
        if film_id is not None:
            film_id = to_int(film_id)
            if film_id is not None:
                self.service.remove_film(film_id)

        raise cherrypy.HTTPRedirect("/admin_films")

    # ============================================================
    # HUMEURS
    # ============================================================

    @cherrypy.expose
    def admin_humeurs(self):
        humeurs = self.service.list_humeurs()

        template = mylookup.get_template("admin_humeurs.html")
        return template.render(humeurs=humeurs)

    @cherrypy.expose
    def add_humeur_form(self):
        raise cherrypy.HTTPRedirect("/admin_humeurs")

    @cherrypy.expose
    def add_humeur(self, nom="", description=""):
        try:
            self.service.create_humeur(nom, description)
        except ValueError:
            pass
        raise cherrypy.HTTPRedirect("/admin_humeurs")

    @cherrypy.expose
    def delete_humeur(self, humeur_id=None):
        if humeur_id is not None:
            humeur_id = to_int(humeur_id)
            if humeur_id is not None:
                self.service.remove_humeur(humeur_id)

        raise cherrypy.HTTPRedirect("/admin_humeurs")

    # ============================================================
    # GENRES
    # ============================================================

    @cherrypy.expose
    def admin_genres(self):
        genres = self.service.list_genres()

        template = mylookup.get_template("admin_genres.html")
        return template.render(genres=genres)

    @cherrypy.expose
    def add_genre_form(self):
        raise cherrypy.HTTPRedirect("/admin_genres")

    @cherrypy.expose
    def add_genre(self, nom=""):
        try:
            self.service.create_genre(nom)
        except ValueError:
            pass
        raise cherrypy.HTTPRedirect("/admin_genres")

    @cherrypy.expose
    def delete_genre(self, genre_id=None):
        if genre_id is not None:
            genre_id = to_int(genre_id)
            if genre_id is not None:
                self.service.remove_genre(genre_id)

        raise cherrypy.HTTPRedirect("/admin_genres")

    # ============================================================
    # RECHERCHE
    # ============================================================

    @cherrypy.expose
    def search(self, titre="", genre="", annee=""):
        annee_value = to_int(annee) if annee else None

        films = self.service.find_films(
            titre=titre,
            genre=genre,
            annee=annee_value
        )

        template = mylookup.get_template("search.html")
        return template.render(
            films=films,
            titre=titre,
            genre=genre,
            annee=annee
        )

    # ============================================================
    # STATISTIQUES
    # ============================================================

    @cherrypy.expose
    def stats(self):
        stats_humeur = self.service.get_stats_by_humeur()
        stats_genre = self.service.get_stats_by_genre()
        stats_annee = self.service.get_stats_by_annee()

        template = mylookup.get_template("stats.html")
        return template.render(
            stats_humeur=stats_humeur,
            stats_genre=stats_genre,
            stats_annee=stats_annee
        )


if __name__ == "__main__":
    cherrypy.config.update({
        "server.socket_host": "127.0.0.1",
        "server.socket_port": 8080,
        "tools.staticdir.root": os.path.abspath(os.getcwd())
    })

    config = {
        "/static": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": "res/static"
        }
    }

    cherrypy.quickstart(CineMatchWeb(), "/", config)