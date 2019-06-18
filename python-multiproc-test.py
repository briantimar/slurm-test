from multiprocessing import Pool, Process
import time

ncore = 10
dt = 30

def use_core(i):
    print("Starting %d"%i)
    t = time.time()
    n = 0
    #busywork
    while time.time() -t < dt:
        n += 1
    print("Finished %d"%i)

jobs = []
for j in range(ncore):
    p=Process(target=use_core, args=(j,))
    jobs.append(p)
    p.start()

