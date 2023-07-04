# Jackson Small
# July 1, 2023
# One Variable Statistics Calculator
# Inlcudes: mean, sum, sum of x^2, sample stdev, population stdev, n, MinX, Q1, median, Q3, MaxX, IQR, lower fence, upper fence, outliers, and SSX. 

import numpy as np

# Inputs to array

numbers = []

while True:
    number = input("Please enter a number or enter 'q' to quit: ")

    if number.lower() == 'q':
        break
    try:
        number = float(number)
        numbers.append(number)

    except ValueError:
        print("That is not a number. Please enter a number")


    x_val = np.array(numbers)

print("X - Values:", x_val, sep="\n")

# checks for outliers in np array
def check_outlier(array):
    outliers = x_val[(x_val < lower_fence) | (x_val > upper_fence)]

    return outliers


# Calculates Mean
mean_x = np.mean(x_val)
print("Mean: ", mean_x)

# Calculates Sum
sum_x = np.sum(x_val)
print("Sum of X: ", sum_x)

# Calculates Sum(x**2)
x_val_squared_arr = np.sum(x_val)**2
sum_x_squared = np.sum((x_val_squared_arr))

print("sum of x^2: ", sum_x_squared)


# Caluclates Sample Standard Deviation
sample_stdev = np.std(x_val, ddof=1)
print("Sample Stdev: ", sample_stdev)

# Caluclates Population Standard Deviation
population_stdev = np.std(x_val)
print("Population Stdev: ", population_stdev)

# Calculates n
n = np.size(x_val)
print("n:", n)

# Calculates Min
min_x = np.min(x_val)
print("MinX:", min_x)

# Calculates Q1_x
q1_x = np.percentile(x_val, 25.0, method='nearest')
print("q1 of x:", q1_x)

# Calculates Median
median_x = np.median(x_val)
print("Median: ", median_x)

# Calculate Q3_x
q3_x = np.percentile(x_val, 75.0, method='nearest')
print("q3 of x:", q3_x)

# Calculates Max
max_x = np.max(x_val)
print("MaxX: ", max_x)

# Calculates IQR
iqr_x = (q3_x - q1_x)
print("IQR: ", iqr_x)

# Calculates Lower Fence
lower_fence = q1_x - (iqr_x * 1.5)
print("Lower Fence: ", lower_fence)

# Calculates Upper Fence
upper_fence = q3_x + (iqr_x * 1.5)
print("Upper Fence: ", upper_fence)

# Checks for Outliers
outliers = check_outlier(x_val)
print("The outliers are: ", outliers)


# Calculates SSX sum(x - x_bar)**2
ssx_arr = np.sum(((x_val - mean_x)**2))
ssx = np.sum(ssx_arr)
print("SSX: ", ssx)



