import os
import threading
import re

def count_numbers(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    numbers = re.findall(r'\d+', content)
    return len(numbers)

def process_files():
    directory = os.path.dirname(os.path.abspath(__file__))
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    global total_numbers
    total_numbers = 0
    lock = threading.Lock()
    threads = []
    for file_name in txt_files:
        file_path = os.path.join(directory, file_name)
        thread = threading.Thread(target=lambda: update_total_numbers(file_path, lock))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"total numbers: {total_numbers}")

def update_total_numbers(file_path, lock):
    global total_numbers
    number_count = count_numbers(file_path)
    with lock:
        total_numbers += number_count

if __name__ == "__main__":
    process_files()