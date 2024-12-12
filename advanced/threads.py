import threading
import time


def process_request(request_id):
    print(f"Processing request {request_id}")
    time.sleep(3)
    print(f"Request {request_id} processed")


threads = []

for i in range(3):
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

print("Threads", threads)

for thread in threads:
    thread.join()

print("All requests processed")
