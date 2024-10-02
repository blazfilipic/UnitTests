import ctypes
import unittest

# Load the DLL
checksum_lib = ctypes.CDLL('./checksum.dll')

# Specify argument and return types for the function
checksum_lib.calculate_checksum.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.c_size_t]
checksum_lib.calculate_checksum.restype = ctypes.c_int

class TestChecksum(unittest.TestCase):

    def test_checksum(self):
        # Test case with a known checksum
        buffer = b"\x01\x02\x03\x04\x0A"  # Known data
        size = len(buffer)
        # Calculate the expected checksum
        expected_checksum = sum(buffer[:-1]) % 256  # Exclude the last byte
        # Get the last byte which is supposed to be the checksum
        actual_checksum = buffer[-1]
        # Call the function to calculate checksum
        calculated_checksum = checksum_lib.calculate_checksum(buffer, size)
        self.assertEqual(calculated_checksum, expected_checksum)
        self.assertEqual(calculated_checksum, actual_checksum)

    def test_checksum_with_specific_data(self):
        # Test case with specific data
        buffer = b"\x0a\xd0\x00\x05\x2e\x00\x00\x00\x00\x01\x00\x00\x38\x10\x01\x00\x57"
        size = len(buffer)
        # Calculate the expected checksum
        expected_checksum = sum(buffer[:-1]) % 256  # Exclude the last byte
        # Get the last byte which is supposed to be the checksum
        actual_checksum = buffer[-1]
        # Call the function to calculate checksum
        calculated_checksum = checksum_lib.calculate_checksum(buffer, size)
        self.assertEqual(calculated_checksum, expected_checksum)
        self.assertEqual(calculated_checksum, actual_checksum)

    def test_checksum_with_zero_sum(self):
        # Test case with input that results in a zero checksum
        buffer = b"\x00\x00"  # Example input that will sum to zero
        size = len(buffer)
        # Calculate the expected checksum
        expected_checksum = sum(buffer[:-1]) % 256  # Exclude the last byte
        # Get the last byte which is supposed to be the checksum
        actual_checksum = buffer[-1]
        # Call the function to calculate checksum
        calculated_checksum = checksum_lib.calculate_checksum(buffer, size)
        self.assertEqual(calculated_checksum, expected_checksum)
        self.assertEqual(calculated_checksum, actual_checksum)

if __name__ == '__main__':
    unittest.main(verbosity=2)  # Set verbosity level to 2 for detailed output
