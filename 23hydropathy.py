# function that returns KD hydrophobicity value for an amino acid letter

I = Ile = 4.50
V = Val = 4.20
L = Leu = 3.80
F = Phe = 2.80
C = Cys = 2.50
M =  Met = 1.90
A = Ala = 1.80
G = Gly = -0.40
T = Thr = -0.70
S = Ser = -0.80
W = Trp = -0.90
Y = Tyr = -1.30
P = Pro = -1.60
H = His = -3.20
E = Glu = -3.50
Q = Gln = -3.50
D = Asp = -3.50
N = Asn = -3.50
K = Lys = -3.90
R = Arg = -4.50

def kd_val(x):
	if x == ("AUU"): 	return print(I)
	if x == ("AUC"):  	return print(I)
	if x == ("AUA"):		return print(I)
	if x == ("GUU"): 	return print(V)
	if x == ("GUC"):		return print(V)
	if x == ("GUA"):		return print(V)
	if x == ("GUG"): 	return print(V)
	if x == ("CUU"):		return print(L)
	if x == ("CUC"): 	return print(L)
	if x == ("CUA"): 	return print(L)
	if x == ("CUG"):		return print(L)
	if x == ("UUG"): 	return print(L) 
	if x == ("UUA"): 	return print(L)
	if x == ("UUU"):		return print(F)
	if x == ("UUC"): 	return print(F)
	if x == ("UGU"): 	return print(C)
	if x == ("UGC"): 	return print(C)
	if x == ("AUG"): 	return print(M)
	if x == ("GCG"): 	return print(A)
	if x == ("GCA"): 	return print(A)
	if x == ("GCC"): 	return print(A) 
	if x == ("GCU"):		return print(A)
	if x == ("GGG"): 	return print(G)
	if x == ("GGA"): 	return print(G)
	if x == ("GGC"): 	return print(G)
	if x == ("GGU"):		return print(G)
	if x == ("ACG"): 	return print(T)
	if x == ("ACA"): 		return print(T)
	if x == ("ACC"): 	return print(T)
	if x == ("ACU"):		return print(T)
	if x == ("AGC"): 	return print(S) 
	if x == ("AGU"): 	return print(S)
	if x == ("UGG"): 	return print(W)
	if x == ("UAU"): 	return print(Y)
	if x == ("UAC"):		return print(Y)
	if x == ("CCU"): 	return print(P)
	if x == ("CCC"): 	return print(P)
	if x == ("CCA"): 	return print(P)
	if x == ("CCG"): 	return print(P)
	if x == ("CAU"): 	return print(H) 
	if x == ("CAC"): 	return print(H)
	if x == ("GAG"): 	return print(E) 
	if x == ("GAA"):		return print(E)
	if x == ("CAA"): 		return print(Q) 
	if x == ("CAG"): 	return print(Q)
	if x == ("GAC"): 	return print(D)
	if x == ("GAU"): 	return print(D)
	if x == ("AAU"): 		return print(N)
	if x == ("AAC"): 		return print(N)
	if x == ("AAA"): 		return print(K) 
	if x == ("AAG"): 	return print(K)
	if x == ("AGG"): 	return print(R) 
	if x == ("AGA"): 	return print(R)
	if x == ("UAA"): 		return print('stop codon')
	if x == ("UAG"): 	return print('stop codon')
	if x == ("UGA"):		return print('stop codon')
	else: 			return print('not an amino acid')

kd_val("AUU")
kd_val("AUC")
kd_val("ATG")
kd_val("GUC")
kd_val("CAU")
kd_val("UAG")
kd_val("CCC")
kd_val("AAG")
kd_val("AGA")
kd_val("GAG")
kd_val("CAG")
kd_val("TAC")
kd_val("CCU")
kd_val("ACA")
kd_val("GCA")
kd_val("GGU")
kd_val("AUG")
kd_val("UUU")
kd_val("CUC")
kd_val("UGU")
kd_val("AGU")
kd_val("UGG")
kd_val("UAU")
kd_val("AAG")
kd_val("AGG")

# surely there must have been an easier way of doing this









