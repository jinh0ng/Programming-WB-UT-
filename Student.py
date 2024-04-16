# File: Student.py
# Student:  Yejin Hong
# UT EID:   yh25386
# Course Name: CS303E
# 
# Date: 03/04/24
# Description of Program: 

class Student:
    def __init__(self, name, exam1=None, exam2=None):
        self.__name = name
        self.__exam1 = exam1
        self.__exam2 = exam2

    def getName(self):
        return self.__name

    def getExam1Grade(self):
        return self.__exam1

    def setExam1Grade(self, grade):
        self.__exam1 = grade

    def getExam2Grade(self):
        return self.__exam2

    def setExam2Grade(self, grade):
        self.__exam2 = grade

    def getAverage(self):
        if self.__exam1 is None or self.__exam2 is None:
            return "Some exam grades not available."
        else:
            return (self.__exam1 + self.__exam2) / 2

    def __str__(self):
        student_info = "Student: " + self.__name + "\n"
        student_info += "  Exam1: " + (str(self.__exam1) if self.__exam1 is not None else "None") + "\n"
        student_info += "  Exam2: " + (str(self.__exam2) if self.__exam2 is not None else "None")
        return student_info
