import random

def new_arr(number):
    arr=[]
    for _ in range(number):
        rand = random.randint(1,100)
        arr.append(rand)
    return arr

if __name__=="__main__":
    print(new_arr(1_000_000))