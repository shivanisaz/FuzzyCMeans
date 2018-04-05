import pandas as pd
import numpy as np
import random
import operator
import math


df_full = pd.read_csv("SPECTF_New.csv")

# fetches name of columns - Attr_1,..
columns = list(df_full.columns)

#features=columns[0..len-1] i.e. all columns except 'class'
features = columns[:len(columns)-1]

# last element of columns array = 'Class', value of all rows in Class column
class_labels = list(df_full[columns[-1]])

# fetching all attributes - all values except class values
df = df_full[features]

# Number of Attributes
num_attr = len(df.columns) - 1

# Number of Clusters
k = 2

# Maximum number of iterations
MAX_ITER = 100

# Number of data points = rows
n = len(df)

# Fuzzy parameter
m = 2.00
temp_num = list()
for i in range(n):

    # all attributes of 1 data point i.e. value of ith row
    data_point = list(df.iloc[i]) 

    # multiplying membership value to value of each attribute of data point
    prod = [1 * val for val in data_point]

    temp_num.append(prod)

# print prod
# print temp_num

numerator = map(sum, zip(*temp_num))

distances = [np.linalg.norm([7419, 7354])]
print distances
