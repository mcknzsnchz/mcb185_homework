import math

# function that return accuracy and F1 score

def accuracy(TP, FP, TN, FN): 
	a = (TP + FP + TN + FN)
	b = (TP + TN) 
	c = (FP + FN)
	pos_accuracy = print(b / a)
	neg_accuracy = print(c / a)
	return pos_accuracy, neg_accuracy
	
pos_accuracy, neg_accuracy = accuracy(24, 5, 63, 4)

pos_accuracy, neg_accuracy = accuracy(35, 2, 50, 7)

pos_accuracy, neg_accuracy = accuracy(45, 6, 20, 5)

def f1score(TP, FP, FN): 
	precision = (TP / (TP + FP))
	recall = (TP / (TP + FN))
	return print(2 * ((precision * recall) / (precision + recall)))
	
f1score(30, 3, 5)

f1score(50, 6, 3)

f1score (25, 5, 5)