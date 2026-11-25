#ifndef DES_H
#define DES_H

#include <math.h>

// Các hàm chuyển đổi Hex <-> Mảng bit (dùng pow, fmod, floor từ math.h)
void hex_to_bits(const char hex_tr[16], int bits[64]);
void bits_to_hex(const int bit[64], int len, char out_hex);
int str