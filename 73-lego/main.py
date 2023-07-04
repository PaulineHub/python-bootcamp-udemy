#  How many different sets did LEGO sell in their first year? How many types of LEGO products were on offer in the year the company started?
df_sets.sort_values('year', ascending=True).head()
df_sets[df_sets['year'] == 1949]

# Find the top 5 LEGO sets with the most number of parts.
df_sets.sort_values('num_parts', ascending=False).head()
