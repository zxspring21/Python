import multiprocessing as mp
import threading
import time
from queue import Queue
def multithreading():
   q = Queue()
   threads = []
   data = [[1,2,3],[2,3,4],[3,4,5],[4,5,6]]
   for i in range(4):
       t = threading.Thread(target = thread_job,args=(data[i],q))
       t.start()
       threads.append(t)
   for thread in threads:
       thread.join()
   results=[]
   for _ in range(4):
       results.append( q.get() )
   print(results)
    
def thread_job(l,q):
    for i in range(len(l)):
       l[i] = l[i]**2
    q.put(l)
def proecess_job():
    print('aa')
    
def main():

    p1=mp.Process(target = proecess_job)
    multithreading()
    

    p1.start()
    p1.join()

if __name__ == '__main__':
    main()
