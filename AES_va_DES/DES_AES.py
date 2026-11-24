IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

FP = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

DES_S_BOX = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
       26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
       51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def hex_to_bits(hex_str):
    val = int(hex_str, 16)
    return [int (b) for b in f"{val:064b}"]
def bits_to_hex(bits):
    val = int("".join(map(str, bits)), 2)
    return f"{val:0{len(bits)//4}X}"
def expand_32_to_48(R):
    expanded = []
    for i in range(8):
        s = i * 4
        expanded.extend([R[(s - 1) % 32]] + R[s:s+4] + [R[(s + 4) % 32]])
    return expanded
def permute(bits, table):
    return [bits[i - 1] for i in table]
def generate_subkeys(key_bits):
    k56 = permute(key_bits, PC1)
    C, D = k56[:28], k56[28:]
    subkeys = []
    for s in SHIFT:
        C = C[s:] + C[:s]
        D = D[s:] + D[:s]
        subkeys.append(permute(C + D, PC2))
    return subkeys
def feistel(R, subkey):
    expanded = expand_32_to_48(R)
    xored = [a ^ b for a, b in zip(expanded, subkey)]
    sbox_out = []
    for i in range(8):
        chunk = xored[i*6:(i+1)*6]
        row = (chunk[0] << 1) + chunk[5]
        col = (chunk[1] << 3) + (chunk[2] << 2) + (chunk[3] << 1) + chunk[4]
        val = DES_S_BOX[i][row][col]
        sbox_out.extend([(val >> shift) & 1 for shift in (3, 2, 1, 0)])
    return permute(sbox_out, P)
def des_encrypt_trace(plain_hex, key_hex):
    logs = []
    bits = hex_to_bits(plain_hex)
    ip_bits = permute(bits, IP)
    L, R = ip_bits[:32], ip_bits[32:]
    logs.append(f"Sau hoán vị IP     : L0 = {bits_to_hex(L)} | R0 = {bits_to_hex(R)}")
    logs.append("-" * 65)

    subkeys = generate_subkeys(hex_to_bits(key_hex))
    for r in range(16):
        f_res = feistel(R, subkeys[r])
        new_L = R
        new_R = [a ^ b for a, b in zip(L, f_res)]
        L, R = new_L, new_R
        logs.append(f"Vòng {r+1:02d} | K{r+1:02d}={bits_to_hex(subkeys[r])} | L={bits_to_hex(L)} | R={bits_to_hex(R)}")

    cipher_bits = permute(R + L, FP)
    cipher_hex = bits_to_hex(cipher_bits)
    logs.append("-" * 65)
    logs.append(f"Bản mã cuối cùng (Sau FP): {cipher_hex}\n")
    return cipher_hex, "\n".join(logs)
def des_decrypt(cipher_hex, key_hex):
    bits = hex_to_bits(cipher_hex)
    ip_bits = permute(bits, IP)
    L, R = ip_bits[:32], ip_bits[32:]
    # Giải mã DES dùng khóa con đảo ngược từ K16 về K1
    subkeys = generate_subkeys(hex_to_bits(key_hex))[::-1]
    for r in range(16):
        f_res = feistel(R, subkeys[r])
        L, R = R, [a ^ b for a, b in zip(L, f_res)]
    plain_bits = permute(R + L, FP)
    return bits_to_hex(plain_bits)
   #Thuật toán AES_128
   # ==============================================================================
def gmul(a, b):
    p = 0
    for i in range(8):
        if b & 1:
            p ^= a
        hi = a & 0x80
        a = (a << 1) & 0xff
        if hi:
            a ^= 0x1b
        b >>= 1
    return p
def bytes_to_hex(byte_list):
    return "".join(f"{b:02X}" for b in byte_list)
def gf_inverse(a):
    if a == 0:
        return 0
    res, base, exp = 1, a, 254
    while exp > 0:
        if exp & 1:
            res = gmul(res, base)
        base = gmul(base, base)
        exp >>= 1
    return res
def generate_sbox():
    sbox = []
    rotl = lambda x, s: ((x << s) | (x >> (8 - s))) & 0xff
    for i in range(256):
        inv = gf_inverse(i)
        sbox.append(inv ^ rotl(inv, 1) ^ rotl(inv, 2) ^ rotl(inv, 3) ^ rotl(inv, 4) ^ 0x63)
    return sbox
AES_S_BOX = generate_sbox()
RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]

def key_expansion(key_bytes):
    w = [list(key_bytes[i:i+4]) for i in range(0, 16, 4)]
    for i in range(4, 44):
        temp = list(w[i - 1])
        if i % 4 == 0:
            temp = [AES_S_BOX[b] for b in (temp[1:] + temp[:1])]  # <-- Gọi AES_S_BOX
            temp[0] ^= RCON[i // 4 - 1]
        w.append([w[i - 4][j] ^ temp[j] for j in range(4)])
    return [sum(w[4*r:4*(r+1)], []) for r in range(11)]

def add_round_key(state, round_key):
    return [s ^ k for s, k in zip(state, round_key)]
def shift_rows(s):
    return [
        s[0], s[5], s[10], s[15],
        s[4], s[9], s[14], s[3],
        s[8], s[13], s[2], s[7],
        s[12], s[1], s[6], s[11]
    ]

def mix_columns(s):
    res = [0] * 16
    for c in range(4):
        i = c * 4
        res[i]   = gmul(0x02, s[i]) ^ gmul(0x03, s[i+1]) ^ s[i+2] ^ s[i+3]
        res[i+1] = s[i] ^ gmul(0x02, s[i+1]) ^ gmul(0x03, s[i+2]) ^ s[i+3]
        res[i+2] = s[i] ^ s[i+1] ^ gmul(0x02, s[i+2]) ^ gmul(0x03, s[i+3])
        res[i+3] = gmul(0x03, s[i]) ^ s[i+1] ^ s[i+2] ^ gmul(0x02, s[i+3])
    return res

def aes128_encrypt_trace(plain_hex, key_hex):
    logs = []
    state = list(bytes.fromhex(plain_hex))
    round_keys = key_expansion(list(bytes.fromhex(key_hex)))

    state = add_round_key(state, round_keys[0])
    logs.append(f"Vòng 00 | RoundKey={bytes_to_hex(round_keys[0])} | State={bytes_to_hex(state)}")
    logs.append("-" * 82)

    for r in range(1, 10):
        state = [AES_S_BOX[b] for b in state]  
        sub_hex = bytes_to_hex(state)
        state = shift_rows(state)
        shift_hex = bytes_to_hex(state)
        state = mix_columns(state)
        mix_hex = bytes_to_hex(state)
        state = add_round_key(state, round_keys[r])
        logs.append(f"Vòng {r:02d} | SubBytes={sub_hex} | ShiftRows={shift_hex}")
        logs.append(f"        | MixCols ={mix_hex} | AddRKey  ={bytes_to_hex(state)}")

    state = [AES_S_BOX[b] for b in state]  
    sub_hex = bytes_to_hex(state)
    state = shift_rows(state)
    shift_hex = bytes_to_hex(state)
    state = add_round_key(state, round_keys[10])
    cipher_hex = bytes_to_hex(state)
    logs.append(f"Vòng 10 | SubBytes={sub_hex} | ShiftRows={shift_hex}")
    logs.append("-" * 82)
    logs.append(f"Bản mã cuối cùng (Ciphertext): {cipher_hex}\n")
    return cipher_hex, "\n".join(logs)
INV_AES_S_BOX = [AES_S_BOX.index(i) for i in range(256)]

def inv_shift_rows(s):
    return [
        s[0], s[13], s[10], s[7],
        s[4], s[1], s[14], s[11],
        s[8], s[5], s[2], s[15],
        s[12], s[9], s[6], s[3]
    ]

def inv_mix_columns(s):
    res = [0] * 16
    for c in range(4):
        i = c * 4
        res[i]   = gmul(0x0e, s[i]) ^ gmul(0x0b, s[i+1]) ^ gmul(0x0d, s[i+2]) ^ gmul(0x09, s[i+3])
        res[i+1] = gmul(0x09, s[i]) ^ gmul(0x0e, s[i+1]) ^ gmul(0x0b, s[i+2]) ^ gmul(0x0d, s[i+3])
        res[i+2] = gmul(0x0d, s[i]) ^ gmul(0x09, s[i+1]) ^ gmul(0x0e, s[i+2]) ^ gmul(0x0b, s[i+3])
        res[i+3] = gmul(0x0b, s[i]) ^ gmul(0x0d, s[i+1]) ^ gmul(0x09, s[i+2]) ^ gmul(0x0e, s[i+3])
    return res

def aes128_decrypt(cipher_hex, key_hex):
    state = list(bytes.fromhex(cipher_hex))
    round_keys = key_expansion(list(bytes.fromhex(key_hex)))
    state = add_round_key(state, round_keys[10])
    state = inv_shift_rows(state)
    state = [INV_AES_S_BOX[b] for b in state]
    for r in range(9, 0, -1):
        state = add_round_key(state, round_keys[r])
        state = inv_mix_columns(state)
        state = inv_shift_rows(state)
        state = [INV_AES_S_BOX[b] for b in state]
    stte = add_round_key(state, round_keys[0])
    return bytes_to_hex(state)