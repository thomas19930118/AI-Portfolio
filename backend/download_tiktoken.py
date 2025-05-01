# backend/download_tiktoken.py
import os
import requests
from pathlib import Path

def download_tiktoken_files():
    # Create cache directory
    cache_dir = Path.home() / '.cache' / 'tiktoken'
    cache_dir.mkdir(parents=True, exist_ok=True)

    # File to download
    file_url = 'https://openaipublic.blob.core.windows.net/encodings/cl100k_base.tiktoken'
    local_file = cache_dir / 'cl100k_base.tiktoken'

    # Set explicit timeout and headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(file_url, timeout=30, headers=headers)
        response.raise_for_status()
        
        with open(local_file, 'wb') as f:
            f.write(response.content)
        print(f"Successfully downloaded tiktoken file to {local_file}")
    except Exception as e:
        print(f"Error downloading tiktoken file: {e}")

if __name__ == '__main__':
    download_tiktoken_files()