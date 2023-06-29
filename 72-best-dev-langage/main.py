# Import Matplotlib
import matplotlib.pyplot as plt

# .pivot() allows to cahnge shape of the table (witch values is the column, the index and the values inside the table)

pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')

# We want to substitute the number 0 for each NaN value in the DataFrame.
# The inplace argument means that we are updating reshaped_df.
reshaped_df.fillna(0, inplace=True)

# Check if there are any NaN values left in the entire DataFrame with this line:
reshaped_df.isna().values.any()


