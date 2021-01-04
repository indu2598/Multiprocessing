import time
import multiprocessing

def cal_square(a, myarray, v):
    print("claculating square:")
    v.value = 7.9
    for i in a:
        time.sleep(1)
        print('square:',i*i)
        for idx, j in enumerate(myarray):
            if j == 0:
                myarray[idx] = i * i
                break
    print(f"square {myarray[:]}")
    return

def cal_cube(a,myarray):
    print('calculating cube')
    for i in a:
        time.sleep(1)
        print('cube:',i*i*i)
        for idx, j in enumerate( myarray):
            if j == 0:
                myarray[idx] = i*i*i
                break
    print(f"cube {myarray[:]}")
    return

if __name__ =='__main__':

    b= [4,6,3,2,44,5]
    time1= time.time()
    myarray = multiprocessing.Array('i',12)
    v  = multiprocessing.Value('d',0.0)
    t1= multiprocessing.Process(target=cal_square, args=(b,myarray, v))
    t2= multiprocessing.Process(target=cal_cube, args=(b,myarray))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(f"final {myarray[:]}, {v.value}")
    time2= time.time()
    print("total time take by program is :", time2-time1)