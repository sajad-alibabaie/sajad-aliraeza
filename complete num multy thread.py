import math
import threading
import timeit


# function to count the divisors
def countDivisors(n):
    sum = 1
    for i in range(2, (int)(math.sqrt(n)) + 1):
        if (n % i == 0):
            sum += i

            if (n / i != i):
                sum += (n / i)

    if (sum == n):
        return True
    return False


def handlethread(start, end, name):
    for j in range(start, end):
        if (countDivisors(j)):
            print("thread :", name, " find", j)


n = int(input("enter num:"))
threadcount = int(input("enter thread count:"))
lentgh = int(n / threadcount)

start = timeit.default_timer()
st = 0
en = lentgh
threads = []
for j in range(threadcount-1):
    threads.append(threading.Thread(target=handlethread, args=(st, en, j + 1)))
    st = en
    en += lentgh
    threads[j].start()
    threads[j].join()
    if j == threadcount - 1:
        if n % threadcount > 0:
            en += n % threadcount

stop = timeit.default_timer()

print('Time: ', stop - start)
