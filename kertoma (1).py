# Tamam Krajrm



def factorial_recursive(n: int):

    if (n == 0):

        return 1

    return n * factorial_recursive(n - 1)





def factorial_loop(n: int):

    multiplier = 1



    for i in range(1, n+1):

        multiplier = multiplier * i

    return multiplier





def init():

    print("Type an integer between 1 and 10")

    input_a = input()