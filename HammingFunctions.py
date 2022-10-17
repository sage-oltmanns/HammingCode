import numpy as np
import random as rnd


def calculate_parity_bits(data_bits):
    """
    Calculates the number of parity bits depending on the length of the data bits

    :param data_bits: The number of data bits the user specifies

    :return: The number of parity bits in the message
    """
    parity_bits = 0
    while pow(2, parity_bits) <= data_bits + parity_bits:
        parity_bits += 1
    return parity_bits


def check_for_error(parity_message, parity_check_matrix):
    """
    Checks the parity message against the parity check matrix to find a corrupt bit

    :param parity_message: The full message (parity bits and data bits)
    :param parity_check_matrix: Holds the positions of the data_bits we are interested in

    :return: An array that holds the position of the corrupt bit in binary
    """
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


def corrupt_a_bit(correct_message):
    """
    Corrupts a random bit in the correct message

    :params correct_message: The expected parity message which was transmitted

    :return: The expected parity message with a corrupt bit
    """
    # Find a bit to corrupt
    corrupt_bit = rnd.randint(0, len(correct_message) - 1)
    corrupt_message = correct_message.copy()

    # Flip the bit at the corrupt bit index
    if correct_message[corrupt_bit] == 0:
        corrupt_message[corrupt_bit] = 1
    else:
        corrupt_message[corrupt_bit] = 0
    return corrupt_message


def corrupt_bit_to_int(corrupt_bit):
    """
    Converts an array which holds the location of the corrupt bit into
    an index value

    :param corrupt_bit: An array which holds the location of the corrupt bit
    :returns: The index of the corrupt bit
    """
    error_bit_str = "".join(str(i) for i in corrupt_bit)
    error_bit_int = int(error_bit_str, 2)

    return error_bit_int - 1


def create_dynamic_decoding_matrix(data_bits):
    """
    Create the decoding matrix to decode send vector to the message that was sent

    :param data_bits: The number of data bits in the message
    :returns: The decoding matrix
    """
    # Number of columns
    total_bits = get_full_message_length(data_bits)
    decoding_matrix = np.zeros((data_bits, total_bits), dtype=int)

    # The exponent value to find the index of the parity bit
    next_parity = 0
    next_row = 0
    for i in range(0, total_bits):
        # If the index is going to be a parity bit
        if pow(2, next_parity) - 1 == i:
            # Increment the exponent and do nothing
            next_parity += 1
        else:
            # Insert a row of 0s with a 1 at position i
            decoding_matrix[next_row][i] = 1
            next_row += 1

    return decoding_matrix


def create_dynamic_generator_matrix(data_bits, parity_check_matrix):
    """
    Creates the generator matrix from the number of data bits and the parity check matrix

    :param data_bits: The number of data bits being sent
    :param parity_check_matrix: The parity check matrix

    :returns: The generator matrix
    """
    # Get the length of the parity message
    total_bits = get_full_message_length(data_bits)
    # Initialize code generator matrix
    code_generator_matrix = np.zeros((total_bits, data_bits), dtype=int)

    # Set up variables to track insertion index and exponent for determining parity row
    parity_row = 0
    data_bit_index = 0
    for row in range(0, total_bits):
        # If the row is not a parity bit location
        if pow(2, parity_row) - 1 != row:
            # Insert a 1 to mask the data bit at that location
            code_generator_matrix[row][data_bit_index] = 1
            # Increment data bit index so we can mask the next data bit
            data_bit_index += 1
        else:
            # Create variables to track insertion and lookup indexes
            parity_bit = 0
            last_data_bit = 0
            for j in range(0, total_bits):
                # If the index is a parity bit
                if pow(2, parity_bit) - 1 == j:
                    parity_bit += 1
                else:
                    # Insert the data bit into the generator matrix
                    code_generator_matrix[row][last_data_bit] = parity_check_matrix[parity_row][j]
                    # Increment the column to insert the next data bit
                    last_data_bit += 1
            parity_row += 1

    return code_generator_matrix


def create_dynamic_parity_check_matrix(data_bits):
    """
    Creates the parity check matrix based on the number of data bits

    :params data_bits: The number of data bits the user specifies
    :returns: The parity check matrix
    """
    # Number of rows in parity_check_matrix
    parity_bits = calculate_parity_bits(data_bits)
    # Number of columns in parity_check_matrix
    total_bits = get_full_message_length(data_bits)
    parity_check_matrix = [[0] * total_bits] * parity_bits

    for i in range(0, parity_bits):
        # Create array of 1s to insert into the array
        num_ones = pow(2, i)
        num_ones_arr = [1] * num_ones

        # Calculate the starting index for the 1s
        start_j = num_ones - 1
        while start_j < total_bits:
            # Calculate the end of the insertion
            last_j = start_j + num_ones

            # Insert the 1s array into the parity check matrix from the start index to the end
            parity_check_matrix[i] = parity_check_matrix[i][:start_j] + num_ones_arr + parity_check_matrix[i][last_j:]

            # Calculate next start location
            start_j = num_ones + last_j
        # Resize the array to remove excess 1s
        parity_check_matrix[i] = np.resize(parity_check_matrix[i], total_bits)

    return parity_check_matrix


def create_random_message(data_bits):
    """
    Creates a random message based on the number of data bits

    :param data_bits: The number of data bits in a message
    :returns: An array which holds the random message created
    """
    message = np.zeros((1, data_bits), dtype=int)
    for i in range(0, data_bits - 1):
        message[0][i] = rnd.randint(0, 1)
    return message[0]


def find_parity_message(message, generator_matrix):
    """
    Finds the full parity message based off of the message sent and the generator matrix

    :param message: The message which was sent
    :param generator_matrix: The matrix used to generate the parity bits
    :returns: The full parity message
    """
    # Do a matrix multiply to get the parity message
    parity_message = np.matmul(generator_matrix, message)

    for i in range(len(parity_message)):
        # If the bit is even set it to 0 otherwise set it to 1
        if parity_message[i] % 2 == 0:
            parity_message[i] = 0
        else:
            parity_message[i] = 1

    return parity_message


def fix_corrupt_bit(corrupt_bit, corrupt_message):
    """
    Flip the corrupt bit to the correct value in the received/corrupt message

    :param corrupt_bit: The position of the corrupt bit
    :param corrupt_message: The corrupt message
    :returns: The corrected message with no corrupt bits
    """
    # Flip the corrupt bit
    if corrupt_message[corrupt_bit] == 1:
        corrupt_message[corrupt_bit] = 0
    else:
        corrupt_message[corrupt_bit] = 1

    return corrupt_message


def get_full_message_length(data_bits):
    """
    Calculates the length of the full parity message

    :param data_bits: The number of data bits sent
    :returns: The length of the full parity message
    """
    return data_bits + calculate_parity_bits(data_bits)
