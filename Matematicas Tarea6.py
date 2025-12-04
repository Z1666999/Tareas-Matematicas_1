#Tarea 5


#ejercicio 1
import math
n=15
k=12
r= math.comb(n,k)
print(r)


#ejercico 2
print("-----------")

import math 
n=420
k=50
r= math.comb(n,k)
print(r)


n=410
k=400
r= math.comb(n,k)
print(r)

n=618
k=615
r= math.comb(n,k)
print(r)
print("-----------")


#ejercicio 3

r=20*21
print(r)

print("-----------")

#ejercicio 12

r=6*6*6*6*6*6*6
print(r)


r=3**7
print(r)

r=6**5
print(r)

print("-----------")

#ejercicio 50

r=4**27
print(r)

print("-----------")
## Ejercicio 4


import numpy as np

numbers = 10  # 0-9
letters = 26  # A-Z

# Calculate the total combinations
total_plates = (numbers ** 2) * (letters ** 2) * (numbers ** 3)
total_plates



print("-----------")
## Ejercicio 5

questions = 11
options_per_question = 2  # True or False

total_ways = options_per_question ** questions
total_ways

print("-----------")
## Ejercicio 6

#| code-fold: true

players = 893
matches = 0
rounds = 0

while players > 1:
    matches += players // 2
    players = (players + 1) // 2

    rounds += 1
    print(f"After round {rounds}, remaining players: {players}")
print(f"Total matches played: {matches}")


print("-----------")
## Ejercicio 10

import math

math_books = 6
cs_books = 4

# Calculate the arrangements
math_arrangements = math.perm(math_books, 2)
cs_arrangements = math.perm(cs_books, 3)

total_arrangements = math_arrangements * cs_arrangements
total_arrangements

print("-----------")
## Ejercicio 13

import math
captain_choices = 30

alternate_choices = math.comb(29, 2)

total_choices = captain_choices * alternate_choices
total_choices

print("-----------")
## Problema 16

from math import factorial

total_marbles = 2 + 4 + 3
ways = factorial(total_marbles) / (factorial(2) * factorial(4) * factorial(3))
ways

print("-----------")

#b) All marbles are distinguishable?
ways_distinguishable = factorial(total_marbles)

ways_distinguishable

## Ejercicio 22

import math

total_ways = math.comb(10,4)

total_ways

print("-----------")

# Problema 40





# (A \cup B) = \# A + \# B - \# (A \cap B)  = 336+ 223-149= 410$$

print("-----------")
##ejercicio 7

print(5*2)

print("-----------")
#ejercicio 8

print(4*2)


print("-----------")

# ejercicio 9
print(2**8)


#ejercicio 11

print(26*10)

print("-----------")


#ejercicio 12

print(6**7)

print(3**7)

print(6**5)


print("-----------")

#ejercico 14
# (a) Divisibles por 5 y por 7 (es decir, por 35)
a = sum(1 for n in range(1000, 10000) if n % 35 == 0)

# (b) Divisibles por 7
b = sum(1 for n in range(1000, 10000) if n % 7 == 0)

# (c) Dígitos distintos
def distinct_digits(n):
    s = str(n)
    return len(set(s)) == 4

c = sum(1 for n in range(1000, 10000) if distinct_digits(n))

# (d) Divisible por 5 pero NO por 7
d = sum(1 for n in range(1000, 10000) if n % 5 == 0 and n % 7 != 0)


print("-----------")

#ejercicio 48
import math 
print(math.factorial(5))

print(math.factorial(6)-math.factorial(5))

print("-----------")
#ejercicio 47 

print(1000-869)

print(524-323)

print("-----------")
#ejercicio 45

#Solo DS=122−18=104
#Solo Wii=181−18=163


print(104+163)


print("-----------")

#ejercicio 44
   #∣M∪P∣=44+21−5=60
print(522-60)

print(44-5)


#ejercicio 43

  #∣I∪B∣=280+101−23=358

print(1081-358)

#ejercicio 41

print(198+71-21)