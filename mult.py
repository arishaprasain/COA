def reverse(num):
    return num[-1::-1]

def mul(b1, b2):
    if b1 == "0" or b2 == "0":
        return "0"
    else:
        return "1"
    
def multiply(b1 = "100", b2 = "101"):
    l1, l2 = len(b1), len(b2)
    largest = max(l1, l2)
    
    #number padding
    b1  = b1.zfill(largest)
    b2  = b2.zfill(largest)
    
    # reverse both numbers
    b1  = reverse(b1)
    b2  = reverse(b2)
    
    b2 = list(b2)
    
    for i in range(l):
        if b2[0] == 1:
            partial_sum.append(b1)
            
        
    
    
    
    
    partial_sum = []
    for i in b2