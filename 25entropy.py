import math 

# function that returns the Shannon entropy for nucleotide counts a, c, g, t.

def shannon_entropy(a, c, g, t): 
	total = a + c + g + t
	pa = a / total
	pc = c / total
	pg = g / total
	pt = t / total
	entropy = 0 
	if pa != 0: entropy = entropy + pa * math.log2(pa)
	if pc != 0: entropy = entropy + pc * math.log2(pc)
	if pg != 0: entropy = entropy + pg * math.log2(pg)
	if pt != 0: entropy = entropy + pt * math.log2(pt)
	return -entropy
	
print(shannon_entropy(5, 0, 5, 5))




