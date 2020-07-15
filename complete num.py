import math
import timeit


# function to count the divisors
def countDivisors(n):
    sum = 1
    for i in range(2, (int)(math.sqrt(n))+1):
        if (n % i == 0):
            sum += i

            if (n / i != i):
                sum += (n / i)

    if (sum == n):
        return True
    return False


n = int(input("enter num:"))
start = timeit.default_timer()
for j in range(n):
    if (countDivisors(j)):
        print(j)
stop = timeit.default_timer()

print('Time: ', stop - start)
