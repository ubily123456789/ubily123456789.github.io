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
    return ans

def square(num):
    return num * num

def power(num, power):
    return num ** power

def factorial(num):
    other = 0
    ans = 1
    for i in range(num):
        other = other + 1
        # print(other)
        ans = ans * other
    # print("")
    return ans

def root(num):
    return power(num, 0.5)

def eore(num):
    if num/2 == num//2: print("even")
    else: print("odd")

def fib(am):
    num = 1
    num2 = 1
    for i in range(am):
        var = num + num2
        num2 = var
    return var

print(fib(1))
