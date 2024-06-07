import os
import threading
import re

def clean_sentences(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    cleaned_sentences = [re.sub(r'[.!?]+', '.', sentence.strip()) for sentence in re.split(r'[.!?]+', content)]
    return cleaned_sentences

def process_files():
    directory = os.path.dirname(os.path.abspath(__file__))
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    
    cleaned_sentences = []
    lock = threading.Lock()
    threads = []
    
    if txt_files:
        for file_name in txt_files:
            file_path = os.path.join(directory, file_name)
            thread = threading.Thread(target=lambda: update_cleaned_sentences(file_path, lock, cleaned_sentences))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        if cleaned_sentences:
            for sentence in cleaned_sentences:
                print(sentence)
    else:
        print("No .txt files found in the directory.")

def update_cleaned_sentences(file_path, lock, cleaned_sentences):
    cleaned_sentence_list = clean_sentences(file_path)
    with lock:
        cleaned_sentences.extend(cleaned_sentence_list)

if __name__ == "__main__":
    process_files()