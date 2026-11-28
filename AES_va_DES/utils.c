#include "des.h"

void hex_to_bits(const char hex_str[16], int bits[64]) {
    for (int i = 0; i < 16; i++) {
        char c = hex_str[i];
        int val = 0;
        if (c >= '0' && c <= '9') val = c - '0';
        else if (c >= 'a' && c <= 'f') val = c - 'a' + 10;
        else if (c >= 'A' && c <= 'F') val = c - 'A' + 10;

        for (int b = 0; b < 4; b++) {
            bits[i * 4 + b] = (val >> (3 - b)) & 1;
        }
    }
}

void bits_to_hex(const int *bits, int len, char *out_hex) {
    int hex_len = len / 4;
    for (int i = 0; i < hex_len; i++) {
        int val = (bits[i * 4] << 3) | (bits[i * 4 + 1] << 2) |
                  (bits[i * 4 + 2] << 1) | bits[i * 4 + 3];
        if (val < 10) out_hex[i] = (char)('0' + val);
        else out_hex[i] = (char)('A' + (val - 10));
    }
    out_hex[hex_len] = '\0';
}

int str_equal(const char *s1, const char *s2, int len) {
    for (int i = 0; i < len; i++) {
        if (s1[i] != s2[i]) return 0;
    }
    return 1;
}