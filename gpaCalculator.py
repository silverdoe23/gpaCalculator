#!/usr/bin/python
import sys

gpaNumbers = {'A+': 4.0, 'A':4.0, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7, 'C+': 2.4, 'C':2.0, 'C-':1.7, 'F':1.0}


#HT of letter grades (A+, A, A-, B+, B, B-, etc.) and numbers (4, 4, 3.7, )

#main user interaction function
#function that translates grade to number
#function that calculates GPA


#user passes in their  .txt file
#prints the GPA, then the steps if desired

def organiseFile(filePath):
    with open(filePath) as gradeFile:
        gradeFile_read = gradeFile.read()
        myGradeList = [x.strip() for x in gradeFile_read.split(',')]
        return myGradeList


def calculate_GPA(gradeList):
    total = 0
    for i in gradeList:
       # if i in gpaNumbers.keys():
          #  print(i) 
        total += gpaNumbers[i]
    GPA = total / len(gradeList)
    print('Your GPA is ' + str(GPA))
    steps = raw_input('\nWould you like to see the steps (Yes/No)? ')
    if steps == 'Yes':
        show_steps(gradeList, GPA)


def show_steps(theGradeList, GPA):
    for i in theGradeList:
        print(i + ' --> '+ str(gpaNumbers[i]))
    print(str(gpaNumbers[theGradeList[0]]) + '+ ... + ' + str(gpaNumbers[theGradeList[-1]]) + ' =')
    print(GPA*len(theGradeList))
    print(str(GPA*len(theGradeList)) + ' divided by '+ str(len(theGradeList)) + ' (the number of letter grades you inputed) is ' + str(GPA))



if __name__ == '__main__':
    myFilePath = sys.argv[1]
    reportCard_list = organiseFile(myFilePath)
    calculate_GPA(reportCard_list)
