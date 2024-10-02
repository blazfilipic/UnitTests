#include <stdio.h>
#include <stdlib.h>

// Function to calculate checksum
__declspec(dllexport) int calculate_checksum(const char* buffer, size_t size) {
    unsigned char sum = 0;

    // Sum all bytes except the last one
    for (size_t i = 0; i < size - 1; i++) {
        sum += (unsigned char)buffer[i];
    }
    // Used modulo 256 for checksum (no need for %256, because we have unsigned char)
    return sum; // Return sum as unsigned char (wraps automatically)
}
