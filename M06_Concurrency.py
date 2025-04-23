#Lexus Aguilera
#M06 Programming Assignment

#13.1
import datetime

today = datetime.date.today()
with open('today.txt', 'w') as file:
    file.write(today.isoformat())

#13.2
with open('today.txt', 'r') as file:
    today_string = file.read()

#13.3
parsed_date = datetime.datetime.strptime(today_string, '%Y-%m-%d').date()
print(parsed_date)
break

#15.1
import multiprocessing
import time
import random
from datetime import datetime

def show_time():
    wait_time = random.random()
    time.sleep(wait_time)
    print(f"Process {multiprocessing.current_process().name} - Time: {datetime.now().time()}")

if __name__ == '__main__':
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=show_time, name=f'Process-{i+1}')
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
