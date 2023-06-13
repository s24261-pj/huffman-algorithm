import os
from huffman import huffman_compress, get_generated_codes
from ascii_encode import ascii_encode


def huffman_compress_file(file_path):
    try:
        with open(file_path, "r") as text_file:
            text = text_file.read()
            codes = get_generated_codes(text)
            compressed_text = huffman_compress(text)
            ascii_encoded_text = ascii_encode(compressed_text)

        compressed_file_path = "files/text-after-compress.txt"

        if os.path.exists(compressed_file_path):
            os.remove(compressed_file_path)

        with open(compressed_file_path, "w") as compressed_file:
            compressed_file.write(str(codes))
            compressed_file.write('\n')
            compressed_file.write(ascii_encoded_text)

    except IOError as error:
        print(f"File read/write error: {error}")
