import unittest
from HammingFunctions import *

class TestMethods(unittest.TestCase):
    G = [
        [1, 1, 0, 1],
        [1, 0, 1, 1],
        [1, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]

    H = [
        [1, 0, 1, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1]
    ]
    
    R = [
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1]
    ]

    def test_error_in_bit_5(self):
        correct_message = [0, 1, 1, 0, 0, 1, 1]
        # Error in bit 5
        test_message = [0, 1, 1, 0, 1, 1, 1]
        # Check the message for an error
        error_bit_arr = check_for_error(test_message, self.H)
        # Convert the bit index to an integer
        error_bit = error_bit_to_int(error_bit_arr)
        if(error_bit != 0):
            test_message = fix_error_bit(error_bit, test_message)
        self.assertTrue(test_message == correct_message)
    
    def test_error_in_bit_3(self):
        correct_message = [0, 1, 1, 0, 0, 1, 1]
        # Error in bit 3
        test_message = [0, 1, 0, 0, 0, 1, 1]
        # Check the message for an error
        error_bit_arr = check_for_error(test_message, self.H)
        # Convert the bit index to an integer
        error_bit = error_bit_to_int(error_bit_arr)
        if(error_bit != 0):
            test_message = fix_error_bit(error_bit, test_message)
        self.assertTrue(test_message == correct_message)