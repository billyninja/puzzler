from puzzle.models import Puzzle
from rest_framework import serializers


class PuzzleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Puzzle
        fields = ('id', 'username', 'tiles')


class SolutionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Puzzle
        fields = ('id', 'username', 'tiles')
