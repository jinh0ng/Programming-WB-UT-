# File: ScoreTests.py
# Student: Yejin Hong
# UT EID: yh25386
# Course Name: CS303E
# 
# Date: 03/28/24
# Description of Program: This program grades a collection of tests and prints a grade report for each student, as well as the class average.

STUDENTS = ['Kevin', 'Joe', 'Nick', 'Michael', 'Randy', 'Jermaine', 'Tito', 'Marlon', 'Jackie', 
            'Jimmy', 'Merrill', 'Alan', 'Jay', 'Wayne', 'Virl', 'Donnie', 'Phil', 'Don', 'Dick', 'Tom' ]

CORRECT =  ['A', 'C', 'C', 'B', 'A', 'A', 'D', 'A', 'C', 'C', 'C', 'B', 'A', 'A', 'C', 'D', 'C', 'A', 'A', 'D']

ANSWERS = [['C',  'C',  'B',  'A',  'B',  'C',  'A',  'D',  'C',  'A',  'D',  'A',  'C',  None,  'C',  'B',  'A',  'B',  'A',  'B'],
           ['B',  'D',  'B',  'B',  'B',  'D',  'B',  'C',  'C',  'A',  'C',  'C',  'D',  'B',  'A',  'B',  'A',  'A' ],
           ['A',  'B',  'C',  'B',  'C',  'D',  'B',  'C',  'C',  'A',  'D',  'C',  'D',  'B',  'A',  'A',  'C',  'A',  'D',  'D'],
           [None, 'A',  None, 'B',  'D',  None, 'C',  'B',  'B',  None, 'A',  'C',  None, 'A',  'A',  'B',  'B',  'D',  'C',  'A'],
           ['D',  'G',  'C',  'D',  'C',  'D',  'A',  'C',  'D',  'D',  'C',  'D',  'A',  'D',  'A',  'D',  'A',  'D',  'C',  'A'],
           ['B',  'C',  'C',  'B',  'C',  'B',  'C',  'C',  'C',  'C',  'D',  'A',  'D',  'A',  'A',  'D',  'D',  'D',  'D',  'A'],
           ['B',  'C',  'C',  'B',  'C',  'D',  'B',  'C',  'C',  'A',  'D',  'A',  'D',  'B',  'A',  'A',  'A',  'D',  'D',  'D'],
           ['D',  'C',  'A',  'B',  'C',  'D',  'B',  'B',  'A',  'A',  'D',  'A',  'D',  'A',  'B',  'A',  'A',  'D',  'D',  'B'],
           ['B',  'C',  'C',  'A',  'C',  'C',  'B',  'C',  'C',  'A',  'D',  'A',  'A',  'B',  'C',  'A',  'A',  'D',  'D',  'D'],
           ['B',  'B',  'B',  'B',  'C',  'D',  'C',  'B',  'C',  'C',  'D',  'A',  'B',  'D',  'A',  'A',  'B',  'D',  'C',  'C'],
           ['B',  'C',  'D',  'D',  'A',  'D',  'D',  'C',  'C',  'C',  'D',  'A',  'A',  'A',  'C',  'A',  'A',  'D',  'A',  'D'],
           ['B',  'C',  'C',  'B',  'C',  'D',  'B',  'C',  'C',  'A',  'D',  'A',  'D',  'B',  'A',  'A',  'A',  'D',  'D',  'D'],
           ['C',  'C',  'C',  'B',  'C',  'D',  'B',  'D',  'B',  'A',  'D',  'D',  'C',  'C',  'A',  'A',  'B',  'C',  'B',  'C'],
           ['A',  'A',  'A',  'D',  'C',  'B',  'B',  'A',  'B',  'D',  'A',  'D',  'C',  'C',  'D',  'D',  'B',  'A',  'D',  'D'],
           ['B',  'C',  'D',  'A',  'C',  'D',  'C',  'C',  'B',  'A',  'D',  'B',  'D',  'B',  'A',  'A',  'A',  'D',  'D',  'D'],
           ['B',  'D',  'C',  'B',  'C',  'C',  'B',  'D',  'C',  'A',  'D',  'A',  'D',  'B',  'A',  'A',  'A',  'D',  'D',  'D'],
           ['D',  'D',  'A',  'B',  'D',  'D',  'B',  'D',  'A',  'A',  'D',  'A',  'C',  'B',  'A',  'D',  'C',  'D',  'A',  'D'],
           ['B',  'C',  'C',  'B',  'C',  'A',  'B',  'A',  'C',  'D',  'C',  'A',  'A',  'A',  'A',  'B',  'A',  'B',  'B',  'B'],
           ['A',  'A',  'C',  'B',  'D',  'D',  'C',  'A',  'C',  'A',  'A',  'D',  'D',  'C',  'D',  'D',  'A',  'A',  'C',  'A'],
           ['D',  'C',  'C',  'C',  'D',  'D',  'B',  'C',  'C',  'A',  'D',  'A',  'D',  'B',  'A',  'C',  'D',  'A',  'D',  'B']]

def grade_tests(STUDENTS, CORRECT, ANSWERS):
    total_correct = 0
    total_students = 0
    
    print("Student        Grade")
    print("--------------------")
    
    # Iterate over each student's answers
    for i in range(len(STUDENTS)):
        student = STUDENTS[i]
        correct_answers = 0
        student_answers = ANSWERS[i]
        
        # Check if student's answer list has correct format
        if len(student_answers) != len(CORRECT):
            print("{:<10}: Bad format in answer list.".format(student))
            continue
        
        for j in range(len(CORRECT)):
            if student_answers[j] == CORRECT[j]:
                correct_answers += 1
            elif student_answers[j] is None or student_answers[j] not in ['A', 'B', 'C', 'D']:
                pass
        
        # Calculate grade percentage
        grade = (correct_answers / len(CORRECT)) * 100
        total_correct += correct_answers
        total_students += 1
        
        print("{:<10}: {:7.2f}".format(student, grade))

    class_average = (total_correct / (total_students * len(CORRECT))) * 100
    print("--------------------")
    print("Average   :  ", "{:.2f}".format(class_average))


grade_tests(STUDENTS, CORRECT, ANSWERS)