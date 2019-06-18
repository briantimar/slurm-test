from multiprocessing import Pool, Process
import time

ncore = 10

def use_core(i):
    print("Starting %d"%i)
    time.sleep(13)
    print("Finished %d"%i)

jobs = []
for j in range(ncore):
    p=Process(target=use_core, args=(j,))
    jobs.append(p)
    p.start()
    
