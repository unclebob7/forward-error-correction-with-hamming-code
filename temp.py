"""pre-test probability design"""

# bit-oriented algorithm
n ::= bit_expected_probability
for i in range(0, (280000*18)):
	bit_probability := np.randint(0, n)
	if(probability==0):
		bit[i] := bit[i]^1
		
# package-oriented algorithm
n ::= pack_expected_probability
m ::= bit_expected_probability 
for i in range(0, 280000):
	pack_probability :=np.randint(0, n)
	if(pack_probability==0):
		for j in pack[i]:
			bit_probability := np.randint(0, m)
			if(bit_probability==0)
				bit[j] := bit[j]^1
			
"""post-test probability design"""

n ::= pack_expected_probability (n<=280000)
m ::= bit_expected_probability
for i in np.random.permutatoin(0, n):	# narray storing random-num with len(n)
	for j in pack[i]:
		bit_probability := np.randint(0, m)
		if(bit_probability==0):
			bit[j] := bit[i]^1
	
