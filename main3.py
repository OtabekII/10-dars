import os
import threading
import re

def count_sentences(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    sentences = re.split(r'[.!?]+', content)
    return len(sentences)

def process_files():
    directory = os.path.dirname(os.path.abspath(__file__))
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    global total_sentences
    total_sentences = 0
    lock = threading.Lock()
    threads = []
    for file_name in txt_files:
        file_path = os.path.join(directory, file_name)
        thread = threading.Thread(target=lambda: update_total_sentences(file_path, lock))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"Total number of sentences in all .txt files: {total_sentences}")

def update_total_sentences(file_path, lock):
    global total_sentences
    sentence_count = count_sentences(file_path)
    with lock:
        total_sentences += sentence_count

if __name__ == "__main__":
    process_files()