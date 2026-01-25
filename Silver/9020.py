def check_prime(s):
    if s == 1:
        return False
    for j in range(2,s):
        if s%j == 0:
            return False
    else:
        return True


num = int(input())

for i in range(num):

    n = int(input())

    prime1 = n//2
    prime2 = n//2

    while not (check_prime(prime1) and check_prime(prime2)):
        prime1 += 1
        prime2 -= 1

    print(prime2, prime1)