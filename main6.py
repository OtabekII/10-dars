import os
import requests

def download_images_from_urls(image_urls_list):
    for i, url in enumerate(image_urls_list):
        response = requests.get(url)
        if response.status_code == 200:
            filename = f'image_{i+1}.jpg'
            file_path = os.path.join('path/to/save/directory', filename)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f'Image {i+1} downloaded successfully.')
        else:
            print(f'Failed to download image {i+1}.')

# Example usage
image_urls = [
    'https://example.com/image1.jpg',
    'https://example.com/image2.jpg',
    'https://example.com/image3.jpg',
    'https://example.com/image4.jpg',
    'https://example.com/image5.jpg'
]

download_images_from_urls(image_urls)