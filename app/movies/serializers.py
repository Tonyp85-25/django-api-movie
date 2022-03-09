from rest_framework import serializers

from actors.serializers import ActorSerializer
from actors.models import Actor
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ["title", "description", "actors"]
        depth = 1

    def create(self, validated_data):
        """Creates movie object with actors if provided"""

        actors_data = validated_data.pop("actors")
        movie = Movie.objects.create(**validated_data)
        for actor_data in actors_data:
            Actor.objects.create(**actor_data)
        return movie

    def update(self, instance, validated_data):
        """Updates movie objet with actors"""
        actors_data = validated_data.pop("actors")

        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        actors = instance.get("actors", None)

        if actors is not None:
            actors_data_ids = {}
            updated_actors = []
            actors_mapping = {actor["id"]: actor for actor in actors}
            for actor_data in actors_data:
                actor_id = actor_data.get("id", None)
                if actor_id is None:
                    Actor.objects.create(**actor_data)
                else:
                    Actor.objects.update(**actor_data)
                    actors_data_ids[actor_id] = True

            for actor_id, actor in actors_mapping.items():
                if actor_id in actors_data_ids:
                    updated_actors.append(actor)
            instance.actors = updated_actors

        instance.save()
        return instance
