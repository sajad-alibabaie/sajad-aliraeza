import math
import threading
import timeit


# function to count the divisors
def countDivisors(n):
    sum = 1
    end = int(math.sqrt(n)) + 1
    for i in range(2, end):
        if n % i == 0:
            sum += i

            if n / i != i:
                sum += (n / i)

    if sum == n:
        return True
    return False


def handelthread(start, end, name):
    for j in range(start, end):
        if countDivisors(j):
            print("thread :", name, " find", j)


n = int(input("enter num:"))
threadcount = int(input("enter thread count:"))
lentgh = int(n / threadcount)
st, en = 0, lentgh
threads = []
start = timeit.default_timer()

for j in range(threadcount - 1):
    threads.append(threading.Thread(target=handelthread, args=(st, en, j + 1)))
    st = en
    en += lentgh

threads.append(threading.Thread(target=handelthread, args=(st, n, "last one")))

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

stop = timeit.default_timer()

print('Time: ', stop - start)
