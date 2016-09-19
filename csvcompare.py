#!/usr/bin/python -tt


"""Compares two csv files with identical headers to find:
- Additions, new rows
- Deletions, removed rows
- Changes, altered rows
Returns a summary of the differences.
"""

import sys
import csv

# Defines a "repeat" function that takes 2 arguments.
def compareCells(cell1, cell2):
    """
    Compares two cells returns true if same
    """
    result = 0

    return result


# Define a main() function
def main():

##f = open(sys.argv[1])
##for line in f:   ## iterates over the lines of the file
    ##print line,    ## trailing , so print does not add an end-of-line char
                   ## since 'line' already includes the end-of line.
 ## f.close()
  
  ##dictreader = csv.DictReader(open(sys.argv[1]))
  ##for row in dictreader:
    ##print(row['Header1'], row['Header2'])
  
	allrowsM = []  
	master = csv.reader (open(sys.argv[1]))
	for row in master:
		##print row
		allrowsM.append(row)
    
	##print allrowsM
	##print len(allrowsM)
  
	allrowsN = []  
	newf = csv.reader (open(sys.argv[2]))
	for row in newf:
		##print row
		allrowsN.append(row)
    
	##print allrowsN
	##print len(allrowsN)
	##print len(allrowsN[0])

	i=1
	mi=1
	j=0
	
	newEmps = []
	newEmps.append(allrowsN[0]) ## add header row to new emps list
	
	thisEmpChanges = []
	
	AllEmpChanges = []
	AllEmpChanges.append(allrowsN[0])
	
	
  
	while i < len(allrowsN):
		##print 'i: ' + str(i)
		if mi >= len(allrowsM):
			print 'NEW >> ' + str(allrowsN[i])
			newEmps.append(allrowsN[i])
			i += 1
			mi += 1
		else:
			if allrowsN[i]==allrowsM[mi]: ## complete row identical
				##print 'i: ' + str(i)
				i+=1
				mi += 1
			else:  
				j=0
				thisEmpChanges=[]
				if allrowsN[i][0]==allrowsM[mi][0]:	 ## unique id same, compare other cols	
					while j < len(allrowsN[0]):
						##print 'j: '+ str(j)
						if allrowsN[i][j]==allrowsM[mi][j]:
							if j<1:
								thisEmpChanges.append(allrowsN[i][j])
							else:
								thisEmpChanges.append('')
							j+=1
						else:
							print 'CHANGE >> ' + allrowsM[mi][0] + ' ' +  allrowsM[mi][1] +':'
							print allrowsN[0][j] + ':  ' +  allrowsM[mi][j] +' --> ' +allrowsN[i][j]
							thisEmpChanges.append(allrowsN[i][j])
							j+=1
					AllEmpChanges.append(thisEmpChanges)
					mi +=1
					
				else: ## unique id is different, might be a rehire, print as new and advance i but not mi
					print 'NEW >> ' + str(allrowsN[i])
					newEmps.append(allrowsN[i])		
				i+=1
    
	print 'ALL NEW LINES:'
	for row in newEmps:
		print row
		
	print 'ALL EMP CHANGES:'
	for row in AllEmpChanges:
		print row
  
    
  ##f.close()


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()

