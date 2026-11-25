#ifndef DES_H
#define DES_H

#include <math.h>

// Các hàm chuyển đổi Hex <-> Mảng bit (dùng pow, fmod, floor từ math.h)
void hex_to_bits(const char hex_tr[16], int bits[64]);
void bits_to_hex(const int bit[64], int len, char out_hex);
int str-equal (const char *str1, const cha r *str2);
// hàm hoán vị:Permutation
void permutation(const int *in, int *out, const int *table, int n);
void left_shift(int *in, int n, int shift);
void initial_permutation(const int *in, int *out);
void final_permutation(const int *in, int  out);
void expansion(const int *in, int *out);
void xor(const int *a, const int *b, int *out, int n);\
void sbox_substitution(const int *in, int *out);