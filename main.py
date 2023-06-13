import os
from file import huffman_compress_file

file_path = 'files/text-before-compress.txt'
compressed_file_path = "files/text-after-compress.txt"

huffman_compress_file(file_path)

file_size = os.stat(file_path).st_size
compressed_file_size = os.stat(compressed_file_path).st_size

print(f'File size BEFORE compress: {file_size} B')
print(f'File size AFTER compress: {compressed_file_size} B')
