import time
import multiprocessing

def cal_square(a, myarray):
    for i in a:
        time.sleep(1)
        print('square:',i*i)
        myarray.put(i*i)
    return

def cal_cube(a,myarray):
    print('calculating cube')
    for i in a:
        time.sleep(1)
        print('cube:',i*i*i)
        myarray.put(i*i*i)
    return

if __name__ =='__main__':

    b= [4,6,3,2,44,5]
    time1= time.time()
    myarray = multiprocessing.Queue()
    t1= multiprocessing.Process(target=cal_square, args=(b,myarray))
    t2= multiprocessing.Process(target=cal_cube, args=(b,myarray))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    while myarray.empty() is False:
        print(myarray.get())
    time2= time.time()
    print("total time take by program is :", time2-time1)