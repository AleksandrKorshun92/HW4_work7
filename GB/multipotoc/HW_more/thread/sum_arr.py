"""
Реализация через многопоточность
"""

from arry import thread_arr
import time
import threading

start_time = time.time()
result=0
def sum_arr(arr):
    global result
    result += sum(arr)
    print(f'сумма чисел в запущенном потоке - {result:_}. Затраченное время - {time.time() - start_time:.3f}')

def main():
    user_arry = thread_arr(1_000_000)
    count_thread = len(user_arry)//10000
    threads = []
    for i in range(count_thread):
        t = threading.Thread(target=sum_arr(user_arry[i*10000:(i+1)*10000]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__=="__main__":
    main()
    print(f'Сумма массива - {result:_}')
    print(f"Finish. Затраченное время {time.time() - start_time:.3f}")