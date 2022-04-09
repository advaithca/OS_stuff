import threading

N = int(input("Input buffer size :: "))
buff = [0] * N

full = threading.Semaphore(0)
empty = threading.Semaphore(N)

def produce():
	print("Produced one item")
	return 1

def producer():
    front = 0
    while True:
        x = produce()
        empty.acquire()
        buff[front] = x
        full.release()
        front = (front + 1) % N

def consume(y):
	print("One item consumed")

def consumer():
    rear = 0
    while True:
        full.acquire()
        y = buff[rear]
        empty.release()
        consume(y)
        rear = (rear + 1) % N


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()
