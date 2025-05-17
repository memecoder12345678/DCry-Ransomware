OUTER_XOR_KEY = 42


def is_letter(c):
    return (c >= 65 and c <= 90) or (c >= 97 and c <= 122)


def get_base(c):
    if c >= 65 and c <= 90:
        return 65
    elif c >= 97 and c <= 122:
        return 97
    return 0


def calculate_shift(index):
    shift_val = index * 7 + (index // 3) + (index % 11) + ((index >> 2) & 0x7)
    temp_shift = shift_val + (index % 5)
    return (temp_shift % 26) + 1


def ex42(plaintext):
    if not isinstance(plaintext, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    len_plain = len(plaintext)
    output = bytearray(len_plain)
    for i in range(len_plain):
        current_byte = plaintext[i]
        if is_letter(current_byte):
            base = get_base(current_byte)
            shift = calculate_shift(i)
            pos_in_alphabet = current_byte - base
            shifted_pos_in_alphabet = (pos_in_alphabet + shift) % 26
            value_before_final_xor = shifted_pos_in_alphabet + base
        else:
            value_before_final_xor = current_byte
        value_before_final_xor = value_before_final_xor % 256
        encoded_byte = value_before_final_xor ^ OUTER_XOR_KEY
        encoded_byte = encoded_byte % 256
        output[i] = encoded_byte
    return bytes(output)


def dx42(encoded):
    if not isinstance(encoded, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    len_enc = len(encoded)
    output = bytearray(len_enc)
    for i in range(len_enc):
        encoded_byte = encoded[i]
        value_before_final_xor = encoded_byte ^ OUTER_XOR_KEY
        value_before_final_xor = value_before_final_xor % 256
        if is_letter(value_before_final_xor):
            base = get_base(value_before_final_xor)
            shift = calculate_shift(i)
            pos_in_alphabet = value_before_final_xor - base
            decoded_pos_in_alphabet = (pos_in_alphabet - shift + 26) % 26
            decoded_char = decoded_pos_in_alphabet + base
            output[i] = decoded_char
        else:
            output[i] = value_before_final_xor
    return bytes(output)
