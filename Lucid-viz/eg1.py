import os
import sys
import pandas as pd
import statistics
lst=[]
def readCSV () :
	output = pd.read_csv("in.csv")
	print(output)
	print("--------------------------------------------")

	for i in output["Volume"] :
         # append number in list
	    lst.append(i)
	 # final list
	 # sum of all numbers in list /total numbers    
	mean=sum(lst)/i
	print("MEAN IS :")
	print(mean)
	lst.sort()
	#check the numbers of element
	#if even the sum two number from middle  and divide by 2
	i=len(lst)
	median=0
	if i%2==0 :
		#since index start from 0 actual index is less than 1
		median=(lst[int(i/2)-1]+lst[int(i/2)])/2

	else :
	    median=lst[i-1]
	print("................................................")
	print("MEDIAN IS :")
	print(median)

    # find mode with using statistics library with mode function
	print(".................................................")
	print("Mode of list is  : % s" % (statistics.mode(lst)))
    
    # find standard deviation with using statistics library in python with stdev function
	print("................................................")
	print("Standard Deviation of list is  : % s" % (statistics.stdev(lst)))


   
    


readCSV()