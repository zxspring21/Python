import multiprocessing as mp
#共享內存，可被每個CPU使用，Float8
value = mp.Value('d',1)
#只能是一維的列表，int2
array = mp.Array('i',[1,2,3])
