#include <stdint.h>
#include <stdio.h>

#define WORD_LENGTH 32


uint32_t reverse_bits(uint32_t value, int num_bits) {
    uint32_t reversed = 0;
    for (int i = 0; i < num_bits; i++) {
        reversed |= ((value >> i) & 1) << (num_bits - 1 - i);
    }
    return reversed;
}

uint32_t sbox_function(uint32_t word, int round_num, uint32_t sboxes[8][16]) {
    uint32_t input = word;
    uint32_t output = 0;
    for (int idx = 0; idx < 8; idx++) {
        uint32_t rearrange = (input >> (7 - idx) * 4) & 0xF;
        rearrange = reverse_bits(rearrange, 4);
        uint32_t temp = sboxes[round_num % 8][rearrange];
        uint32_t ba_temp = reverse_bits(temp, 4);
        output |= ba_temp << ((7 - idx) * 4);
    }
    return output;
}

int main() {
    uint32_t word = 0b00111111110000101000001110110100;
    uint32_t sboxes[8][16] = {
	{3, 8,15, 1,10, 6, 5,11,14,13, 4, 2, 7, 0, 9,12}, 
	{15,12, 2, 7, 9, 0, 5,10, 1,11,14, 8, 6,13, 3, 4}, 
	{8, 6, 7, 9, 3,12,10,15,13, 1,14, 4, 0,11, 5, 2},
	{0,15,11, 8,12, 9, 6, 3,13, 1, 2, 4,10, 7, 5,14},
	{1,15, 8, 3,12, 0,11, 6, 2, 5, 4,10, 9,14, 7,13},
	{15, 5, 2,11, 4,10, 9,12, 0, 3,14, 8,13, 6, 7, 1},
	{7, 2,12, 5, 8, 4, 6,11,14, 9, 1,15,13, 3,10, 0},
	{1,13,15, 0,14, 8, 2,11, 7, 4,12,10, 9, 3, 5, 6},
    };
    sbox_function(word, 0, sboxes); 
    return 0;
}