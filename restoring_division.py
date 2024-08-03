
# Restoring Division Algorithm

# add two binary numbers
def add(A, M):
	carry = 0
	Sum = ''

	for i in range (len(A)-1, -1, -1):

		temp = int(A[i]) + int(M[i]) + carry

		# If the binary number exceeds 1
		if (temp>1):
			Sum += str(temp % 2)
			carry = 1
		else:
			Sum += str(temp)
			carry = 0


	return Sum[::-1] 


# complement of the given binary number
def complement(m):
	M = ''

	# Iterating through the number
	for i in range (0, len(m)):

		# Computing the complement
		M += str((int(m[i]) + 1) % 2)

	# Adding 1 to the computed 
	
	M = add(M, '0001')
	return M
	

# Restoring Division Algorithm
def restoringDivision(Q, M, A):

	# Computing the length of the
	# number
	count = len(M)


	# Printing the initial values
	print ('Initial Values: A:', A, ' Q:', Q, ' M:', M)

	while (count):

		# Printing the values at every step
		print ("\nstep:", len(M)-count + 1, end = '')
		
		# Step1: Left Shift, assigning LSB of Q to MSB of A.
		print (' Left Shift and Subtract: ', end = '')
		A = A[1:] + Q[0]
		

		comp_M = complement(M)

		A = add(A, comp_M)
		print(' A:', A)
		print('A:', A, ' Q:', Q[1:]+'_', end ='')
		
		if (A[0] == '1'):

			Q = Q[1:] + '0'
			print (' -Unsuccessful')

			# Restoration of A is required
			A = add(A, M)
			print ('A:', A, ' Q:', Q, ' -Restoration')
			
		else:

			Q = Q[1:] + '1'
			print (' Successful')

			# No Restoration of A.
			print ('A:', A, ' Q:',
				Q, ' -No Restoration')
		count -= 1
 
	print ('\nQuotient(Q):', Q,	' Remainder(A):', A)



dividend = input("Enter dividend : " )
divisor = input("Enter divisor : " )



accumulator = '0' * len(dividend)
restoringDivision(dividend,	divisor, accumulator)
