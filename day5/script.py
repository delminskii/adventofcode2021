#!/usr/bin/env python3
import math
import re
from dataclasses import dataclass, replace
from pathlib import Path


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Vent:
    point_from: Point
    point_to: Point

    def __post_init__(self):
        # "from" must be the nearest one to (0, 0)
        coords_from = (self.point_from.x, self.point_from.y)
        coords_to = (self.point_to.x, self.point_to.y)

        # exchange
        len1 = math.hypot(*coords_from)
        len2 = math.hypot(*coords_to)
        if len2 < len1:
            # exchange
            self.point_from, self.point_to = self.point_to, self.point_from

    def __hash__(self):
        return hash((self.point_from, self.point_to))

    def is_horizontal(self):
        return self.point_from.x == self.point_to.x

    def is_vertical(self):
        return self.point_from.y == self.point_to.y

    def is_diagonal(self):
        # y = kx where k=1 so x == y
        x_diff = abs(self.point_from.x - self.point_to.x)
        y_diff = abs(self.point_from.y - self.point_to.y)
        return x_diff == y_diff

    def get_max_dim(self):
        return max(
            self.point_from.x,
            self.point_from.y,
            self.point_to.x,
            self.point_to.y,
        )

    def get_cover_points(self, take_diagonal: bool = False):
        ret_points = set()

        if self.point_from.x == self.point_to.x:
            ret_points.update(
                Point(self.point_from.x, y)
                for y in range(self.point_from.y, self.point_to.y + 1)
            )
        elif self.point_from.y == self.point_to.y:
            ret_points.update(
                Point(x, self.point_from.y)
                for x in range(self.point_from.x, self.point_to.x + 1)
            )
        elif take_diagonal:
            step_x = 1 if self.point_from.x < self.point_to.x else -1
            step_y = 1 if self.point_from.y < self.point_to.y else -1
            p = replace(self.point_from)

            while 1:
                ret_points.add(p)

                p = Point(p.x + step_x, p.y + step_y)
                if p == self.point_to:
                    break

            ret_points.add(self.point_to)

        return ret_points


def _get_vent_segments(contents) -> list:
    ret_vent_segments = []

    segment_line_re = re.compile(r'(\d+)')

    for line in contents.split('\n'):
        re_matches = segment_line_re.findall(line)
        if re_matches:
            numbers = list(map(int, map(str.strip, re_matches)))

            point_from = Point(numbers[0], numbers[1])
            point_to = Point(numbers[2], numbers[3])
            ret_vent_segments.append(Vent(point_from, point_to))

    return ret_vent_segments


def part1(contents):
    # we're interested in the ones where x1 = x2 or y1 = y2.
    vent_segments = _get_vent_segments(contents)
    vent_segments = list(
        filter(
            lambda vent: vent.is_horizontal() or vent.is_vertical(),
            vent_segments,
        )
    )

    n = max(x.get_max_dim() for x in vent_segments) + 1
    diagram = [[0] * n for _ in range(n)]

    for vent in vent_segments:
        for p in vent.get_cover_points():
            diagram[p.y][p.x] += 1

    # finally calc overlapped points
    n_overlapped_points = 0
    for rowline in diagram:
        n_overlapped_points += sum(1 for _ in filter(lambda x: x > 1, rowline))
    print(f'{n_overlapped_points}')


def part2(contents):
    vent_segments = _get_vent_segments(contents)
    vent_segments = list(
        filter(
            lambda vent: vent.is_horizontal()
            or vent.is_vertical()
            or vent.is_diagonal(),
            vent_segments,
        )
    )

    n = max(x.get_max_dim() for x in vent_segments) + 1
    diagram = [[0] * n for _ in range(n)]

    for vent in vent_segments:
        for p in vent.get_cover_points(True):
            diagram[p.y][p.x] += 1

    # finally calc overlapped points
    n_overlapped_points = 0
    for rowline in diagram:
        n_overlapped_points += sum(1 for _ in filter(lambda x: x > 1, rowline))
    print(f'{n_overlapped_points}')


if __name__ == '__main__':
    contents = Path('input.txt').read_text()

    # contents = Path('input_sample.txt').read_text()

    part1(contents)
    part2(contents)
