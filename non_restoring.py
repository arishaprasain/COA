
# Function to add two binary numbers
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


def compliment(m):
	M = ''

	# Iterating through the number
	for i in range (0, len(m)):

		# Computing the compliment
		M += str((int(m[i]) + 1) % 2)


	M = add(M, '0001')
	return M
	

def nonRestoringDivision(Q, M, A):
	

	count = len(M)


	comp_M = compliment(M)
	flag = 'successful'


	print ('Initial Values: A:', A, 
		' Q:', Q, ' M:', M)

	while (count):

		# Printing the values at every step
		print ("\nstep:", len(M)-count + 1, 
			end = '')
		
		# Step1: Left Shift, assigning LSB of Q to MSB of A.
		print (' Left Shift and ', end = '')
		A = A[1:] + Q[0]

		# Choosing the addition or subtraction based on the result of the previous step
		if (flag == 'successful'):
			A = add(A, comp_M)
			print ('subtract: ')
		else:
			A = add(A, M)
			print ('Addition: ')
			
		print('A:', A, ' Q:', 
			Q[1:]+'_', end ='')
		
		if (A[0] == '1'):


			# Step is unsuccessful and the quotient bit will be '0'
			Q = Q[1:] + '0'
			print (' -Unsuccessful')

			flag = 'unsuccessful'
			print ('A:', A, ' Q:', Q, 
				' -Addition in next Step')
			
		else:

			# Step is successful and the quotient bit will be '1'
			Q = Q[1:] + '1'
			print (' Successful')

			flag = 'successful'
			print ('A:', A, ' Q:', Q, 
				' -Next Subtraction')
		count -= 1
	print ('\nQuotient(Q):', Q, 
		' Remainder(A):', A)

dividend = input("Enter dividend : " )
divisor = input("Enter divisor : " )



accumulator = '0' * len(dividend)
nonRestoringDivision(dividend,	divisor, accumulator)
