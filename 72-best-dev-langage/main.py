# Import Matplotlib
import matplotlib.pyplot as plt

# .pivot() allows to cahnge shape of the table (witch values is the column, the index and the values inside the table)

pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')

# We want to substitute the number 0 for each NaN value in the DataFrame.
# The inplace argument means that we are updating reshaped_df.
reshaped_df.fillna(0, inplace=True)

# Check if there are any NaN values left in the entire DataFrame with this line:
reshaped_df.isna().values.any()

# Use the matplotlib documentation to plot a single programming language (e.g., java) on a chart.
x = reshaped_df.index
y = reshaped_df['java']

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
plt.plot(x, y)

# Show two line (e.g. for Java and Python) on the same chart.
plt.plot(x, y, x, reshaped_df['python'])
#OU
plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)

# A useful technique to make a trend apparent is to smooth out the observations by taking an average. By averaging say, 6 or 12 observations we can construct something called the rolling mean. Essentially we calculate the average in a window of time and move it forward by one observation at a time.

# Since this is such a common technique, Pandas actually two handy methods already built-in: rolling() and mean(). We can chain these two methods up to create a DataFrame made up of the averaged observations.

# Plus l'indice de windiw est grand, plus on fait de fenetre d'observation, plus on 'smooth' le graphique.
roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)


# Learning Points & Summary
# Today we've seen how to grab some raw data and create some interesting charts using Pandas and Matplotlib. We've: 

# used .groupby() to explore the number of posts and entries per programming language

# converted strings to Datetime objects with to_datetime() for easier plotting

# reshaped our DataFrame by converting categories to columns using .pivot()

# used .count() and isna().values.any() to look for NaN values in our DataFrame, which we then replaced using .fillna()

# created(multiple) line charts using .plot() with a for-loop

# styled our charts by changing the size, the labels, and the upper and lower bounds of our axis.

# added a legend to tell apart which line is which by colour

# smoothed out our time-series observations with .rolling().mean() and plotted them to better identify trends over time.
