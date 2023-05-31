from heap import build_min_heap, get_min, insert


class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None


def calculate_frequencies(text):
    result = {}

    for letter in text:
        if letter in result:
            result[letter].frequency += 1
        else:
            result[letter] = Node(letter, 1)

    return list(result.values())


def build_tree(frequencies):
    heap_array = frequencies
    build_min_heap(heap_array)

    while len(heap_array) > 1:
        first_smallest_freq = get_min(heap_array)
        second_smallest_freq = get_min(heap_array)

        merged_frequency = first_smallest_freq.frequency + second_smallest_freq.frequency
        merged_node = Node(None, merged_frequency)
        merged_node.left = first_smallest_freq
        merged_node.right = second_smallest_freq

        insert(heap_array, merged_node)

    tree = heap_array[0]

    return tree


def get_generated_codes(text):
    frequencies = calculate_frequencies(text)
    tree = build_tree(frequencies)
    codes = {}
    generate_codes(tree, "", codes)

    return codes


def generate_codes(node, current_code, codes):
    if node.char:
        codes[node.char] = current_code
        return

    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)


def compress_text(text, codes):
    compressed_text = ""

    for char in text:
        compressed_text += codes[char]

    return compressed_text


def huffman_compress(text):
    codes = get_generated_codes(text)
    compressed_text = compress_text(text, codes)

    return compressed_text


# for tests to check the results of huffman_compress
def huffman_decompress(text, compressed_text):
    frequencies = calculate_frequencies(text)
    tree = build_tree(frequencies)
    current_node = tree
    decompressed_text = ""

    for bit in compressed_text:
        if bit == "1":
            current_node = current_node.right
        else:
            current_node = current_node.left

        if current_node.char:
            decompressed_text += current_node.char
            current_node = tree

    return decompressed_text
