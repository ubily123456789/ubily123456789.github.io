# making math problem solvers
import math

pi = math.pi

def steps(num):
    other = 0
    ans = 0
    for i in range(num):
        other = other + 1
        # print(other)
        ans = ans + other
    # print("")
    print(ans)

def square(num):
    print(num * num)

def power(num, power):
    print(num ** power)

def factorial(num):
    other = 0
    ans = 1
    for i in range(num):
        other = other + 1
        # print(other)
        ans = ans * other
    # print("")
    print(ans)

def root(num):
    power(num, 0.5)
