def check_for_error(parity_message, H):
    error_bit = [0] * int(len(H))

    for i in range(0, len(H)):
        for j in range(0, len(parity_message)):
            error_bit[i] += (parity_message[j] * H[i][j]) % 2
        if(error_bit[i] % 2 == 0) :
            error_bit[i] = 0
        else :
            error_bit[i] = 1
    error_bit = reverse_bits(error_bit)
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

def reverse_bits(error_bit):
    for i in range(0, int(len(error_bit)/2)):
        temp = error_bit[-1 - i]
        error_bit[-1 - i] = error_bit[i]
        error_bit[i] = temp
    return error_bit