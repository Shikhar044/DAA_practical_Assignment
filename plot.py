import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("results.csv")

# ---------------- QUICK SORT (AVERAGE CASE) ----------------
qs = data[data['Algorithm'].isin(['QuickFirst','QuickRandom','QuickMedian'])]
qs_avg = qs[qs['InputType'] == 'Random']

plt.figure()

for algo in qs_avg['Algorithm'].unique():
    subset = qs_avg[qs_avg['Algorithm'] == algo].sort_values(by='N')
    plt.plot(subset['N'], subset['Time'], marker='o', label=algo)

plt.xlabel("Input Size (N)")
plt.ylabel("Time (seconds)")
plt.title("QuickSort Pivot Comparison (Average Case)")
plt.legend()
plt.grid()
plt.savefig("quick_comparison.png")
plt.show()


# ---------------- QUICK SORT (BEST CASE) ----------------
qs_sorted = qs[qs['InputType'] == 'Sorted']

plt.figure()

for algo in qs_sorted['Algorithm'].unique():
    subset = qs_sorted[qs_sorted['Algorithm'] == algo].sort_values(by='N')
    plt.plot(subset['N'], subset['Time'], marker='o', label=algo)

plt.xlabel("Input Size (N)")
plt.ylabel("Time (seconds)")
plt.title("QuickSort Pivot Comparison (Best Case)")
plt.legend()
plt.grid()
plt.savefig("quick_best.png")
plt.show()


# ---------------- QUICK SORT (WORST CASE) ----------------
qs_reverse = qs[qs['InputType'] == 'Reverse']

plt.figure()

for algo in qs_reverse['Algorithm'].unique():
    subset = qs_reverse[qs_reverse['Algorithm'] == algo].sort_values(by='N')
    plt.plot(subset['N'], subset['Time'], marker='o', label=algo)

plt.xlabel("Input Size (N)")
plt.ylabel("Time (seconds)")
plt.title("QuickSort Pivot Comparison (Worst Case)")
plt.legend()
plt.grid()
plt.savefig("quick_worst.png")
plt.show()


# ---------------- QUICK SORT (COMPARISONS vs N) ----------------
plt.figure()

for algo in qs_avg['Algorithm'].unique():
    subset = qs_avg[qs_avg['Algorithm'] == algo].sort_values(by='N')
    plt.plot(subset['N'], subset['Comparisons'], marker='o', label=algo)

plt.xlabel("Input Size (N)")
plt.ylabel("Number of Comparisons")
plt.title("QuickSort Comparisons vs Input Size")
plt.legend()
plt.grid()
plt.savefig("quick_comparisons.png")
plt.show()


# ---------------- QUICK SORT (TIME PER COMPARISON) ----------------
qs_avg = qs_avg.copy()
qs_avg['TimePerComparison'] = qs_avg['Time'] / qs_avg['Comparisons'].replace(0, 1)

plt.figure()

for algo in qs_avg['Algorithm'].unique():
    subset = qs_avg[qs_avg['Algorithm'] == algo].sort_values(by='N')
    plt.plot(subset['N'], subset['TimePerComparison'], marker='o', label=algo)

plt.xlabel("Input Size (N)")
plt.ylabel("Time per Comparison")
plt.title("QuickSort Time per Comparison")
plt.legend()
plt.grid()
plt.savefig("quick_time_per_comp.png")
plt.show()


# ---------------- ALL ALGORITHMS (ONLY BEST QUICK SORT) ----------------
algorithms = ['Selection','Bubble','Insertion','Merge','Heap','Radix','QuickMedian']


# -------- AVERAGE CASE --------
avg = data[data['InputType'] == 'Random']

plt.figure()

for algo in algorithms:
    subset = avg[avg['Algorithm'] == algo].sort_values(by='N')
    plt.plot(subset['N'], subset['Time'], marker='o', label=algo)

plt.xlabel("Input Size (N)")
plt.ylabel("Time (seconds)")
plt.title("All Algorithms Comparison (Average Case)")
plt.legend()
plt.grid()
plt.savefig("all_algorithms.png")
plt.show()


# -------- BEST CASE --------
best = data[data['InputType'] == 'Sorted']

plt.figure()

for algo in algorithms:
    subset = best[best['Algorithm'] == algo].sort_values(by='N')
    plt.plot(subset['N'], subset['Time'], marker='o', label=algo)

plt.xlabel("Input Size (N)")
plt.ylabel("Time (seconds)")
plt.title("All Algorithms Comparison (Best Case)")
plt.legend()
plt.grid()
plt.savefig("all_best.png")
plt.show()


# -------- WORST CASE --------
worst = data[data['InputType'] == 'Reverse']

plt.figure()

for algo in algorithms:
    subset = worst[worst['Algorithm'] == algo].sort_values(by='N')
    plt.plot(subset['N'], subset['Time'], marker='o', label=algo)

plt.xlabel("Input Size (N)")
plt.ylabel("Time (seconds)")
plt.title("All Algorithms Comparison (Worst Case)")
plt.legend()
plt.grid()
plt.savefig("all_worst.png")
plt.show()


# ---------------- COMPARISONS vs TIME ----------------
plt.figure()
plt.scatter(data['Comparisons'], data['Time'])

plt.xlabel("Comparisons")
plt.ylabel("Time")
plt.title("Comparisons vs Time")
plt.grid()
plt.savefig("comparison_vs_time.png")
plt.show()