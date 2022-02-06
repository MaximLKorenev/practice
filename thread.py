import time
import random
from threading import Thread

list_float = []
for _ in range(100000):
    list_float.append(random.random())

x = len(list_float) // 10

dl1 = list_float[0: x]
dl2 = list_float[x: 2 * x]
dl3 = list_float[2 * x: 3 * x]
dl4 = list_float[3 * x: 4 * x]
dl5 = list_float[4 * x: 5 * x]
dl6 = list_float[5 * x: 6 * x]
dl7 = list_float[6 * x: 7 * x]
dl8 = list_float[7 * x: 8 * x]
dl9 = list_float[8 * x: 9 * x]
dl10 = list_float[9 * x:]


def sum_list(list_data, list_result):
    sum = 0
    for i in list_data:
        sum += i
        time.sleep(0.05)
    list_result.append(sum)


results = []

t1 = Thread(target=sum_list, name='Thread N 1', args=(dl1, results))
t2 = Thread(target=sum_list, name='Thread N 2', args=(dl2, results))
t3 = Thread(target=sum_list, name='Thread N 3', args=(dl3, results))
t4 = Thread(target=sum_list, name='Thread N 4', args=(dl4, results))
t5 = Thread(target=sum_list, name='Thread N 5', args=(dl5, results))
t6 = Thread(target=sum_list, name='Thread N 6', args=(dl6, results))
t7 = Thread(target=sum_list, name='Thread N 7', args=(dl7, results))
t8 = Thread(target=sum_list, name='Thread N 8', args=(dl8, results))
t9 = Thread(target=sum_list, name='Thread N 9', args=(dl9, results))
t10 = Thread(target=sum_list, name='Thread N 10', args=(dl10, results))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

print(sum(list_float))
print(results)
