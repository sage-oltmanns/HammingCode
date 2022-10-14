from cmath import sqrt
import numpy as np
import random as rnd


def check_for_error(parity_message, parity_check_matrix):
    '''
    :param parity_message:
    :param parity_check_matrix:
    :return:
    '''
    # Cool numpy stuff
    error_bit = np.matmul(parity_check_matrix, parity_message)

    # Flip the bit to a 0 or a 1 based on odd or even
    for i in range(0, len(error_bit)):
        if error_bit[i] % 2 == 0:
            error_bit[i] = 0
        else:
            error_bit[i] = 1
    # Reverse the list (easier for matrix multiplication later)
    return error_bit[::-1]


def calculate_parity_bits(data_bits):
    parity_bits = 0
    while pow(2, parity_bits) <= data_bits + parity_bits:
        parity_bits += 1
    return parity_bits


def corrupt_a_bit(correct_message):
    corrupt_bit = rnd.randint(0, len(correct_message))
    received_message = correct_message.copy()
    if correct_message[corrupt_bit] == 0:
        received_message[corrupt_bit] = 1
    else:
        received_message[corrupt_bit] = 0
    return received_message


def create_dynamic_parity_check_matrix(data_bits):
    # Num rows of parity_check_matrix
    parity_bits = calculate_parity_bits(data_bits)
    # Num columns of parity_check_matrix
    total_bits = get_full_message_length(data_bits)
    parity_check_matrix = [[0] * total_bits] * parity_bits
    for i in range(0, parity_bits):
        num_ones = pow(2, i)
        num_ones_arr = [1] * num_ones
        row = parity_check_matrix[i]
        start_j = 0
        while start_j < total_bits:
            if start_j == num_ones - 1:
                last_j = start_j + num_ones
                parity_check_matrix[i] = row[:start_j] + num_ones_arr + row[last_j:]
                start_j = num_ones + last_j
            elif start_j > num_ones - 1:
                last_j = start_j + num_ones
                parity_check_matrix[i] = row[:start_j] + num_ones_arr + row[last_j:]
                start_j = last_j + num_ones
            else:
                start_j += 1
            row = parity_check_matrix[i]
        parity_check_matrix[i] = np.resize(parity_check_matrix[i], total_bits)
    return parity_check_matrix


def create_dynamic_generator_matrix(data_bits, parity_check_matrix):
    # Get the length of the parity message
    total_bits = get_full_message_length(data_bits)
    # Initialize code generator matrix
    code_generator_matrix = np.zeros((total_bits, data_bits), dtype=int)

    last_parity_row = 0
    last_data_bit_mask = 0
    for row in range(0, total_bits):
        if pow(2, last_parity_row) - 1 != row:
            code_generator_matrix[row][last_data_bit_mask] = 1
            last_data_bit_mask += 1
        else:
            parity_row = np.zeros((1, data_bits), dtype=int)
            last_parity = 0
            last_data_bit = 0
            for j in range(0, total_bits):
                if pow(2, last_parity) - 1 == j:
                    last_parity += 1
                else:
                    parity_row[0][last_data_bit] = parity_check_matrix[last_parity_row][j]
                    last_data_bit += 1
            code_generator_matrix[row] = parity_row[0]
            last_parity_row += 1
    return code_generator_matrix


def create_dynamic_decoding_matrix(data_bits):
    total_bits = get_full_message_length(data_bits)
    decoding_matrix = np.zeros((data_bits, total_bits), dtype=int)
    next_parity = 0
    next_row = 0
    for i in range(0, total_bits):
        if pow(2, next_parity) - 1 == i:
            next_parity += 1
        else:
            data_bit_mask = np.zeros((1, total_bits), dtype=int)
            data_bit_mask[0][i] = 1
            decoding_matrix[next_row] = data_bit_mask
            next_row += 1

    return decoding_matrix


def find_parity_message(message, G):
    parity_message = np.matmul(G, message)
    for i in range(len(G)):
        if parity_message[i] % 2 == 0:
            parity_message[i] = 0
        else:
            parity_message[i] = 1

    return parity_message


def fix_error_bit(error_bit, received_message):
    if received_message[error_bit - 1] == 1:
        received_message[error_bit - 1] = 0
    else:
        received_message[error_bit - 1] = 1
    return received_message


def error_bit_to_int(error_bit):
    error_bit_str = "".join(str(i) for i in error_bit)
    error_bit_int = int(error_bit_str, 2)
    return error_bit_int


def create_random_message(data_bits):
    message = np.zeros((1, data_bits), dtype=int)
    for i in range(0, data_bits - 1):
        message[0][i] = rnd.randint(0, 1)
    return message[0]


def reverse_bits(error_bit):
    for i in range(0, int(len(error_bit) / 2)):
        temp = error_bit[-1 - i]
        error_bit[-1 - i] = error_bit[i]
        error_bit[i] = temp
    return error_bit


def get_full_message_length(data_bits):
    return data_bits + calculate_parity_bits(data_bits)
