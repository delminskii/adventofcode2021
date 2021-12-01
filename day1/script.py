#!/usr/bin/env python3

from pathlib import Path

if __name__ == '__main__':
    lines = Path('input.txt').read_text().split('\n')
    lines = filter(len, map(str.strip, lines))

    numbers = list(map(int, lines))
    n = len(numbers)

    acc = 0
    for i in range(1, n):
        prev = numbers[i - 1]
        curr = numbers[i]
        acc += curr > prev
    print(acc)
