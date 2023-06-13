def ascii_encode(binary_string: str):
    binary_groups = []
    encoded_string = ''

    for i in range(0, len(binary_string), 8):
        group = binary_string[i:i + 8]
        binary_groups.append(group)

    for group in binary_groups:
        decimal_value = int(group, 2)
        ascii_char = chr(decimal_value)
        encoded_string += ascii_char

    return encoded_string
