import os

def count_rabbits(n, k):
    prev = 1
    curr = 1
    for _ in range(n - 2):
        prev, curr = curr, k * prev + curr
    return curr

print(count_rabbits(33, 3))