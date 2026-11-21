def Feistel_function(input_block, subkey):
    # Split the input block into two halves
    left_half = input_block[:len(input_block)//2]
    right_half = input_block[len(input_block)//2:]
return bytes([b ^ subkey for b in right_half]) + left_half
def expand_32_to_48(    input_block):
    # Expansion permutation table for DES
    #expansion_table = 
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32
    expanded = []
    for i in range(8):
        # Vị trí 4 bit gốc của nhóm thứ i
        start = i * 4
        # Bit mượn từ cuối nhóm trước (dùng % 32 để bit 0 mượn được bit 31)
        left_bit = R[(start - 1) % 32]
        # 4 bit ở giữa
        middle_bits = R[start : start + 4]
        # Bit mượn từ đầu nhóm sau (dùng % 32 để bit 31 mượn được bit 0)
        right_bit = R[(start + 4) % 32]
        
        expanded.extend([left_bit] + middle_bits + [right_bit])
    return expanded
def permute_bitwise(value, table, in_bits):
    result = 0
    for pos in table:
        # Lấy bit tại vị trí pos (đếm từ trái sang, bắt đầu từ 1)
        bit = (value >> (in_bits - pos)) & 1
        # Đẩy bit đó vào kết quả mới
        result = (result << 1) | bit
    return result
    