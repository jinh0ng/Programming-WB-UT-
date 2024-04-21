# File: Benford.py
# Student: Yejin Hong
# UT EID:  yh25386
# Course Name: CS303E
# 
# Date:   04/03/24
# Description of Program: This program validates Benford's Law for population data of Texas counties by extracting the population numbers from a given file, counting the leading digits of the population numbers, and generating output showing the distribution of leading digits both on the terminal and in a file named "benford.txt".

import os

def validate_file_existence(file_name):
    """Check if the given file exists."""
    return os.path.exists(file_name)

def extract_population_data(file_name):
    """Extract population data from the given file."""
    population_data = []
    with open(file_name, 'r') as file:
        for line in file:
            if '#' not in line:  # Ignore comment lines
                data = line.split('&')
                pop_2020 = data[6].replace(',', '').strip()  # Remove commas and space
                pop_2022 = data[7].replace(',', '').strip()  # Remove commas space
                population_data.append((pop_2020, pop_2022))
    return population_data

def count_leading_digits(population_data):
    """Count leading digits in population data."""
    digit_counts = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    for pop_2020, pop_2022 in population_data:
        if pop_2020:  # Check if population value exists
            first_digit = pop_2020[0]
            digit_counts[first_digit] += 1
        if pop_2022:  # Check if population value exists
            first_digit = pop_2022[0]
            digit_counts[first_digit] += 1
    return digit_counts

# function to check if the right values go inside the variables. (for debugging)
def print_output(total_count, unique_count, digit_counts):
    """Print output to the terminal."""
    #print("Total number of counties:", total_count)
    #print("Unique population counts:", unique_count)
    #print("First digit frequency distributions:")
    #print("Digit\tCount\tPercentage")
    for digit, count in digit_counts.items():
        percentage = (count / (total_count * 2)) * 100  # Total count is multiplied by 2 since we are counting both 2020 and 2022 population data
        #print(digit + "\t" + str(count) + "\t" + "{:.1f}%".format(percentage))

# I had to use file.write() to make output file(.txt)
def write_output_to_file(total_count, unique_count, digit_counts):
    """Write output to the file."""
    with open("benford.txt", 'w') as file:
        file.write("Total number of counties: {}\n".format(total_count))
        file.write("Unique population counts: {}\n".format(unique_count))
        file.write("First digit frequency distributions:\n")
        file.write("Digit\tCount\tPercentage\n")
        for digit, count in digit_counts.items():
            percentage = (count / (total_count * 2)) * 100  # Total count is multiplied by 2 since we are counting both 2020 and 2022 population data
            file.write("{}\t{}\t{:.1f}%\n".format(digit, count, percentage))
    print("Output written to benford.txt")

def main():
    file_name = input("Enter the name of a file: ")
    
    if not validate_file_existence(file_name):
        print("File does not exist")
        return
    
    population_data = extract_population_data(file_name)
    total_count = len(population_data)
    unique_count = len(set(population_data))
    digit_counts = count_leading_digits(population_data)
    
    #print_output(total_count, unique_count, digit_counts)
    write_output_to_file(total_count, unique_count, digit_counts)

if __name__ == "__main__":
    main()