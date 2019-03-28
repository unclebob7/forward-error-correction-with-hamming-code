#function to check no of parity bits in genration of hamming code
#return no of parity bits required to append in given size of data word
def noOfParityBits(noOfBits):
	i=0
	while 2.**i <= noOfBits+i: # (power of 2 + parity bits laready  counted) that is for 4 bit of dataword requires 3 bit of parity bits
		i+=1
	return i

#function to genrate no of parity bits while length of entire code is clarified,
def noOfParityBitsInCode(noOfBits):
	i=0
	while 2.**i <= noOfBits:
		i+=1
	return i
"""
parameter:data
returns a list with parity bits position is 0 that is position which are power of 2 are 0
"""
def appendParityBits(data):
	n=noOfParityBits(len(data)) #no of parity bits required for given length of data
	i=0 #loop counter
	j=0 #no of parity bits
	k=0 #no of data bits
	list1=list()
	while i <n+len(data):
		if i== (2.**j -1):
			list1.insert(i,0)
			j+=1
		else:
			list1.insert(i,data[k])
			k+=1
		i+=1
	return list1
#returns a list of hamming codes even parity
#the concept here i used is : i will create one sublist of appropriate bits to be considered for corresponding parity bits that is
#if data is p1 p2 d1 p4 d2 d3 d4 where p is parity bits and d is data bits 
#so for p1 sublist will be p1 d1 d2 d4
#for p2 sublist will be p2d1 d3d4
#for p4 sublist will be p4d2d3d4
#so to genralise formula is   list[(j*k)-1:((j+1)*k)-1] where j is intialised to 1 and after each iteration will be incremented by 2 
#as we need alternate pairs of data that is for p1 pattern is like take 1 bit skip 1 take 1 skip 1 so taking alternate bits of size  k 
#that is k is the weight of parity bits we are considering when for p1 k=2^0=1 for p2 k=2^1=2 for p4 k=2^2=4 so on and i for no of parity bits to be iterated.
#Will increment j upto length of list
def hammingCodes(data):
	n=noOfParityBits(len(data))
	list1=appendParityBits(data) # list with parity bits at appropriate position
	i=0 #loop counter
	k=1 #2 to the power kth parity bit
	while i<n:
		k=2.**i
		j=1
		total=0
		while j*k -1 <len(list1):
			if j*k -1 == len(list1)-1: #if lower index is last one to be considered in sub list then
				lower_index=j*k -1
				temp=list1[int(lower_index):len(list1)]
			elif (j+1)*k -1>=len(list1):
				lower_index=j*k -1
				temp=list1[int(lower_index):len(list1)] #if list's size is smaller than boundary point
			elif (j+1)*k -1<len(list1)-1:
				lower_index=(j*k)-1
				upper_index=(j+1)*k -1
				temp=list1[int(lower_index):int(upper_index)]
			
			total=total+sum(int(e) for e in temp) #do the sum of sub list for corresponding parity bits
			print (total,j)
			j+=2 #increment by 2 beacause we want alternative pairs of numberss from list
		if total%2 >0:
			list1[int(k)-1]=1 # to check even parity summing up all the elements in sublist and if summ is even than even parity else odd parity
			print ("Element is ",list1[int(k)-1],k)
		i+=1
	return list1
#Prodecure is same as above function the minor change is we need to identify if error exists then on which bit
#To do so we will identify that which parity bits are odd parities(incorrect) we will add all parities bit position(weight) to get position of corrupted bit
#E.g.: if p1 and p4 are odd parity but p2 is even(correct) so errorthbit=1+4=5 that is 5th bit(4th index of list) is wrong toggle it and display the data
def hammingCorrection(data):
	n=noOfParityBitsInCode(len(data))
	i=0
	list1=list(data)
	print (list1)
	errorthBit=0
	while i<n:
		k=2.**i
		j=1
		total=0
		while j*k -1 <len(list1):
			if j*k -1 == len(list1)-1:
				lower_index=j*k -1
				temp=list1[int(lower_index):len(list1)]
			elif (j+1)*k -1>=len(list1):
				lower_index=j*k -1
				temp=list1[int(lower_index):len(list1)] #if list's size is smaller than boundary point
			elif (j+1)*k -1<len(list1)-1:
				lower_index=(j*k)-1
				upper_index=(j+1)*k -1
				temp=list1[int(lower_index):int(upper_index)]
			
			total=total+sum(int(e) for e in temp)
			print (total,j)
			j+=2 #increment by 2 beacause we want alternative pairs of numberss from list
		if total%2 >0:
			errorthBit+=k # to check even parity summing up all the elements in sublist and if summ is even than even parity else odd parity
		i+=1
	if errorthBit>=1:
		print ("error in ",errorthBit," bit after correction data is " )
		#toggle the corrupted bit
		if list1[int(errorthBit-1)]=='0' or list1[int(errorthBit-1)]==0:
			list1[int(errorthBit-1)]=1
		else:
			list1[int(errorthBit-1)]=0
	else:
		print ("No error")
	list2=list()
	i=0
	j=0
	k=0
	#returning only data from codeword that is ignoring parity bits
	while i<len(list1): #returning only data bits
		if i!= ((2**k)-1):
			temp=list1[int(i)]
			list2.append(temp)
			j+=1
		else:
			k+=1
		i+=1
	return list2

# def hammingDecode(data):
# 	# hc_item = '01101010101010101010'
# 	list_data = list(data)
# 	parity_num=noOfParityBits(len(data))
# 	loop_counter=0 #loop counter
# 	# parity_positon=1 #2 to the power kth parity bit
# 	while loop_counter<(parity_num-1):
# 		parity_positon=2**loop_counter-1
# 		list_data[parity_positon] = 'a'
# 		loop_counter = loop_counter+1
# 	while 'a' in list_data:
# 		list_data.remove('a')
# 	decoded_data = ''.join(list_data)
# 	print(decoded_data)
