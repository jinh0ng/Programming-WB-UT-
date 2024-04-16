# File: Project1.py
# Student:  Yejin Hong
# UT EID:   yh25386
# Course Name: CS303E
# 
# Date: 03/01/24
# Description of Program: This is a program to calculate semester grades for multiple students based on inputs for homeworks, exams, and projects, ensuring all inputs are validated and computing averages to assign letter grades.

# Constants
HW_ERROR_MESSAGE = "  Grade must be in range [0..10]. Try again."
PR_EX_ERROR_MESSAGE = "  Grade must be in range [0..100]. Try again."
HW_WEIGHT = 0.3
PROJECT_WEIGHT = 0.3
EXAM_WEIGHT = 0.4

def get_grade(prompt, error_message, min_value, max_value):
    while True:
        grade_input = input(prompt)
        if grade_input.lstrip('-').isdigit():  # Check if the input is a digit, allowing for negative sign
            grade = int(grade_input)  # Convert to integer
            if min_value <= grade <= max_value:
                return grade
            else:
                print(error_message)
        else:
            print(error_message)


def compute_average(grades):
    """Compute weighted average of grades."""
    return sum(grades) / len(grades)

def compute_final_grade(hw_avg, project_avg, exam_avg):
    """Compute final grade based on component averages."""
    return hw_avg * HW_WEIGHT + project_avg * PROJECT_WEIGHT + exam_avg * EXAM_WEIGHT

def convert_to_letter_grade(final_grade):
    """Convert numeric grade to letter grade."""
    if final_grade >= 90:
        return 'A'
    elif final_grade >= 80:
        return 'B'
    elif final_grade >= 70:
        return 'C'
    elif final_grade >= 60:
        return 'D'
    else:
        return 'F'

def print_grade_report(name, hw_avg, project_avg, exam_avg, final_grade, letter_grade):
    """Print the detailed grade report for a student."""
    print("\nGrade report for: ", name)
    print("   Homework average (30% of grade): ", format(hw_avg, ".2f"))
    print("   Project average (30% of grade): ", format(project_avg, ".2f"))
    print("   Exam average (40% of grade): ", format(exam_avg, ".2f"))
    print("   Student course average: ", format(final_grade, ".2f"))
    print("   Course grade (CS303E: Spring, 2024): ", letter_grade)

def main():
    while True:
        name = input("\nEnter the student's name (or 'stop'): ")
        if name == 'stop':
            print("Thanks for using the grade calculator! Goodbye.")
            break

        print("\nHOMEWORKS:")
        hw_grades = []
        for i in range(3):
            # the range of hw is [0..10] so I multiplied by 10.
            hw_grades.append(10*get_grade("  Enter HW" + str(i+1) + " grade: ", HW_ERROR_MESSAGE, 0, 10))
            
        print("\nPROJECTS:")
        project_grades = []
        for i in range(2): 
            project_grades.append( get_grade("  Enter Pr" + str(i+1) + " grade: ", PR_EX_ERROR_MESSAGE, 0, 100))
        
        print("\nEXAMS:")
        exam_grades = []
        for i in range(2): 
            exam_grades.append(get_grade("  Enter Ex" + str(i+1) + " grade: ", PR_EX_ERROR_MESSAGE, 0, 100))

        hw_avg = compute_average(hw_grades)
        project_avg = compute_average(project_grades)
        exam_avg = compute_average(exam_grades)
        final_grade = compute_final_grade(hw_avg, project_avg, exam_avg)
        letter_grade = convert_to_letter_grade(final_grade)

        print_grade_report(name, hw_avg, project_avg, exam_avg, final_grade, letter_grade)

if __name__ == "__main__":
    main()