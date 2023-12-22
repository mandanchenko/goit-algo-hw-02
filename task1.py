import time
from queue import Queue

my_queue = Queue()


def generate_request():
    new_request = f"Request № {int(time.time())}"
    my_queue.put(new_request)
    print(f"Generated request: {new_request}")

def process_request():
    if not my_queue.empty():
        print(f"Processing request: {my_queue.get()}")
    else:
        print("Queue is empty. No requests to process.")

if __name__ == "__main__":
    
    while True:
        generate_request()
        process_request()
        time.sleep(3)
        exit_choice = input("Do you want to exit? (y/n): ")
        if exit_choice.lower() == 'y':
            break

