def Feistel_function(input_block, subkey):
    # Split the input block into two halves
    left_half = input_block[:len(input_block)//2]
    right_half = input_block[len(input_block)//2:]
return bytes([b ^ subkey for b in right_half]) + left_half
def expand_32_to_48(    input_block):
    # Expansion permutation table for DES
    expansion_table = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32
    ]
    expanded_block = bytearray()
    for i in expansion_table:
        expanded_block.append(input_block[i - 1])
    return bytes(expanded_block)

    