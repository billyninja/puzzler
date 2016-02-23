import json
from django.shortcuts import get_object_or_404
from puzzle.models import Puzzle, Piece
from rest_framework import viewsets
from puzzle.serializers import SolutionSerializer, PieceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from hashlib import md5


class PuzzleView(APIView):

    def get(self, request, puzzle_id):
        puzzle = get_object_or_404(Puzzle, pk=puzzle_id)

        # Setting the puzzle pieces to a randomized order
        pieces = puzzle.pieces.all().order_by("?")
        # Hammering the original serializer
        resp = SolutionSerializer(puzzle).data
        fhost = 'http://localhost:8080'
        resp["pieces"] = [{"secret_id": x.secret, "href": fhost + x.src_href}
                          for x in pieces]

        return Response(resp, status=200)

    def post(self, request):
        puzzle = Puzzle.objects.create(username=request.data["username"])
        bulk = list()

        for piece in json.loads(request.data["pieces"]):
            if "href" in piece:
                piece["src_href"] = piece["href"]
                del piece["href"]
            piece["puzzle_id"] = puzzle
            seed = "%d-%d-%d" % (puzzle.pk,
                                 piece["pos_x"],
                                 piece["pos_y"])
            piece["secret"] = md5(seed).hexdigest()
            bulk.append(Piece(**piece))

        # Bulk Create - almost N times faster in sqlite!
        # where N is the number of pieces
        Piece.objects.bulk_create(bulk)

        return Response("ok!", status=status.HTTP_201_CREATED)

    def put(self, request, puzzle_id):
        puzzle = get_object_or_404(Puzzle, pk=puzzle_id)
        prop_solution = "-".join(request.data["sequence"])

        status = 200 if (puzzle.solution_string == prop_solution) else 400

        MESSAGES = {
            200: "Congratulations! Solution found!",
            400: "No luck! Try again!",
        }

        return Response(MESSAGES.get(status), status=status)


class SolutionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that retrieves the final solution to the puzzle
    """
    queryset = Puzzle.objects.all().order_by('-id')
    serializer_class = SolutionSerializer


class PieceViewSet(viewsets.ModelViewSet):
    queryset = Piece.objects.all().order_by('-id')
    serializer_class = PieceSerializer
