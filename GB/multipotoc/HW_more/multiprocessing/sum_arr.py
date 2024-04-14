"""
Реализация через многопроцессорность
"""

from arry import procces_arr
import time
import multiprocessing

start_time = time.time()
result=0
def sum_arr(arr):
    global result
    result += sum(arr)
    print(f'сумма чисел в запущенном процессе - {result:_}. Затраченное время - {time.time() - start_time:.3f}')

if __name__=="__main__":
    user_arry = procces_arr(1_000_000)
    count_process = len(user_arry) // 10000
    threads = []
    for i in range(count_process):
        p = multiprocessing.Process(target=sum_arr(user_arry[i * 10000:(i + 1) * 10000]))
        threads.append(p)
        p.start()

    for p in threads:
        p.join()

    print(f'Сумма массива - {result:_}')
    print(f"Finish. Затраченное время {time.time() - start_time:.3f}")