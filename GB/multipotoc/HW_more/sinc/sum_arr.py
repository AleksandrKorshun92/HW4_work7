'''
Синхронное выполнение кода
'''

from arry import new_arr
import time


start_time = time.time()
def sum_arr(arr):
    res = 0
    for num in arr:
        res += num
    return res

def main():
    user_arry = new_arr(1_000_000)
    sum_arry = sum_arr(user_arry)
    return sum_arry

if __name__=="__main__":
    main()
    print(f'Сумма массива - {main():_}')
    print(f"Finish. Затраченное время {time.time() - start_time:.3f}")