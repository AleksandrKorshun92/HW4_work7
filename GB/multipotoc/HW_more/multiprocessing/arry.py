"""
Реализация через многопроцессорность
"""

import random
import time
import multiprocessing

arr=[]
start_time = time.time()
def new_arr(start, stop):
    global arr
    for _ in range(start, stop):
        rand = random.randint(1,100)
        arr.append(rand)
    # print(f'массив - {arr}. Затраченное врем - {time.time() - start_time:.3f}')

def procces_arr(number):
    count_process=1000
    process = []
    for i in range(count_process):
        p = multiprocessing.Process(target=new_arr(i*number//count_process,(i+1)*number//count_process))
        process.append(p)
        p.start()

    for p in process:
        p.join()
    return arr

if __name__=="__main__":
    print(procces_arr(1_000_000))
    print(f"Затраченное время {time.time() - start_time:.3f}")
