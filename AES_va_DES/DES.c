#ifndef DES_H
#define DES_H

#include <math.h>

// Các hàm chuyển đổi Hex <-> Mảng bit (dùng pow, fmod, floor từ math.h)
void hex_to_bits(const char hex_str[16], int bits[64]);
void bits_to_hex(const int *bits, int len, char *out_hex);
int str_equal(const char *s1, const char *s2, int len);

// File permutation.c
void permute(const int *in_bits, int *out_bits, const int *table, int table_len);
void initial_permutation(const int in_64[64], int out_64[64]);
void final_permutation(const int in_64[64], int out_64[64]);
void p_box_permutation(const int in_32[32], int out_32[32]);

// File sbox.c
void expand_32_to_48(const int R[32], int expanded[48]);
void sbox_substitution(const int in_48[48], int out_32[32]);

// File key_schedule.c
void left_shift_bits(int *bits, int len, int shift);
void generate_subkeys(const int key_bits[64], int subkeys[16][48]);
// feistel.c: Hàm Feistel 1 vòng
void feistel_function(const inst R[32], const int subkey[48], int out_32[32]);

// des_encrypt.c: Mã hóa DES
void desencrypt(const char plain_hex[16], const char key_hex[16], char out_ciher[17], int print_trace);

// des_decrypt.c: Giải mã DES
void desdecrypt(const char cipher_hex[16], const char key_hex[16], char out_plin[17], int print_trace);

#endif