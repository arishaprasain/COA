

def binary_multiplication(A, B):
    # Convert binary strings to integers
    A = int(A, 2)
    B = int(B, 2)

    # partial product 
    P = 0
    
    multiplicand = A

    
    while B > 0:
        # If the least significant bit of B is 1, add the multiplicand to P
        if B & 1:
            P += multiplicand
        
        
        multiplicand <<= 1
        
        
        B >>= 1

    # Convert the result to binary string
    result = bin(P)[2:]
    return result.zfill(8)  


A = "00001001"
B = "00001101"


product = binary_multiplication(A, B)
print("Product:", product) 
