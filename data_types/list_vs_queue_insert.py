import time
from collections import deque

def run_and_time(times, data_type=""):
    def decorator(func):
        def wrapper(*args):
            start = time.perf_counter()
            for _ in range(times):
                func(*args)
            end = time.perf_counter()
            return f"Time taken to append to {data_type} {times} times: {end - start} seconds"
        return wrapper
    return decorator

l = []
dq = deque()

times = 1000000000

@run_and_time(times, "list")
def append_to_list():
    l.append(256)

@run_and_time(times, "queue")
def append_to_queue():
    dq.append(256)

result_list = append_to_list()
result_q = append_to_queue()

print(result_list, result_q, sep="\n")

# >>> Time taken to append to list 1000000000 times: 80.22499270000117 seconds
# >>> Time taken to append to queue 1000000000 times: 70.74587310000061 seconds



