import pandas as pd

# Load all 5 files
files = [
    "results_run1.csv",
    "results_run2.csv",
    "results_run3.csv",
    "results_run4.csv",
    "results_run5.csv"
]

dfs = [pd.read_csv(f) for f in files]

# Combine all data
combined = pd.concat(dfs)

# Group by Algorithm, N, InputType and take average
avg_df = combined.groupby(['Algorithm', 'N', 'InputType'], as_index=False).mean()

# Sort to maintain clean order
avg_df = avg_df.sort_values(by=['N', 'InputType', 'Algorithm'])

# Save final file
avg_df.to_csv("result_avg.csv", index=False)

print("✅ result_avg.csv created successfully")