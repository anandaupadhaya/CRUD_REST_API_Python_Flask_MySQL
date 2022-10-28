'''''
# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Anuj', 'Jai', 'Princi',
                  'Gaurav', 'Anuj', 'Princi', 'Abhi'],
         'Age': [27, 24, 22, 32,
                 33, 36, 27, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                     'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd',
                           'B.Tech', 'B.com', 'Msc', 'MA']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1)

print(df)
print("________________________________________________________")
df.groupby('Name')
print(df.groupby('Name').groups)

print("___________________________________________________")
# applying groupby() function to
# group the data on Name value.
gk = df.groupby('Name')

# Let's print the first entries
# in all the groups formed.
print(gk.first())

'''''

'''''
# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Anuj', 'Jai', 'Princi',
                  'Gaurav', 'Anuj', 'Princi', 'Abhi'],
         'Age': [27, 24, 22, 32,
                 33, 36, 27, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                     'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd',
                           'B.Tech', 'B.com', 'Msc', 'MA']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1)
print("_____________________________________________________")
print(df)
print("_____________________________________________________")
# Using multiple keys in
# groupby() function
df.groupby(['Name', 'Qualification'])

print(df.groupby(['Name', 'Qualification']).groups)

print("_____________________________________________________")
'''''

'''''
# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Anuj', 'Jai', 'Princi',
                  'Gaurav', 'Anuj', 'Princi', 'Abhi'],
         'Age': [27, 24, 22, 32,
                 33, 36, 27, 32], }

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1)

print(df)

print("________________________________________________")
# using groupby function
# without using sort

print(df.groupby(['Name']).sum())

print("__________________________________________________")

# using groupby function
# with sort

df.groupby(['Name'], sort=False).sum()


print("__________________________________________________")


'''''

'''''
# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Anuj', 'Jai', 'Princi',
                  'Gaurav', 'Anuj', 'Princi', 'Abhi'],
         'Age': [27, 24, 22, 32,
                 33, 36, 27, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                     'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd',
                           'B.Tech', 'B.com', 'Msc', 'MA']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1)

print(df)
print("______________________________________________")

# using keys for grouping
# data

print(df.groupby('Name').groups)


print("________________________________________________________")

'''''

'''''

# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Anuj', 'Jai', 'Princi',
                  'Gaurav', 'Anuj', 'Princi', 'Abhi'],
         'Age': [27, 24, 22, 32,
                 33, 36, 27, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                     'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd',
                           'B.Tech', 'B.com', 'Msc', 'MA']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1)

print(df)

print("_________________________________________________________")

# iterating an element
# of group

grp = df.groupby('Name')
for name, group in grp:
    print(name)
    print(group)
    print()

print("_____________________________________________")

# iterating an element
# of group containing
# multiple keys

grp = df.groupby(['Name', 'Qualification'])
for name, group in grp:
    print(name)
    print(group)
    print()


print("__________________________________________________")

'''''

'''''
# importing pandas module
import pandas as pd

# importing numpy as np
import numpy as np

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Anuj', 'Jai', 'Princi',
                  'Gaurav', 'Anuj', 'Princi', 'Abhi'],
         'Age': [27, 24, 22, 32,
                 33, 36, 27, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                     'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd',
                           'B.Tech', 'B.com', 'Msc', 'MA']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1)

print(df)
print("_________________________________________________________")

# selecting a single group
grp = df.groupby('Name')
print(grp.get_group('Jai'))

print("_________________________________________________")

# selecting object grouped
# on multiple columns

grp = df.groupby(['Name', 'Qualification'])
print(grp.get_group(('Jai', 'Msc')))

print("_________________________________________________")

# performing aggregation using
# aggregate method

grp1 = df.groupby('Name')

print(grp1.aggregate(np.sum))

print("______________________________________________________")

# performing aggregation on
# group containing multiple
# keys
grp1 = df.groupby(['Name', 'Qualification'])

print(grp1.aggregate(np.sum))

'''''

'''''
import pandas as pd

data = {
  "x": [50, 40, 30],
  "y": [300, 1112, 42]
}

df = pd.DataFrame(data)
print(df)

x = df.aggregate(["sum"])

print(x)

'''''
'''''

# importing pandas library
import pandas as pd

# Initializing the nested list with Data set
player_list = [['M.S.Dhoni', 36, 75, 5428000],
               ['A.B.D Villers', 38, 74, 3428000],
               ['V.Kholi', 31, 70, 8428000],
               ['S.Smith', 34, 80, 4428000],
               ['C.Gayle', 40, 100, 4528000],
               ['J.Root', 33, 72, 7028000],
               ['K.Peterson', 42, 85, 2528000]]

# creating a pandas dataframe
df = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])

# data frame before slicing
print(df)

print("___________________________________")

# Slicing rows in data frame
df1 = df.iloc[0:4]

# data frame after slicing
print(df1)

print("__________________________________________")

# Slicing columnss in data frame
df1 = df.iloc[:, 0:2]

# data frame after slicing
print(df1)


print("_________________________________________________")


for ind in df.index:
    print(df['Name'][ind], df['Weight'][ind])


print("____________________________________________")


# iterate through each row and select
# 'Name' and 'Weight' column respectively.
for i in range(len(df)):
    print(df.loc[i, "Name"], df.loc[i, "Weight"])

print("________________________________________")

# iterate through each row and select
# 0th and 2nd index column respectively.
for i in range(len(df)):
    print(df.iloc[i, 0], df.iloc[i, 2])

print("____________________________________________")


# iterate through each row and select
# 'Name' and 'Age' column respectively.
for index, row in df.iterrows():
    print(row["Name"], row["Weight"])


print("_______________________________________________")


# iterate through each row and select
# 'Name' and 'Percentage' column respectively.
for row in df.itertuples(index=True, name='Pandas'):
    print(getattr(row, "Name"), getattr(row, "Weight"))

print("___________________________________________________")


# iterate through each row and concatenate
# 'Name' and 'Percentage' column respectively.
print(df.apply(lambda row: row["Name"] + " " +
               str(row["Weight"]), axis=1))

print("______________________________________________")
print(df.count())
print("____________________________________________")

print(df.drop_duplicates())

print("_______________________________________________")

# sorting by first name
print(df.sort_values("Name", inplace=True))

print("______________________________________")
# dropping duplicate values
print(df.drop_duplicates(keep=False, inplace=True))

print("__________________________________________")

# length after removing duplicates
length3 = len(df)
print(length3)
print("____________________________________________")

print(df["Name"])

print("_________________________________________________")

'''''
'''''
# importing pandas

import pandas as pd

# Creating dataframe a
a = pd.DataFrame()

# Creating Dictionary
d = {'id': [1, 2, 10, 12],
     'val1': ['a', 'b', 'c', 'd']}

a = pd.DataFrame(d)

# Creating dataframe b
b = pd.DataFrame()

# Creating dictionary
d = {'id': [1, 2, 9, 8],
     'val1': ['p', 'q', 'r', 's']}
b = pd.DataFrame(d)

# printing the dataframe
print(b)

# printing the dataframe
print(a)

# inner join
df_join = pd.merge(a, b, on='id', how='inner')

print(df_join)

# left outer join
df_l_outer_join = pd.merge(a, b, on='id', how='left')

print(df_l_outer_join)

# right outer join
df_outer = pd.merge(a, b, on='id', how='right')

# display dataframe
print(df_outer)

# full outer join
df_outer_full = pd.merge(a, b, on='id', how='outer')

# display dataframe
print(df_outer_full)

# index join
df_index = pd.merge(a, b, left_index=True, right_index=True)

# display dataframe
print(df_index)

#print(b.pivot('id', columns="val1"))

'''''

'''''
# importing pandas as pd
import pandas as pd

# creating a dataframe
df = pd.DataFrame({'A': ['John', 'Boby', 'Mina'],
                   'B': ['Masters', 'Graduate', 'Graduate'],
                   'C': [27, 23, 21]})

print(df)

print("__________________________________________")
# values can be an object or a list
print(df.pivot('A', 'B', 'C'))

'''''

'''''
# importing pandas as pd
import pandas as pd

# Creating the DataFrame
df = pd.DataFrame({"A": [12, 4, 5, None, 1],
                   "B": [7, 2, 54, 3, None],
                   "C": [20, 16, 11, 3, 8],
                   "D": [14, 3, None, 2, 6]})

# Create the index
index = ['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5']

# Set the index
df.index = index

# Print the DataFrame
print(df)
print("_________________________________________")


# add 10 to each element of the dataframe
result = df.transform(func=lambda x: x + 10)

# Print the result
print(result)

print("_______________________________________________")

# pass a list of functions
result = df.transform(func=['sqrt', 'exp'])

# Print the result
print(result)
'''''

# function to returns x*x
def squareData(x):
     return x * x


# import pandas and numpy packages
import pandas as pd
import numpy as np

# list of tuples
matrix = [(1, 2, 3, 4),
          (5, 6, 7, 8,),
          (9, 10, 11, 12),
          (13, 14, 15, 16)
          ]

# Creating a Dataframe object
df = pd.DataFrame(matrix, columns=list('abcd'))
print(df)

print("______________________________________________")

# Applying a user defined function to
# each column that will square the given
# value
new_df = df.apply(squareData)

# Output
print(new_df)

print("_______________________________________________")

new_new_df = df.apply(np.square)

print(new_new_df)


