from actors.models import Actor
from movies.models import Movie
from reviews.models import Review
from random import randint
import  os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

actors = []
movies=[]
def actor_factory():
    for i in range(10):
        first_name = "actor{0}".format(i)
        last_name = "name{0}".format(i)
        actor = Actor.objects.create(first_name=first_name,last_name=last_name)
        actors.append(actor)
        actor.save()


def movie_factory():
    for i in range(10):
        title = "movie{0}".format(i)
        index = randint(0,9)
        movie = Movie.objects.create(title=title,description="blablabla")
        movie.actors.add(actors[index])
        index = randint(0, 9)
        movie.actors.add(actors[index])
        movies.append(movie)
        movie.save()

def review_factory():
    for i in range(10):
        grade =randint(0,5)
        index = randint(0, 9)
        movie = movies[index]
        review = Review.objects.create(grade=grade, movie=movie)
        review.save()

def load_fixtures():
    actor_factory()
    movie_factory()
    review_factory()



