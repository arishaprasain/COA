import gates

def reverse(num):
    return num[-1::-1]


def addition(b1 = "1011", b2 = "101", carry = "0"):
    
    l1, l2 = len(b1), len(b2)
    l = largest = max(l1,l2)
    b1 = b1.zfill(largest)
    b2 = b2.zfill(largest)
    
    rev1 = reverse(b1)
    rev2 = reverse(b2) 

    i = 0
    ans = []
    while (largest ):  #sum for all bits  
        s = gates.xor_(gates.xor_(rev1[i], rev2[i]), carry)
        carry =  gates.or_(gates.and_(rev1[i], rev2[i]), gates.and_(gates.xor_(rev1[i], rev2[i]), carry))
        ans.append(s)
        if len(ans) == l:
            ans.append(carry)
        print(f"Sum : {s} , Carry : {carry}")
        i += 1
        largest -= 1
    answer = reverse(''.join(ans))
    # print(answer)
    return answer
        


# operand1 = input("Enter 1st binary number : ")
# operand2 = input("Enter 2nd binary number : ")
# result = addition(operand1, operand2)
# print(f"The sum is : {result}")




