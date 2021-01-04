import time
import multiprocessing

myarray = []
def cal_square(a):
    print("claculating square:")
    for i in a:
        time.sleep(3)
        print('square:',i*i)
        myarray.append(i*i)
    print(f"square {myarray}")
    return

def cal_cube(a):
    print('calculating cube')
    for i in a:
        time.sleep(3)
        print('cube:',i*i*i)
        myarray.append(i*i*i)
    print(f"cube {myarray}")
    return

if __name__ =='__main__':

    b= [4,6,3,2,44,5]
    time1= time.time()
    t1= multiprocessing.Process(target=cal_square, args=(b,))
    t2= multiprocessing.Process(target=cal_cube, args=(b,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(f"final {myarray}")
    time2= time.time()
    print("total time take by program is :", time2-time1)