import sys
import numpy as np
#import pandas as pd

def getSubSets(set0):
	if len(set0)==0:
		#print 'NULL SET'
		return set0
	if len(set0)==1:
		newList=[[],set0]
		return newList
	subset=getSubSets(set0[1:len(set0)])
	#print set0[1:len(set0)], subset
	start=set0[0]
	newList=[]
	newList.extend(subset)
	for set1 in subset:
		set1 = [start]+set1
		newList.append(set1)
	return newList

if __name__=="__main__":
	dataMat=np.loadtxt(sys.argv[1],delimiter='\t')
	dataCp=dataMat
	dataCp[dataCp>0.9] = 1
	dataCp[dataCp<-0.9] = -1
	dataCp[np.logical_and(dataCp>=-0.9, dataCp<=0.9)]=0
	#print dataCp[0:5]
	dataCp[dataCp==-1]=0
	print dataCp[0:10]
	(rowNum,colNum)=dataCp.shape
	print rowNum, colNum
	rowCount=0
	biclusterDict={}
	activeMap = {}
	for row in dataCp:
		colCount=0
		activeEdges=[]
		for col in row:
			if col==1:
				activeEdges.append(colCount)
			colCount+=1
		activeSet = getSubSets(activeEdges)
		if rowCount<10:
			print 'FOR DEBUGGING PURPOSES'
			print 'activeEdges',activeEdges
			print '==============='
			print activeSet
			print '==============='
		for set0 in activeSet:
			if len(set0)==0:
				continue
			counter=0
			for i in set0:
				counter+=(2**i)
			if rowCount<10:
				print 'counter',counter
			if counter in activeMap and len(set0)!=len(activeMap[counter]):
				print "HUGE PROBLEM"
				print activeMap[counter], set0
			activeMap[counter]=set0
			if counter in biclusterDict:
				biclusterDict.get(counter).append(rowCount)
			else:
				biclusterDict[counter]=[rowCount]
		rowCount+=1
	maxEdges=0
	maxCounter=-1
	for counter in biclusterDict:
		sizeR=len(biclusterDict[counter])
		sizeL=len(activeMap[counter])
		if sizeL*sizeR>maxEdges:
			maxEdges=sizeR*sizeL
			maxCounter=counter
	print "=====RESULTS======"
	print biclusterDict[maxCounter], activeMap[maxCounter]
	print 'maxEdges',maxEdges
	print dataCp[biclusterDict[maxCounter],:]
