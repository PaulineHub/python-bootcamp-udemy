import pandas as pd

#Import file
df = pd.read_csv('salaries_by_college_major.csv')

# Print head of the table
df.head()

# Get number of rows
len(df.index)

# Get number of columns
len(df.columns)

# Get lables of columns
list(df.columns.values)

# Visualize NaN values (true or false in each cell)
df.isna()

# Print tail of the table
df.tail()

# Delete last row with NaN values
clean_df = df.dropna()
clean_df.tail()

# To access a particular column from a data frame we can use the square bracket notation:
clean_df['Starting Median Salary']

# Find the highest starting salary
clean_df['Starting Median Salary'].max()

# the .idxmax() method will give us index for the row with the largest value.
clean_df['Starting Median Salary'].idxmax() # return 43

# See the name of the major that corresponds to that particular row
clean_df['Undergraduate Major'].loc[43]
clean_df['Undergraduate Major'][43] # Works too.

# If you don't specify a particular column you can use the .loc property to retrieve an entire row:
clean_df.loc[43]

# How would we calculate the difference between the earnings of the 10th and 90th percentile?
# print a new column with result for each row
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']

# Add the new column to our existing dataframe
# The first argument is the position of where the column should be inserted. In our case, it's at position 1, so the second column.
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

# To see which degrees have the smallest spread, we can use the .sort_values() method. And since we are interested in only seeing the name of the degree and the major, we can pass a list of these two column names to look at the .head() of these two columns exclusively.
low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

# We have three categories in the 'Group' column: STEM, HASS and Business. Let's count how many majors we have in each category:
clean_df.groupby('Group').count()

# Average salary by group
# We can tell Pandas to print the numbers in our notebook to look like 1,012.45 with the following line:
pd.options.display.float_format = '{:,.2f}'.format
clean_df.groupby('Group').mean()


# Learning Points


# Use .head(), .tail(), .shape and .columns to explore your DataFrame and find out the number of rows and columns as well as the column names.

# Look for NaN(not a number) values with .findna() and consider using .dropna() to clean up your DataFrame.

# You can access entire columns of a DataFrame using the square bracket notation: df['column name'] or df[['column name 1', 'column name 2', 'column name 3']]

# You can access individual cells in a DataFrame by chaining square brackets df['column name'][index] or using df['column name'].loc[index]

# The largest and smallest values, as well as their positions, can be found with methods like .max(), .min(), .idxmax() and .idxmin()

# You can sort the DataFrame with .sort_values() and add new columns with .insert()

# To create an Excel Style Pivot Table by grouping entries that belong to a particular category use the .groupby() method
