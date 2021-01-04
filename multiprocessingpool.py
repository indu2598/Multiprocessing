# def f(n):
#     return n*n
#
# if __name__ == "__main__":
#     array = [2,4,6,76,43]
#     result = []
#     for n in array:
#         result.append(f(n))
#     print(result)


    # here only one Core using with code whereas other cores are sitting idle at somepoint
    # so here we code inorder to divide this code equaly with all other cores which will reduce the time of computing
    #  using map and reduce

from multiprocessing import Pool
import time
def fn(n):
    sum = 0
    for x in range(100):
        sum+= x*x
    return sum


if __name__ == "__main__":
    t1 = time.time()
    p = Pool(processes=5)
    result =p.map(fn,range(10000000))
    p.close()
    p.join()
    # print(result)
    print(time.time()-t1)



    t1 = time.time()
    result = []
    for x in range(10000000):
        result.append(fn(x))
    print(time.time()-t1)