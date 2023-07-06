#  How many different sets did LEGO sell in their first year? How many types of LEGO products were on offer in the year the company started?
df_sets.sort_values('year', ascending=True).head()
df_sets[df_sets['year'] == 1949]

# Find the top 5 LEGO sets with the most number of parts.
df_sets.sort_values('num_parts', ascending=False).head()

# Matplotlib : to exlude the 2 last year from the chart : 
plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])

# Count the number of unique theme_ids per calendar year.
themes_by_year = df_sets.groupby('year').agg({'theme_id': pd.Series.nunique})

# Rename the column
themes_by_year.rename(columns={'theme_id': 'nb_themes'}, inplace=True)

# Configure and plot our data on two separate axes on the same chart.
ax1 = plt.gca()  # get current axes
ax2 = ax1.twinx() # create another axis that share the same x-axis

ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
ax2.plot(themes_by_year.index[:-2], themes_by_year.nb_themes[:-2], 'b')

# Styling chart
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of sets', color='green')
ax2.set_ylabel('Number of themes', color='blue')
