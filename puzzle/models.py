from __future__ import unicode_literals

from django.db import models


class Piece(models.Model):
    puzzle_id = models.ForeignKey(
        'puzzle.Puzzle',
        related_name="pieces"
    )
    src_id = models.CharField(max_length=32)
    src_href = models.CharField(max_length=256)
    secret = models.CharField(max_length=128)

    pos_x = models.IntegerField()
    pos_y = models.IntegerField()
    abs_x = models.IntegerField()
    abs_y = models.IntegerField()


class Puzzle(models.Model):
    username = models.CharField(max_length=32)
    src_id = models.CharField(max_length=32)
    src_href = models.CharField(max_length=256)

    @property
    def solution_string(self):
        return "-".join(
            map(lambda x: x.secret, self.pieces.all())
        )
