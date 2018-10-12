import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
	inFile = open(file, 'r')
	line = inFile.readline()
	dictList = []

	keys = line.split(',')
	ft = keys[0]
	lt = keys[1]
	em = keys[2]
	cl = keys[3]
	b = keys[4]

	line = inFile.readline()

	while line: 
		fileDict = {}
		vals = line.split(',')
		first = vals[0]
		last = vals[1]
		email = vals[2]
		clas = vals[3]
		dob = vals[4]

		fileDict[ft] = first
		fileDict[lt] = last
		fileDict[em] = email
		fileDict[cl] = clas
		fileDict[b] = dob

		dictList.append(fileDict)
		line = inFile.readline()

	inFile.close()
	return dictList



# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows

	pass

def mySort(data,col):
	sortedList = sorted(data, key=lambda x: x[col])
	item1 = sortedList[0]
	first_item1 = item1['First'] 
	last_item1 = item1['Last']
	return first_item1 + ' ' + last_item1 
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	pass


def classSizes(data):
	tupList = []
	sr = 0
	jr = 0
	soph = 0
	fr = 0
	
	for d in data:
		if d['Class'] == 'Senior':
			sr += 1
		elif d['Class'] == 'Junior':
			jr += 1
		elif d['Class'] == 'Sophomore':
			soph += 1
		elif d['Class'] == 'Freshman':
			fr += 1

	tupList.append(('Senior', sr))
	tupList.append(('Junior', jr))
	tupList.append(('Sophomore', soph))
	tupList.append(('Freshman', fr))

	tupsSorted = sorted(tupList, key=lambda x: x[1], reverse=True) 
	return tupsSorted
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	pass


def findMonth(a):
	monthList = []
	for d in a:
		date = d['DOB\n'] 
		dobList = date.split('/') 
		m = dobList[0]
		monthList.append(m) 

	monthDict = {}
	for num in monthList:
		if num in monthDict:
			monthDict[num] += 1
		else:
			monthDict[num] = 1

	monthSorted = sorted(monthDict, key=lambda x: monthDict[x], reverse=True) 
	commonMonth = monthSorted[0] 
	return int(commonMonth)  
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

	pass

def mySortPrint(a,col,fileName):
	outfile = open(fileName, 'w')
	sortedList = sorted(a, key=lambda x: x[col])
	for di in sortedList:
		first_item = di['First'] 
		last_item = di['Last']
		email_item = di['Email'] 

		outfile.write(first_item + ", " + last_item + ", " + email_item)

	outfile.close()

#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	pass

def findAge(a):
	totalPpl = 0
	totalAge = 0
	for d in a:
		date = d['DOB\n'] 
		dobList = date.split('/') 
		yr = dobList[2]
		age = 2018 - int(yr) 
		totalAge += age
		totalPpl += 1

	avrg = totalAge/totalPpl
	intAvrg = int(avrg) 

	return intAvrg  
# #Find the average age (rounded) of the Students
# # Input: list of dictionaries
# # Output: Return the average age of the students and round that age to the nearest
# # integer.  You will need to work with the DOB and the current date to find the current
# # age in years.
	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
