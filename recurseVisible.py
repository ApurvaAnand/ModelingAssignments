
visible = 0

def solution(T):
	#visible = 0
	recurseTree(T,0)
	return visible

def recurseTree(T, maxVal):
	if T=None or T.X == None or (T.L==None and T.R==None):
		return
	if T.X >= maxVal:
		visible+=1
		maxVal = T.X
	recurseTee(T.L, maxVal)
	recurseTee(T.R, maxVal)
	return
