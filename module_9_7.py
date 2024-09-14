def is_prime(fanc):
    def wrapper(*number):
        is_primes = True
        result_fanc = fanc(*number)
        for i in range(2, result_fanc):
            if result_fanc % i == 0:
                is_primes = False
        if is_primes:
            print("Простое")
        else:
            print("Составное")
        return result_fanc
    return wrapper


@ is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
