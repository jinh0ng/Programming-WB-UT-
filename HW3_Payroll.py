# File:     Payroll.py
# Student:  Yejin Hong
# UT EID:   yh25386  
# Course:   CS303E
# 
# Date:     02/01/24
# Description of Program: A program calculating payroll of entered employee's


if __name__=="__main__":
    employee = input("Employee's name: ")
    hours = float(input("Enter number of hours worked in a week: "))
    pay_rate = float(input("Enter hourly pay rate: "))
    federal_tax_rate = float(input("Enter federal tax withholding rate: "))
    state_tax_rate = float(input("Enter state tax withholding rate: "))
    gross_pay = hours * pay_rate
    federal_tax = federal_tax_rate*gross_pay
    state_tax = gross_pay*state_tax_rate

    print("\nEmployee Name: %s" %(employee))
    print("Hours worked: %.1f" %(hours))
    print("Pay rate: $%.2f" %(pay_rate))
    print("Gross pay: $%.2f" %(gross_pay))
    print("Deductions:")
    print(" Federal Withholding (%.1f%%): $%.2f" %(federal_tax_rate*100, federal_tax ))
    print(" State Withholding (%.1f%%): $%.2f" %(state_tax_rate*100, state_tax))
    print(" Total Deduction: $%.2f" %(federal_tax + state_tax))
    print("Net Pay: $%.2f" %(gross_pay - federal_tax - state_tax))