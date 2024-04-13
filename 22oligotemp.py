import math

# returns the oligo matching temperature 
# given the number of As, Cs, Gs, and Ts, in the oligo

def oligo_tmelt(A, T, G, C):
	a = oligo = (A + T + G + C)
	b = nt = 13
	tm1 = (((A + T) * 2) + ((G + C) * 4))
	tm2 = (64.9 + 41 * (G + C - 16.4) / (A + T + G + C))
	if a < b:  		return print(tm1)
	if a == b: 		return print(tm1)
	if a > b: 		return print(tm2)
oligo_tmelt(4, 4, 4, 4)

oligo_tmelt(1, 4, 5, 3)

oligo_tmelt(2, 3, 4, 2)

oligo_tmelt(5, 9, 6, 3)