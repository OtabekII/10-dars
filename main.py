import os
import threading

def count_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return len(content.split())

def get_total_word_count():
    directory = os.path.dirname(os.path.abspath(__file__))
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    
    total_word_count = 0
    lock = threading.Lock()
    threads = []
    
    if txt_files:
        for file_name in txt_files:
            file_path = os.path.join(directory, file_name)
            thread = threading.Thread(target=lambda: update_total_word_count(file_path, lock, total_word_count))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        print(f"Total word count: {total_word_count}")
    else:
        print("No .txt files found in the directory.")

def update_total_word_count(file_path, lock, total_word_count):
    word_count = count_words(file_path)
    with lock:
        total_word_count += word_count

if __name__ == "__main__":
    get_total_word_count()