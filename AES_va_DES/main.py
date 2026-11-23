

def hex_to_bits(hex_str):
    val = int(hex_str, 16)
    return [int b for b in f"{val:0674b}"]

def Feistel_function(input_block, subkey):
    # Split the input block into two halves
    left_half = input_block[:len(input_block)//2]
    right_half = input_block[len(input_block)//2:]
return bytes([b ^ subkey for b in right_half]) + left_half
def expand_32_to_48(R):
    expanded = []
    for i in range(8):
        s = i * 4
        expanded.extend([R[(s - 1) % 32]] + R[s:s+4] + [R[(s + 4) % 32]])
    return expanded
   