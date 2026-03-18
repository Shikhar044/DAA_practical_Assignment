import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("results.csv")


qs = data[data['Algorithm'].isin(['QuickFirst','QuickRandom','QuickMedian'])]
qs = qs[qs['InputType'] == 'Random']

for algo in qs['Algorithm'].unique():
    subset = qs[qs['Algorithm'] == algo]
    plt.plot(subset['N'], subset['Time'], marker='o', label=algo)

plt.xlabel("Input Size (N)")
plt.ylabel("Time (seconds)")
plt.title("QuickSort Pivot Comparison (Average Case)")
plt.legend()
plt.grid()

plt.savefig("quick_comparison.png")
plt.show()





avg = data[data['InputType'] == 'Random']

for algo in avg['Algorithm'].unique():
    subset = avg[avg['Algorithm'] == algo]
    plt.plot(subset['N'], subset['Time'], marker='o', label=algo)

plt.xlabel("Input Size (N)")
plt.ylabel("Time (seconds)")
plt.title("All Sorting Algorithms Comparison")
plt.legend()
plt.grid()

plt.savefig("all_algorithms.png")
plt.show()




qs = data[data['Algorithm'] == 'QuickRandom']

for t in ['Random','Sorted','Reverse']:
    subset = qs[qs['InputType'] == t]
    plt.plot(subset['N'], subset['Time'], marker='o', label=t)

plt.xlabel("Input Size (N)")
plt.ylabel("Time (seconds)")
plt.title("QuickSort Case Comparison")
plt.legend()
plt.grid()

plt.savefig("quick_cases.png")
plt.show()





plt.scatter(data['Comparisons'], data['Time'])

plt.xlabel("Comparisons")
plt.ylabel("Time")
plt.title("Comparisons vs Time")
plt.grid()

plt.savefig("comparison_vs_time.png")
plt.show()


# Quick sort best case(sorted)
qs = data[data['Algorithm'].isin(['QuickFirst','QuickRandom','QuickMedian'])]
qs_sorted = qs[qs['InputType'] == 'Sorted']

plt.figure()

for algo in qs_sorted['Algorithm'].unique():
    subset = qs_sorted[qs_sorted['Algorithm'] == algo]
    plt.plot(subset['N'], subset['Time'], marker='o', label=algo)

plt.xlabel("Input Size (N)")
plt.ylabel("Time (seconds)")
plt.title("QuickSort Pivot Comparison (Best Case)")
plt.legend()
plt.grid()

plt.savefig("quick_best.png")
plt.show()


# Quick sort worst case(reverse)
qs_reverse = qs[qs['InputType'] == 'Reverse']

plt.figure()

for algo in qs_reverse['Algorithm'].unique():
    subset = qs_reverse[qs_reverse['Algorithm'] == algo]
    plt.plot(subset['N'], subset['Time'], marker='o', label=algo)

plt.xlabel("Input Size (N)")
plt.ylabel("Time (seconds)")
plt.title("QuickSort Pivot Comparison (Worst Case)")
plt.legend()
plt.grid()

plt.savefig("quick_worst.png")
plt.show()



# all algo best case
best = data[data['InputType'] == 'Sorted']

plt.figure()

for algo in best['Algorithm'].unique():
    subset = best[best['Algorithm'] == algo]
    plt.plot(subset['N'], subset['Time'], marker='o', label=algo)

plt.xlabel("Input Size (N)")
plt.ylabel("Time (seconds)")
plt.title("All Algorithms Comparison (Best Case)")
plt.legend()
plt.grid()

plt.savefig("all_best.png")
plt.show()



# all algo worst case
worst = data[data['InputType'] == 'Reverse']

plt.figure()

for algo in worst['Algorithm'].unique():
    subset = worst[worst['Algorithm'] == algo]
    plt.plot(subset['N'], subset['Time'], marker='o', label=algo)

plt.xlabel("Input Size (N)")
plt.ylabel("Time (seconds)")
plt.title("All Algorithms Comparison (Worst Case)")
plt.legend()
plt.grid()

plt.savefig("all_worst.png")
plt.show()