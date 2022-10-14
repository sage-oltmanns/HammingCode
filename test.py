import unittest
from HammingFunctions import *


class TestMethods(unittest.TestCase):
    generator_matrix_4 = np.array([
        [1, 1, 0, 1],
        [1, 0, 1, 1],
        [1, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    generator_matrix_11 = np.array([
        [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ])

    parity_check_matrix_4 = np.array([
        [1, 0, 1, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1]
    ])

    parity_check_matrix_10 = np.array([
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    ])

    parity_check_matrix_12 = np.array([
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    ])

    decoding_matrix_4 = np.array([
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1]
    ])

    decoding_matrix_11 = np.array([
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ])

    def test_error_in_bit_5(self):
        correct_message = [0, 1, 1, 0, 0, 1, 1]
        # Error in bit 5
        test_message = [0, 1, 1, 0, 1, 1, 1]
        # Check the message for an error
        error_bit_arr = check_for_error(test_message, self.parity_check_matrix_4)
        # Convert the bit index to an integer
        error_bit = error_bit_to_int(error_bit_arr)
        if error_bit != 0:
            test_message = fix_error_bit(error_bit, test_message)
        self.assertTrue(test_message == correct_message)

    def test_error_in_bit_3(self):
        correct_message = [0, 1, 1, 0, 0, 1, 1]
        # Error in bit 3
        test_message = [0, 1, 0, 0, 0, 1, 1]
        # Check the message for an error
        error_bit_arr = check_for_error(test_message, self.parity_check_matrix_4)
        # Convert the bit index to an integer
        error_bit = error_bit_to_int(error_bit_arr)
        if error_bit != 0:
            test_message = fix_error_bit(error_bit, test_message)
        self.assertTrue(test_message == correct_message)

    def test_calculate_parity_bits_1_data_bit(self):
        # Num data bits
        data_bits = 1
        result = calculate_parity_bits(data_bits)
        self.assertTrue(result == 2)

    def test_calculate_parity_bits_4_data_bit(self):
        # Num data bits
        data_bits = 4
        result = calculate_parity_bits(data_bits)
        self.assertTrue(result == 3)

    def test_calculate_parity_bits_8_data_bit(self):
        # Num data bits
        data_bits = 8
        result = calculate_parity_bits(data_bits)
        self.assertTrue(result == 4)

    def test_calculate_parity_bits_11_data_bit(self):
        # Num data bits
        data_bits = 11
        result = calculate_parity_bits(data_bits)
        self.assertTrue(result == 4)

    def test_calculate_parity_bits_26_data_bit(self):
        # Num data bits
        data_bits = 26
        result = calculate_parity_bits(data_bits)
        self.assertTrue(result == 5)

    def test_calculate_parity_bits_27_data_bits(self):
        data_bits = 27
        result = calculate_parity_bits(data_bits)
        self.assertTrue(result == 6)

    def test_create_dynamic_H_4_bits(self):
        data_bits = 4
        parity_check_matrix = create_dynamic_parity_check_matrix(data_bits)
        self.assertTrue((parity_check_matrix == self.parity_check_matrix_4).all())

    def test_create_dynamic_H_10_bits(self):
        data_bits = 10
        parity_check_matrix = create_dynamic_parity_check_matrix(data_bits)
        self.assertTrue((parity_check_matrix == self.parity_check_matrix_10).all())

    def test_create_dynamic_H_12_bits(self):
        data_bits = 12
        parity_check_matrix = create_dynamic_parity_check_matrix(data_bits)
        self.assertTrue((parity_check_matrix == self.parity_check_matrix_12).all())

    def test_create_dynamic_G_4_bits(self):
        data_bits = 4
        parity_check_matrix = create_dynamic_parity_check_matrix(data_bits)
        generator_matrix = create_dynamic_generator_matrix(data_bits, parity_check_matrix)
        self.assertTrue((generator_matrix == self.generator_matrix_4).all())

    def test_create_dynamic_G_11_bits(self):
        data_bits = 11
        parity_check_matrix = create_dynamic_parity_check_matrix(data_bits)
        generator_matrix = create_dynamic_generator_matrix(data_bits, parity_check_matrix)
        self.assertTrue(((generator_matrix == self.generator_matrix_11).all()))

    def test_create_dynamic_R_4_bits(self):
        data_bits = 4
        decoding_matrix = create_dynamic_decoding_matrix(data_bits)
        self.assertTrue((decoding_matrix == self.decoding_matrix_4).all())

    def test_create_dynamic_R_11_bits(self):
        data_bits = 11
        decoding_matrix = create_dynamic_decoding_matrix(data_bits)
        self.assertTrue((decoding_matrix == self.decoding_matrix_11).all())


if __name__ == '__main__':
    unittest.main()
