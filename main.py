from huffman import huffman_compress, huffman_decompress

text = 'Ala ma kota a kot ma Ale'

compressed_text = huffman_compress(text)
print('Tekst przed kompresją:', text)
print('Tekst po kompresji:', compressed_text)

decompressed_text = huffman_decompress(text, compressed_text)
print('Tekst po dekompresji:', decompressed_text)
