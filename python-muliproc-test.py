from multiprocessing import Pool
import time

ncore = 20

def use_core(i):
    print("Starting %d"%i)
    time.sleep(13)
    print("Finished %d"%i)

p = Pool(ncore)
p.map(use_core, range(ncore))