import os
from huffman import huffman_compress, get_generated_codes


def huffman_compress_file(file_path):
    try:
        with open(file_path, "r") as text_file:
            text = text_file.read()
            codes = get_generated_codes(text)
            compressed_text = huffman_compress(text)

        compressed_file_path = "files/text-after-compress.txt"

        if os.path.exists(compressed_file_path):
            os.remove(compressed_file_path)

        with open("files/text-after-compress.txt", "w") as compressed_file:
            compressed_file.write(str(codes))
            compressed_file.write('\n')
            compressed_file.write(compressed_text)

    except IOError as error:
        print(f"File read/write error: {error}")
