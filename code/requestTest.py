import threading
import requests
import time

def worker(num):
    """thread worker function"""
    for i in range(100):
        r = requests.get('http://52.91.205.75')
        #print('Worker: ', num, ' code:', r.status_code)
    return

threads = []
start_time = time.time()
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for i in range(5):
    threads[i].join()

print("--- %s seconds ---" % (time.time() - start_time))