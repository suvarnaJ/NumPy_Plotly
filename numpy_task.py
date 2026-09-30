import numpy as np


# ============================================================
# 1. ARRAY CREATION
# ============================================================

print("\n========== 1. ARRAY CREATION ==========")

# Numbers 1-50
numbers_1_to_50 = np.arange(1, 51)

# Even numbers 2-100
even_numbers = np.arange(2, 101, 2)

# Odd numbers 1-99
odd_numbers = np.arange(1, 100, 2)

print("Numbers 1-50:")
print(numbers_1_to_50)

print("\nEven numbers 2-100:")
print(even_numbers)

print("\nOdd numbers 1-99:")
print(odd_numbers)


# ============================================================
# 2. STUDENT MARKS ANALYSIS
# ============================================================

print("\n========== 2. STUDENT MARKS ANALYSIS ==========")

marks = np.array([
    78, 85, 92, 67, 88,
    73, 95, 60, 84, 91
])

total_marks = np.sum(marks)
average_marks = np.mean(marks)
maximum_marks = np.max(marks)
minimum_marks = np.min(marks)
median_marks = np.median(marks)

print("Marks:", marks)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Maximum Marks:", maximum_marks)
print("Minimum Marks:", minimum_marks)
print("Median Marks:", median_marks)


# ============================================================
# 3. FILTERING
# ============================================================

print("\n========== 3. FILTERING ==========")

# Students scoring above 90
above_90 = marks[marks > 90]

# Students scoring above average
above_average = marks[marks > average_marks]

# Students scoring below 70
below_70 = marks[marks < 70]

print("Students scoring above 90:")
print(above_90)

print("\nStudents scoring above average:")
print(above_average)

print("\nStudents scoring below 70:")
print(below_70)


# ============================================================
# 4. RESHAPING
# ============================================================

print("\n========== 4. RESHAPING ==========")

numbers_1_to_20 = np.arange(1, 21)

matrix_4x5 = numbers_1_to_20.reshape(4, 5)

print("Numbers 1-20:")
print(numbers_1_to_20)

print("\n4 x 5 Matrix:")
print(matrix_4x5)


# ============================================================
# 5. TWO-DIMENSIONAL ARRAY
# ============================================================

print("\n========== 5. TWO-DIMENSIONAL ARRAY ==========")

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("3 x 3 Matrix:")
print(matrix)

# Row selection
print("\nFirst Row:")
print(matrix[0])

# Second row
print("\nSecond Row:")
print(matrix[1])

# Column selection
print("\nFirst Column:")
print(matrix[:, 0])

print("\nSecond Column:")
print(matrix[:, 1])

# Individual element
print("\nIndividual Element:")
print(matrix[1, 2])


# ============================================================
# 6. MATHEMATICAL OPERATIONS
# ============================================================

print("\n========== 6. MATHEMATICAL OPERATIONS ==========")

a = np.array([10, 20, 30, 40, 50])

b = np.array([5, 10, 15, 20, 25])

print("Array A:", a)
print("Array B:", b)

# Addition
print("\nAddition:")
print(a + b)

# Subtraction
print("\nSubtraction:")
print(a - b)

# Multiplication
print("\nMultiplication:")
print(a * b)

# Division
print("\nDivision:")
print(a / b)


# ============================================================
# 7. STATISTICAL ANALYSIS
# ============================================================

print("\n========== 7. STATISTICAL ANALYSIS ==========")

# Generate 100 random numbers between 1 and 100
random_numbers = np.random.randint(1, 101, 100)

mean_value = np.mean(random_numbers)
median_value = np.median(random_numbers)
standard_deviation = np.std(random_numbers)
variance = np.var(random_numbers)

print("100 Random Numbers:")
print(random_numbers)

print("\nMean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", standard_deviation)
print("Variance:", variance)


# ============================================================
# 8. SORTING
# ============================================================

print("\n========== 8. SORTING ==========")

unsorted_array = np.array([
    45, 12, 89, 23, 67,
    5, 91, 34, 78, 10
])

ascending = np.sort(unsorted_array)

# Reverse the ascending array
descending = ascending[::-1]

print("Original Array:")
print(unsorted_array)

print("\nAscending Order:")
print(ascending)

print("\nDescending Order:")
print(descending)


# ============================================================
# 9. UNIQUE VALUES
# ============================================================

print("\n========== 9. UNIQUE VALUES ==========")

values = np.array([
    1, 2, 2, 3, 3,
    3, 4, 5, 5, 6
])

unique_values = np.unique(values)

print("Original Array:")
print(values)

print("\nUnique Values:")
print(unique_values)


# ============================================================
# 10. MATRIX OPERATIONS
# ============================================================

print("\n========== 10. MATRIX OPERATIONS ==========")

matrix_a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix_b = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

# Matrix Addition
print("\nMatrix Addition:")
print(matrix_a + matrix_b)

# Matrix Subtraction
print("\nMatrix Subtraction:")
print(matrix_a - matrix_b)

# Element-wise multiplication
print("\nElement-wise Multiplication:")
print(matrix_a * matrix_b)

# Matrix multiplication
print("\nMatrix Multiplication:")
print(np.matmul(matrix_a, matrix_b))


# ============================================================
# 11. SALARY ANALYSIS
# ============================================================

print("\n========== 11. SALARY ANALYSIS ==========")

salary = np.array([
    35000,
    42000,
    50000,
    38000,
    55000,
    47000,
    62000,
    45000,
    70000,
    52000,
    48000,
    65000,
    40000,
    58000,
    75000
])

highest_salary = np.max(salary)
lowest_salary = np.min(salary)
average_salary = np.mean(salary)

employees_above_average = salary[salary > average_salary]

print("Salary Data:")
print(salary)

print("\nHighest Salary:", highest_salary)
print("Lowest Salary:", lowest_salary)
print("Average Salary:", average_salary)

print("\nEmployees earning above average:")
print(employees_above_average)


# ============================================================
# 12. CHALLENGE - 5 x 5 RANDOM INTEGER MATRIX
# ============================================================

print("\n========== 12. CHALLENGE ==========")

random_matrix = np.random.randint(1, 101, size=(5, 5))

maximum_value = np.max(random_matrix)
minimum_value = np.min(random_matrix)

row_wise_sum = np.sum(random_matrix, axis=1)
column_wise_sum = np.sum(random_matrix, axis=0)

overall_average = np.mean(random_matrix)

print("5 x 5 Random Matrix:")
print(random_matrix)

print("\nMaximum Value:")
print(maximum_value)

print("\nMinimum Value:")
print(minimum_value)

print("\nRow-wise Sum:")
print(row_wise_sum)

print("\nColumn-wise Sum:")
print(column_wise_sum)

print("\nOverall Average:")
print(overall_average)


# ============================================================
# END OF PROGRAM
# ============================================================

print("\n========== PROGRAM COMPLETED ==========")