"""
Program symuluje pojedynczy rzut kostką
"""
import random

rzut = random.randint(1, 6)
# randint(a, b) zwraca pseudolosową wartość N, taką że: a <= N <= b

print('Liczba wyrzuconych oczek:', rzut)
