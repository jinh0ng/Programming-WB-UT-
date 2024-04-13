# File: MinMax.py
# Student: Yejin Hong 
# UT EID: yh25386
# Course Name: CS303E
# 
# Date: 02/17/24
# Description of Program: This code prompts the user to input integers or 'stop' to end. It calculates the count of numbers entered, as well as the minimum and maximum values.
def main():
    count = 0
    min_num = None
    max_num = None
    
    user_input = input("Enter an integer or 'stop' to end: ")
    
    while user_input != 'stop':
        if user_input[0] == '+' or user_input[0] == '-':
            if user_input[1:].isdigit():
                num = int(user_input)
                if min_num == None or num < min_num:
                    min_num = num
                if max_num == None or num > max_num:
                    max_num = num
                count += 1
            else:
                print("Invalid input! Please enter an integer or 'stop'.")
        elif user_input.isdigit():
            num = int(user_input)
            if min_num == None or num < min_num:
                min_num = num
            if max_num == None or num > max_num:
                max_num = num
            count += 1
        else:
            print("Invalid input! Please enter an integer or 'stop'.")
        
        user_input = input("Enter an integer or 'stop' to end: ")
    
    if count == 0:
        print("\nYou didn't enter any numbers.\n")
    else:
        if count > 1:
            print("\nYou entered", count, "numbers.")
        elif count == 1:
            print("\nYou entered", count, "number.")
        print("The maximum is", max_num)
        print("The minimum is", min_num)

if __name__ == "__main__":
    main()
