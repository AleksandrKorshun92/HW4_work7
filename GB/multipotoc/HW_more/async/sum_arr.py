"""
Выполнено через асинхронность
"""

from arry import new_arr
import time
import asyncio

start_time = time.time()
result=0
async def sum_arr(arr):
    global result
    result += sum(arr)
    print(f'сумма чисел в запущенном - {result:_}. Затраченное время - {time.time() - start_time:.3f}')

async def main():
    user_arry = new_arr(1_000_000)
    print(user_arry)
    count_asinc = len(user_arry)//10000
    tasks = []
    for i in range(count_asinc):
        t = asyncio.create_task(sum_arr(user_arry[i*10000:(i+1)*10000]))
        tasks.append(t)

    await asyncio.gather(*tasks)


if __name__=="__main__":
    asyncio.run(main())

    print(f'Сумма массива - {result:_}')
    print(f"Finish. Затраченное время {time.time() - start_time:.3f}")