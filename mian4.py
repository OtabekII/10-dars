import os
import threading
import re

def find_longest_sentence(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    sentences = re.split(r'[.!?]+', content)
    longest_sentence = max(sentences, key=len)
    return longest_sentence

def process_files():
    directory = os.path.dirname(os.path.abspath(__file__))
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    
    longest_sentences = []
    lock = threading.Lock()
    threads = []
    
    if txt_files:
        for file_name in txt_files:
            file_path = os.path.join(directory, file_name)
            thread = threading.Thread(target=lambda: update_longest_sentences(file_path, lock, longest_sentences))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        if longest_sentences:
            print("The longest sentence across all .txt files is:")
            print(max(longest_sentences, key=len))
    else:
        print("No .txt files found in the directory.")

def update_longest_sentences(file_path, lock, longest_sentences):
    longest_sentence = find_longest_sentence(file_path)
    with lock:
        longest_sentences.append(longest_sentence)

if __name__ == "__main__":
    process_files()