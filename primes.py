"""List of prime numbers generator."""

def primes(number_of_primes):

    if number_of_primes < 1:
        raise ValueError(f"{number_of_primes} should be greater than 0")

    if not isinstance(number_of_primes,int):
        raise TypeError(f"{number_of_primes} should be an integer")

    list = [2]
    num = 2
    while len(list) < number_of_primes:
        num += 1
        if is_prime(num):
            list.append(num)
    return list

def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True
