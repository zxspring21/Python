#pool
import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    #map and async區別
    pool = mp.Pool(processes=2)
    #map可放入很多疊代的參數，自動分配給每一個進程，
    #定義了多少個進程就給多少個進程
    res = pool.map(job,range(10))
    
    print(res)
    res = pool.apply_async(job,(2,) )
    print(res.get())
    #apply_async一次只能在一個進程裡算一個東西，把任務推給那一個進程，
    #若想達到map效果可以用疊代的方式，然後再用疊代把他的值傳出來
    multi_res = [pool.apply_async(job,(i,)) for i in range(10)]
    print([res.get() for res in multi_res])
    
    
    
if __name__=='__main__':
    multicore()
