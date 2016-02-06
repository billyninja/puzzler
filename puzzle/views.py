from puzzle.models import Puzzle, Piece
from rest_framework import viewsets
from puzzle.serializers import PuzzleSerializer, SolutionSerializer


class PuzzleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that retrieves puzzled tiles
    """
    queryset = Puzzle.objects.all().order_by('-id')
    serializer_class = PuzzleSerializer


class SolutionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that retrieves the final solution to the puzzle
    """
    queryset = Puzzle.objects.all().order_by('-id')
    serializer_class = SolutionSerializer
