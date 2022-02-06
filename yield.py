import time
from threading import Thread


def long_process(n):
    sum = 0
    for x in range(n):
        sum += x + 1
        if x < n - 1:
            yield
        else:
            yield sum


def make_long_process(data):
    R = {}
    nlen = len(data)
    for n in range(nlen):
        id = long_process(data[n])
        R[n] = {'id': id, 'result': None}

    work = True
    while work:
        work = False
        for k in range(nlen):
            if R[k]['result'] is not None:
                continue
            R[k]['result'] = next(R[k]['id'])
            if R[k]['result'] is None:
                work = True

    summa = 0
    for n in range(nlen):
        summa += R[n]['result']
    return summa


r = make_long_process([10, 100, 256])
