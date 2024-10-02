#include <stdio.h>
#include <stdlib.h>

// Function to calculate checksum
__declspec(dllexport) int calculate_checksum(const char* buffer, size_t size) {
    unsigned char sum = 0;

    // Sum all bytes except the last one
    for (size_t i = 0; i < size - 1; i++) {
        sum += (unsigned char)buffer[i];
    }

    return sum; // Return sum as unsigned char (wraps automatically)
}
