from puzzle.models import Puzzle, Piece
from rest_framework import serializers


class PuzzleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Puzzle
        fields = ('id', 'username', 'pieces')


class PieceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Piece
        fields = ('puzzle_id', 'pos_x', 'pos_y', 'abs_x', 'abs_y')


class SolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Puzzle
        fields = ('id', 'username', 'pieces')
