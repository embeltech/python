import threading
import os

def func1(val):
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
    print("result : ", val)

def func2(val1,val2):
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))
    print("result : ", val1+val2)

if __name__ == "__main__":

    print("ID of process running main program: {}".format(os.getpid()))

    print("Main thread name: {}".format(threading.current_thread().name))

    t1 = threading.Thread(target=func1, name='t1', args=(10,))
    t2 = threading.Thread(target=func2, name='t2', args=(10,20,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
