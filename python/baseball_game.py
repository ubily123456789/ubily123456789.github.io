# making math problem solvers
def steps(num):
    other = 0
    ans = 0
    for i in range(num):
        other = other + 1
        print(other)
        ans = ans + other
    print("")
    print(ans)

def square(num):
    print(num * num)

def power(num, power):
    print(num ** power)

def factorial(num):
    other = 0
    ans = 0
    for i in range(num):
        other = other + 1
        print(i+1)
        ans = ans * num

    print("")
    print(ans)

factorial(4)
