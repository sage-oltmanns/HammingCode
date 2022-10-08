# Hamming Code Implementation for CENG 340
from math import sqrt
from HammingFunctions import *
from test import *
import random as rnd

def create_dynamic_H(num_bits) :
    parity_bits = int(sqrt(num_bits + 1))
    H = [[0] * (num_bits + parity_bits) for i in range(parity_bits)]
    for i in range(0, parity_bits) :
        num_ones = pow(2, i)
        skip = 0
        print(num_ones)
        for j in range(0, len(H[i])):
            if(j == num_ones - 1):
                H[i][j] = 1
                for k in range(0, num_ones):
                    H[i][j + k] = 1
            if(skip <= num_ones) :
                skip += 1
            elif(skip == num_ones):
                for k in range(0, num_ones):
                    H[i][j + k] = 1   
        print(H[i])
def main(): 
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
    
    # User Input
    num_bits = int(input("Enter number of databits: "))

    message = [0] * num_bits
    for i in range(0, num_bits - 1):
        message[i] = rnd.randint(0, 1)
    create_dynamic_H(num_bits)

    correct_message = find_parity_message(message, G)
    check_for_error(correct_message, H)
    # Test Random Corrupt Bit
    corrupt_bit = rnd.randint(0, len(correct_message))
    recieved_message = correct_message.copy()
    if(correct_message[corrupt_bit] == 0):
        recieved_message[corrupt_bit] = 1
    else :
        recieved_message[corrupt_bit] = 0
    error_bit_arr = check_for_error(recieved_message, H)
    error_bit = error_bit_to_int(error_bit_arr)
    if(error_bit != 0):
        corrected_message = fix_error_bit(error_bit, recieved_message.copy())
    
    decoded_message = [0] * int(len(message))
    for i in range(0, len(message)):
        for j in range(0, len(R[0])):
            decoded_message[i] += int(corrected_message[j] * R[i][j])
    print("Message          :  {}".format(message))
    print("Send Vector      :  {}".format(correct_message))
    print("Recieved Message :  {} ".format(recieved_message))
    print("Parity Check     :  {}".format(error_bit_arr))
    print("Corrected Message:  {}".format(corrected_message))
    print("Decoded Message  :  {}".format(decoded_message))
    
    
main()
unittest.main()