#!/usr/bin/env python3
import re
from pathlib import Path


def get_parsed(contents):
    coords, folds = [], []

    pieces = contents.split('\n\n')
    for p in filter(len, pieces[0].strip().split('\n')):
        x, y = map(int, map(str.strip, p.split(',')))
        coords.append((x, y))

    for p in filter(len, pieces[1].strip().split('\n')):
        m = re.search(r'([xy])=(\d+)', p)
        if m:
            axis, val = map(str.strip, m.groups())
            folds.append((axis, int(val)))

    return coords, folds


def print_mtx(mtx):
    for i in range(len(mtx)):
        print(''.join('#' if x else '.' for x in mtx[i]))


def get_next_coords_foldy(y):
    row_indexes = (y, y)
    while 1:
        row_indexes = (row_indexes[0] - 1, row_indexes[1] + 1)
        yield row_indexes


def get_next_coords_foldx(x):
    col_indexes = (x, x)
    while 1:
        col_indexes = (col_indexes[0] - 1, col_indexes[1] + 1)
        yield col_indexes


def part1(contents, exact_part1: bool = True):
    coords, folds = get_parsed(contents)
    m, n = (
        max(coords, key=lambda tup: tup[1])[1] + 1,
        max(coords, key=lambda tup: tup[0])[0] + 1,
    )

    # M x N
    mtx = []
    for i in range(m):
        mtx.append([0] * n)
    for x, y in coords:
        mtx[y][x] = 1

    for (axis, value) in folds:
        if axis == 'y':
            it = get_next_coords_foldy(value)
            foldable_rows_indexes = next(it)
            while all(x > -1 for x in foldable_rows_indexes):
                if any(x >= m for x in foldable_rows_indexes):
                    break

                i1, i2 = foldable_rows_indexes
                for j in range(n):
                    mtx[i1][j] = mtx[i1][j] or mtx[i2][j]

                foldable_rows_indexes = next(it)

            # decr number of rows in mtx
            m = value
            mtx = mtx[:m]

        else:
            # 'x'
            it = get_next_coords_foldx(value)
            foldable_cols_indexes = next(it)
            while all(x > -1 for x in foldable_cols_indexes):
                if any(x >= n for x in foldable_cols_indexes):
                    break

                j1, j2 = foldable_cols_indexes
                for i in range(m):
                    mtx[i][j1] = mtx[i][j1] or mtx[i][j2]

                foldable_cols_indexes = next(it)

            # decr number of cols in mtx
            n = value
            for i in range(m):
                mtx[i] = mtx[i][:n]

        # print_mtx(mtx)
        # print('*' * 10)

        # only for the 1st fold
        if exact_part1:
            break

    s = sum(mtx[i][j] for i in range(m) for j in range(n))
    print(
        'Part {x}; number of dots: {s}'.format(x=1 if exact_part1 else 2, s=s)
    )

    if not exact_part1:
        print_mtx(mtx)


def part2(contents):
    pass


if __name__ == '__main__':
    contents = Path('input.txt').read_text().strip()

    # contents = Path('input_sample.txt').read_text().strip()

    part1(contents)
    part1(contents, False)
