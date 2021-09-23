from collections import deque
import random


def pb(a: deque, b: deque, moves: list):
    b.append(a.pop())
    moves.append('pb')


def sb(b: deque, moves: list):
    tmp1 = b.pop()
    tmp2 = b.pop()
    b.append(tmp1)
    b.append(tmp2)
    moves.append('sb')


def pa(a: deque, b: deque, moves: list):
    a.append(b.pop())
    moves.append('pa')


def rb(b: deque, moves: list):
    b.rotate(-1)
    moves.append('rb')


def rrb(b: deque, moves: list):
    b.rotate(1)
    moves.append('rrb')


def rotate_correctly(a: deque, b: deque, moves: list):
    if len(b) < 2:
        return
    i = 0
    while True:
        if b[-i-1] < a[-1] < b[-i] or b[-i] < b[-i-1] < a[-1] or a[-1] < b[-i] < b[-i-1]:
            break
        i += 1
    if i > len(b) / 2:
        for _ in range(len(b) - i):
            rb(b, moves)
    else:
        for _ in range(i):
            rrb(b, moves)


def push_swap(a: deque) -> list:
    b = deque()
    moves = []
    while a:
        rotate_correctly(a, b, moves)
        pb(a, b, moves)
    while b[-1] < b[0]:
        rb(b, moves)
    for _ in range(len(b)):
        pa(a, b, moves)
    return moves


def main():
    args = random.sample(range(999), 500)
    moves = push_swap(deque(args))
    print(moves)
    print(len(moves))


if __name__ == "__main__":
    main()
