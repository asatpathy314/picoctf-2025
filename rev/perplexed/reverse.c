#include <stdio.h>
#include <string.h>

int main() {
    unsigned char enc_flag[] = {
        0xe1, 0xa7, 0x1e, 0xf8, 0x75, 0x23, 0x7b, 0x61,
        0xb9, 0x9d, 0xfc, 0x5a, 0x5b, 0xdf, 0x69, 0xd2,
        0xfe, 0x1b, 0xed, 0xf4, 0xed, 0x67, 0xf4
    };
    
    char flag[28] = {0}; // 27 chars + null terminator
    int flag_idx = 0;
    int bit_idx = 0;
    
    for (int i = 0; i < 23; i++) {
        for (int j = 0; j < 8; j++) {
            // Get the bit from enc_flag
            int bit = (enc_flag[i] >> (7 - j)) & 1;
            
            // Set the bit in our flag
            flag[flag_idx] |= (bit << (7 - bit_idx));
            
            bit_idx++;
            if (bit_idx == 8) {
                bit_idx = 0;
                flag_idx++;
            }
            
            if (flag_idx >= 27)
                break;
        }
    }
    
    printf("Flag: %s\n", flag);
    return 0;
}
