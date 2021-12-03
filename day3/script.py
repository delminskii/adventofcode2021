#!/usr/bin/env python3
from pathlib import Path


def part1(xs):
    i, n = 0, len(xs[0])
    gamma_rate, epsiolon_rate = [], []
    while i < n:
        ones, zeros = 0, 0
        for x in xs:
            if x[i] == '0':
                zeros += 1
            else:
                ones += 1

        gamma_rate.append(int(ones > zeros))

        i += 1

    epsiolon_rate = map(lambda x: int(not x), gamma_rate)

    gamm_rate_dec = int(''.join(str(x) for x in gamma_rate), 2)
    epsiolon_rate_dec = int(''.join(str(x) for x in epsiolon_rate), 2)
    print(gamm_rate_dec * epsiolon_rate_dec)


def _get_common(xs, i) -> tuple:
    n = len(xs[0])
    ones, zeros = 0, 0
    for x in xs:
        if x[i] == '0':
            zeros += 1
        else:
            ones += 1

    n = max(zeros, ones)
    m = min(zeros, ones)
    most_ch = int(ones > zeros)
    least_ch = int(not most_ch)

    return (str(most_ch), str(least_ch), n, m)


def part2(xs):
    # calc oxygen rating
    new_xs = xs[:]
    i_b = 0
    while len(new_xs) != 1:
        most_common, least_common, most_n, least_n = _get_common(new_xs, i_b)

        if most_n == least_n:
            new_xs = list(filter(lambda x: x[i_b] == '1', new_xs))
        else:
            new_xs = list(filter(lambda x: x[i_b] == most_common, new_xs))

        i_b += 1
    ox_rating = int(''.join(ch for ch in new_xs), 2)

    # the same for co2 rating
    new_xs = xs[:]
    i_b = 0
    while len(new_xs) != 1:
        most_common, least_common, most_n, least_n = _get_common(new_xs, i_b)

        if most_n == least_n:
            new_xs = list(filter(lambda x: x[i_b] == '0', new_xs))
        else:
            new_xs = list(filter(lambda x: x[i_b] == least_common, new_xs))

        i_b += 1
    co2_rating = int(''.join(ch for ch in new_xs), 2)

    print(ox_rating * co2_rating)


if __name__ == '__main__':
    xs = Path('input.txt').read_text().split('\n')
    xs = filter(len, map(str.strip, xs))
    xs = list(xs)

    part1(xs)
    part2(xs)
