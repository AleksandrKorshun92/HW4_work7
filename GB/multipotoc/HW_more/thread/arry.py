"""
Реализация через многопоточность
"""

import random
import time
import threading

arr=[]
start_time = time.time()
def new_arr(start, stop):
    global arr
    for _ in range(start, stop):
        rand = random.randint(1,100)
        arr.append(rand)
    # print(f'массив - {arr}. Затраченное врем - {time.time() - start_time:.3f}')

def thread_arr(number):
    count_thread=1000
    threads = []
    for i in range(count_thread):
        t = threading.Thread(target=new_arr(i*number//count_thread,(i+1)*number//count_thread))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    return arr

if __name__=="__main__":
    print(thread_arr(1_000_000))
    print(f"Затраченное время {time.time() - start_time:.3f}")