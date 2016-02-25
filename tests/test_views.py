import pytest
from puzzle.views import PuzzleView
from puzzle.views import Puzzle
from django.test import RequestFactory
import json


def test_puzzle_options(mock):
    mk_puzzle_model = mock.patch('puzzle.views.Puzzle')
    mk_get_object_or_404 = mock.patch('puzzle.views.get_object_or_404')
    mk_solution_serializer = mock.patch('puzzle.views.SolutionSerializer')

    mk_puzzle_obj = mock.Mock()
    mk_puzzle_obj.pieces.all.order_by.return_value = [mock.Mock()]
    mk_get_object_or_404 = mock.MagicMock(return_value=mk_puzzle_obj)
    mk_solution_serializer.data = mock.MagicMock(return_value={})

    request = RequestFactory().options('/path', data={})
    response = PuzzleView().options(request, 123)

    assert response.status_code == 200


def test_puzzle_post(mock):
    mk_puzzle_model = mock.patch('puzzle.views.Puzzle')
    mk_piece_model = mock.patch('puzzle.views.Piece')
    puzzle_obj = mock.MagicMock(pk__return_value=1)
    mk_puzzle_model.objects.create = mock.MagicMock(return_value=puzzle_obj)
    mk_piece_model.objects.bulk_create = mock.MagicMock(return_value=[mock.Mock()])

    request = RequestFactory().post('/path')
    pieces = json.dumps([{
        'pos_x': 0,
        'pos_y': 0,
        'abs_x': 0,
        'abs_y': 0,
        'href': '/testing/img_0_0.jpg',
        'puzzle_id': '345076895456789',
    }])

    request.data = {'username': 'testuser', 'pieces': pieces}
    response = PuzzleView().post(request)

    assert response.status_code == 201


def test_puzzle_put(mock):
    mk_puzzle_model = mock.patch('puzzle.views.Puzzle')
    mk_puzzle_obj = mock.MagicMock()
    mk_puzzle_obj.solution_string= "asdqwe-qweasd"

    def wtf(model, pk):
        """dunno why but return_value for wasnt working as expected, so i did this"""
        return mk_puzzle_obj

    mk_get_object_or_404 = mock.patch('puzzle.views.get_object_or_404', wtf)

    request = RequestFactory().put('/path')
    request.data = {"sequence": ["asdqwe", "qweasd"]}
    response = PuzzleView().put(request, 123)

    assert response.status_code == 202
