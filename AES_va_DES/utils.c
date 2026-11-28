#include "des.h"
void hex_to_bits(const char hex_str[16], int bits[64]) {
    for (int i = 0; i < 16; i++) {
        char hex_char = hex_str[i];
        int value;
        if (hex_char >= '0' && hex_char <= '9') {
            value = hex_char - '0';
        } else if (hex_char >= 'A' && hex_char <= 'F') {
            value = hex_char - 'A' + 10;
        } else if (hex_char >= 'a' && hex_char <= 'f') {
            value = hex_char - 'a' + 10;
        } else {
            // Invalid character, handle error
            value = 0;
        }
        for (int j = 0; j < 4; j++) {
            bits[i * 4 + j] = (value >> (3 - j)) & 1;
        }
    }
}
void bits_to_hex(const int *bits, int len, char *out_hex) {
    for (int i = 0; i < len / 4; i++) {
        int value = 0;
        for (int j = 0; j < 4; j++) {
            value = (value << 1) | bits[i * 4 + j];
        }
        if (value < 10) {
            out_hex[i] = '0' + value;
        } else {
            out_hex[i] = 'A' + (value - 10);
        }
    }
    out_hex[len / 4] = '\0'; // Null-terminate the string
}