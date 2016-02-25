from puzzle.models import Puzzle, Piece
from rest_framework import serializers


class PuzzleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Puzzle
        fields = ('id', 'username', 'pieces')


class PieceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Piece
        fields = ('puzzle_id', 'pos_x', 'pos_y', 'abs_x', 'abs_y')


class SolutionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Puzzle
        fields = ('id', 'username', 'pieces')
