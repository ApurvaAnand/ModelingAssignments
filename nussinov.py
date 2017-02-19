import sys,string
from numpy import *
from matplotlib import *

#reading the given sequence
seq=["ACCAGAACUGGU"]  


#using a score of 1 for base pairing and 0 for no base pairing. A pairs with U and G pairs with C
def score(nucleotide1,complementary):
	delta=0;
	if nucleotide1=='A' and complementary=='U':
		return 1;
	elif nucleotide1=='U' and complementary=='A':
		return 1;
	elif nucleotide1=='G' and complementary=='C':
		return 1;
	elif nucleotide1=='C' and complementary=='G':
		return 1;
	else:
		return 0;

#finding the alignment
def alignment(seq):
#making a matrix of dimension as length of the sequence
 Length=len(seq);
 matrix=zeros((Length,Length));
 for n in xrange(1,Length):
	 for j in xrange(n,Length):
		 i=j-n;
#finding the optimal condition through dynamic programming where OPT(i,j)=max(matrix[i+1][j-1]+score, matrix[i+1,j],matrix[i,j-1]
		 OPT1=matrix[i+1,j-1]+score(seq[i],seq[j]);
		 OPT2=matrix[i+1,j];
		 OPT3=matrix[i,j-1];
         #skipping if j-i<4 since no crossing is allowed
		 if i+3<=j:            
			tmp=[];
			for k in xrange(i+1,j):
				tmp.append(matrix[i,k]+matrix[k+1,j]);
			OPT4=max(tmp);
			matrix[i,j]=max(OPT1,OPT2,OPT3,OPT4);
		 else:
			matrix[i,j]=max(OPT1,OPT2,OPT3);
 print " the nussinov matrix is: ", matrix;
 return matrix;

#tracing back the matrix
def traceback(matrix,seq,i,j,pair):
	if i<j:
		if matrix[i,j]==matrix[i+1,j]:
			traceback(matrix,seq,i+1,j,pair);
		elif matrix[i,j]==matrix[i,j-1]:
			traceback(matrix,seq,i,j-1,pair);
		elif matrix[i,j]==matrix[i+1,j-1]+score(seq[i],seq[j]):
			pair.append([i,j,str(seq[i]),str(seq[j])]);
			traceback(matrix,seq,i+1,j-1,pair);
	else:
	  for k in xrange(i+1,j):
		  if matrix[i,j]==matrix[i,k]+matrix[k+1,j]:
			  traceback(matrix,seq,i,k,pair);
			  traceback(matrix,seq,k+1,j,pair);
			  break;
	return pair;

for q in xrange(0,len(seq)):

	pair=traceback(alignment(seq[q]),seq[q],0,len(seq[q])-1,[])
	print "The residues binding as per the traceback"
	for x in xrange(0,len(pair)):
		print "("'%s%d == %s%d'")" % (pair[x][2],pair[x][0],pair[x][3],pair[x][1]);
	

























