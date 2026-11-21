def Feistel_function(input_block, subkey):
    # Split the input block into two halves
    left_half = input_block[:len(input_block)//2]
    right_half = input_block[len(input_block)//2:]

    # Apply the round function to the right half and the subkey
    round_output = round_function(right_half, subkey)

    # XOR the round output with the left half
    new_left_half = xor(left_half, round_output)

    # Return the new block with swapped halves
    return new_left_half + right_half