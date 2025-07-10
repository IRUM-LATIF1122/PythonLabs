# # Pandas is a popular open-source data manipulation and analysis library
# # A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).
# # A Series is a one-dimensional labeled array, essentially a single column or row of data.
#
# # lets work with series
#
# import pandas as pd
#  # Create a Series from a list Notice that Pandas automatically assigned numerical indices (0, 1, 2, 3, 4)
# # to each element, but you can also specify custom labels if needed.
#
# data = [10, 20, 30, 40, 50]
# s = pd.Series(data)
# print(s)
#
# # Accessing by label
# print('At index two value is ' ,s[2])     # Access the element with label 2 (value 30)
# # Accessing by position
# print('at position 3rd value is ', s.iloc[3]) # Access the element at position 3 (value 40)
# # Accessing multiple elements
# print('from position 1 to 4 values are ', s[1:4] ,'\n')   # Access a range of elements by label
#
# '''Pandas Series come with various attributes and methods to help you manipulate and analyze data effectively. Here are a few essential ones:
#
# values: Returns the Series data as a NumPy array.
# index: Returns the index (labels) of the Series.
# shape: Returns a tuple representing the dimensions of the Series.
# size: Returns the number of elements in the Series.
# mean(), sum(), min(), max(): Calculate summary statistics of the data.
# unique(), nunique(): Get unique values or the number of unique values.
# sort_values(), sort_index(): Sort the Series by values or index labels.
# isnull(), notnull(): Check for missing (NaN) or non-missing values.
# apply(): Apply a custom function to each element of the Series.'''
#
# # Now lets see DATAFRAMES
# # DataFrames can be created from dictionaries, with keys as column labels and values as lists representing rows.
#
#
# # Creating a DataFrame from a dictionary
# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'Age': [25, 30, 35, 25],
#         'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
# df = pd.DataFrame(data)
# print('Here is a data frame created from dictionary \n ', df)
#
# # Column Selection:
# print('coloum Name selected  & shown here \n', df['Name'])  # Access the 'Name' column
#
# # Finding Unique Elements:
# unique_dates = df['Age'].unique()
# print("unique dates in Age coloumn  are : ", unique_dates)
#
# # Conditional Filtering:
# # For instance, you can filter albums released after a certain year.
# high_above_25 = df[df['Age'] > 25]
# print('\nalbums released after age 25 :\n ' , high_above_25)
#
# #
# # Saving DataFrames:
# # To save a DataFrame to a CSV file, use the to_csv method and specify the filename with a “.csv” extension.Pandas provides other functions for saving DataFrames in different formats.
#
# df.to_csv('trading_data.csv', index=False)
#
#
# # ---------------------loc() Accesses rows and columns by their labels (names).
# # Includes the end index (when slicing).
# df = pd.DataFrame({
#     'Name': ['Ali', 'Sara', 'Ahmed'],
#     'Age': [25, 30, 22]
# }, index=['a', 'b', 'c'])
#
# # Access row with label 'a'
# print(df.loc['a'])
#
# # Access 'Age' column of row 'b'
# print(df.loc['b', 'Age'])
# print('slicing access ',df.loc['a' :'c'])
#
#
# # iloc[] — Integer-based indexing
# # Accesses rows and columns by integer position (like Python lists).
# # Indexing starts from 0.
# # Excludes the end index in slicing (like normal Python)
#
# # Access first row (index 0)
# print('now using iloc() \n')
# print(df.iloc[0])
#
# # Access value in second row (index 1), second column (index 1)
# print(df.iloc[1, 1])
#
#
# '''DataFrames provide numerous attributes and methods for data manipulation and analysis, including:
#
# shape: Returns the dimensions (number of rows and columns) of the DataFrame.
# info(): Provides a summary of the DataFrame, including data types and non-null counts.
# describe(): Generates summary statistics for numerical columns.
# head(), tail(): Displays the first or last n rows of the DataFrame.
# mean(), sum(), min(), max(): Calculate summary statistics for columns.
# sort_values(): Sort the DataFrame by one or more columns.
# groupby(): Group data based on specific columns for aggregation.
# fillna(), drop(), rename(): Handle missing values, drop columns, or rename columns.
# apply(): Apply a function to each element, row, or column of the DataFrame.'''
# # -------------------------------------------------
