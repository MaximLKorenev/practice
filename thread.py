import time
import random
from threading import Thread

list_float = []
for _ in range(100000):
    list_float.append(random.random())


def long_process(id, dat, _from, _to, results):
    s = sum(dat[_from:_to+1])
    time.sleep(0.5)
    results[id] = s


def concurrency(n, data):
    data_len = len(data) // n + 1
    f = 0
    results = {}
    threads = {}
    for i in range(n):
        t = Thread(target=long_process,
                   args=(i, data, f, f + data_len - 1, results))
        threads[i] = t
        t.start()
        f += data_len

    work = True
    while work:
        work = False
        for i in range(n):
            if threads[i].is_alive():
                work = True
                break

    summa = 0
    for i in range(n):
        summa += results[i]

    return summa


print(concurrency(10, list_float))
print(sum(list_float))
