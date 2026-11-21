def Feistel_function(input_block, subkey):
    # Split the input block into two halves
    left_half = input_block[:len(input_block)//2]
    right_half = input_block[len(input_block)//2:]

    