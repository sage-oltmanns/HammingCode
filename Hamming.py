# Hamming Code Implementation for CENG 340
from HammingFunctions import *


def main():
    # User Input
    data_bits = int(input("Enter number of databits: "))

    while data_bits <= 0:
        data_bits = int(input("Please enter a number greater than 0: "))
    # Total bits (helper value)
    total_bits = get_full_message_length(data_bits)
    # Create Message
    message = create_random_message(data_bits)

    # Create Check Matrices
    parity_check_matrix = create_dynamic_parity_check_matrix(data_bits)
    code_generator_matrix = create_dynamic_generator_matrix(data_bits, parity_check_matrix)
    decoding_matrix = create_dynamic_decoding_matrix(data_bits)

    # Find the Correct Message
    correct_message = find_parity_message(message, code_generator_matrix)

    # Corrupt a random bit in the message
    corrupt_message = corrupt_a_bit(correct_message)

    # Find the error bit
    corrupt_bit = check_for_error(corrupt_message, parity_check_matrix)
    corrupt_bit_index = corrupt_bit_to_int(corrupt_bit)

    # Create Arrays to hold checked corrected/decoded messages
    corrected_message = np.zeros((1, total_bits), dtype=int)
    decoded_message = np.zeros((1, data_bits), dtype=int)

    # If an error bit was found
    if corrupt_bit_index != -1:
        # Fix the bit
        corrected_message = fix_corrupt_bit(corrupt_bit_index, corrupt_message.copy())
        # Correct the message
        decoded_message = np.zeros((1, data_bits), dtype=int)
        for i in range(0, data_bits):
            for j in range(0, total_bits):
                decoded_message[0][i] += int(corrected_message[j] * decoding_matrix[i][j])

    # Output important arrays
    print("Message          :  {}".format(message))
    print("Send Vector      :  {}".format(correct_message))
    print("Received Message :  {} ".format(corrupt_message))
    print("Parity Check     :  {}".format(corrupt_bit))
    print("Corrected Message:  {}".format(corrected_message))
    print("Decoded Message  :  {}".format(decoded_message[0]))


main()
