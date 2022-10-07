# Hamming Code Implementation for CENG 340
def check_for_error(parity_message, H):
    error_bit = [0] * int(len(H))

    for i in range(0, len(H)):
        for j in range(0, len(parity_message)):
            error_bit[i] += (parity_message[j] * H[i][j]) % 2
        if(error_bit[i] % 2 == 0) :
            error_bit[i] = 0
        else :
            error_bit[i] = 1
            
    error_bit = list(reversed(error_bit))
    return error_bit

def find_parity_message(message, G): 
    parity_message = [0] * int(len(G))

    for i in range(0, len(G)):
        for j in range(0, len(message)):
            parity_message[i] += (message[j] * G[i][j]) % 2
        if(parity_message[i] % 2 == 0) :
            parity_message[i] = 0
        else :
            parity_message[i] = 1
    
    return parity_message

def fix_error_bit(error_bit, recieved_message):
    if(recieved_message[error_bit - 1] == 1) :
        recieved_message[error_bit - 1] = 0
    else :
        recieved_message[error_bit - 1] = 1
    return recieved_message
def error_bit_to_int(error_bit):
    error_bit_str = "".join(str(i) for i in error_bit)
    error_bit_int = int(error_bit_str, 2)
    return error_bit_int

def main(): 
    message = [1, 0, 1, 1]

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

    correct_message = find_parity_message(message, G)
    check_for_error(correct_message, H)
    # Test Correct Parity
    recieved_message = correct_message
    
    error_bit_arr = check_for_error(recieved_message, H)
    error_bit = error_bit_to_int(error_bit_arr)
    if(error_bit != 0):
        recieved_message = fix_error_bit(error_bit, recieved_message)
    print("Message ",  message)
    print("Send Vector", correct_message)
    print("Recieved Message ", recieved_message)
    print("Parity Check ", error_bit_arr, "\n")
    
    # Test error in bit 5
    error_in_bit_5 = [0, 0, 0, 0, 1, 0, 0]
    # Allocate memory for array
    recieved_message = [0] * len(error_in_bit_5)
    # Add error to test
    for i in range(0, len(error_in_bit_5)):
        recieved_message[i] = error_in_bit_5[i] + correct_message[i]
    # Check the message for an error
    error_bit_arr = check_for_error(recieved_message, H)
    # Convert the bit index to an integer
    error_bit = error_bit_to_int(error_bit_arr)
    if(error_bit != 0):
        recieved_message = fix_error_bit(error_bit, recieved_message)
    # Output for D
    print("Message ",  message)
    print("Send Vector", correct_message)
    print("Recieved Message ", recieved_message)
    print("Parity Check ", error_bit_arr, "\n")
    
    # Test error in bit 3
    error_in_bit_3 = [0, 0, 1, 0, 0, 0, 0]
    for i in range(0, len(error_in_bit_3)):
        recieved_message[i] = error_in_bit_3[i] + correct_message[i]
    # Check the message for an error
    error_bit_arr = check_for_error(recieved_message, H)
    # Convert the bit index to an integer
    error_bit = error_bit_to_int(error_bit_arr)
    recieved_message = fix_error_bit(error_bit, recieved_message)
    # Output for D
    print("Message ",  message)
    print("Send Vector", correct_message)
    print("Recieved Message ", recieved_message)
    print("Parity Check ", error_bit_arr, "\n")
    
main()