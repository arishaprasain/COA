import gates

def reverse(num):
    return num[-1::-1]

def twos_complement(b1):
    l = len(b1)
    ones = []
    
    # Calculate one's complement
    for i in range(l):
        ones.append( gates.not_(b1[i]))
    print("One's complement: ", ''.join(ones))
    
    # Adding 1 to the one's complement to get two's complement
    carry = "1"
    for i in range(l):
        sum_ = gates.xor_(ones[i], carry)
        carry = gates.and_(ones[i], carry)
        ones[i] = sum_
    
    twos = ''.join(ones)
    print("Two's complement: ", twos)
    return twos

def subtraction(b1, b2):
    l1, l2 = len(b1), len(b2)
    largest = max(l1, l2)
    
    # Zero-fill to make both binary numbers the same length
    b1 = b1.zfill(largest)
    b2 = b2.zfill(largest)
    
    # Reverse both numbers for easier processing from the least significant bit
    rev1 = reverse(b1)
    rev2 = reverse(b2)
    
    # Get the two's complement of the second number
    rev2 = twos_complement(rev2)
    rev2 = rev2.ljust(largest, "0")
    print("Reversed and two's complement of b2: ", rev2)
    print("Reversed b1: ", rev1)

    # Adding the first number and the two's complement of the second number
    ans = []
    carry = "0"
    for i in range(largest):
        s = gates.xor_(gates.xor_(rev1[i], rev2[i]), carry)
        carry = gates.or_(gates.and_(rev1[i], rev2[i]), gates.and_(gates.xor_(rev1[i], rev2[i]), carry))
        ans.append(s)
        print(f"Sum: {s}, Carry: {carry}")
    
    # Reverse the answer to get the correct order
    answer = reverse(''.join(ans))
    print("Result: ", answer)


subtraction("1101", "10")
