import pandas as pd
import matplotlib.pyplot as plt

# ---------- LOAD DATA ----------
data = pd.read_csv("result_avg.csv")

# 🔥 CLEAN DATA (VERY IMPORTANT)
data['Algorithm'] = data['Algorithm'].str.strip()
data['InputType'] = data['InputType'].str.strip()

print("Algorithms:", data['Algorithm'].unique())
print("InputTypes:", data['InputType'].unique())


# ---------------- QUICK SORT ----------------
qs_algos = ['QuickFirst','QuickRandom','QuickMedian']

cases = {
    'average': 'Random',
    'best': 'Sorted',
    'worst': 'Reverse'
}

# -------- QUICK SORT GRAPHS --------
for case_name, case_type in cases.items():

    qs = data[
        (data['Algorithm'].isin(qs_algos)) &
        (data['InputType'] == case_type)
    ]

    # ---- Time vs N ----
    plt.figure()
    for algo in qs_algos:
        subset = qs[qs['Algorithm'] == algo]

        if subset.empty:
            print(f"Missing QuickSort Time: {algo} {case_name}")
            continue

        subset = subset.sort_values(by='N')
        plt.plot(subset['N'], subset['Time'], marker='o', label=algo)

    plt.yscale('log')   # 🔥 FIX SCALE
    plt.xlabel("Input Size (N)")
    plt.ylabel("Time (seconds)")
    plt.title(f"QuickSort Time vs N ({case_name.capitalize()} Case)")
    plt.legend()
    plt.grid()
    plt.savefig(f"quick_time_{case_name}.png")
    plt.close()


    # ---- Comparisons vs N ----
    plt.figure()
    for algo in qs_algos:
        subset = qs[qs['Algorithm'] == algo]

        if subset.empty:
            print(f"Missing QuickSort Comp: {algo} {case_name}")
            continue

        subset = subset.sort_values(by='N')
        plt.plot(subset['N'], subset['Comparisons'], marker='o', label=algo)

    plt.yscale('log')   # 🔥 FIX SCALE
    plt.xlabel("Input Size (N)")
    plt.ylabel("Comparisons")
    plt.title(f"QuickSort Comparisons vs N ({case_name.capitalize()} Case)")
    plt.legend()
    plt.grid()
    plt.savefig(f"quick_comp_{case_name}.png")
    plt.close()


# ---------------- ALL ALGORITHMS ----------------
algorithms = ['Selection','Bubble','Insertion','Merge','Heap','Radix','QuickMedian']

for case_name, case_type in cases.items():

    subset_data = data[data['InputType'] == case_type]

    # ---- Time vs N ----
    plt.figure()
    for algo in algorithms:
        subset = subset_data[subset_data['Algorithm'] == algo]

        if subset.empty:
            print(f"Missing Time: {algo} {case_name}")
            continue

        subset = subset.sort_values(by='N')
        plt.plot(subset['N'], subset['Time'], marker='o', label=algo)

    plt.yscale('log')   # 🔥 FIX SCALE
    plt.xlabel("Input Size (N)")
    plt.ylabel("Time (seconds)")
    plt.title(f"All Algorithms Time vs N ({case_name.capitalize()} Case)")
    plt.legend()
    plt.grid()
    plt.savefig(f"all_time_{case_name}.png")
    plt.close()


    # ---- Comparisons vs N ----
    plt.figure()
    for algo in algorithms:
        subset = subset_data[subset_data['Algorithm'] == algo]

        if subset.empty:
            print(f"Missing Comp: {algo} {case_name}")
            continue

        subset = subset.sort_values(by='N')
        plt.plot(subset['N'], subset['Comparisons'], marker='o', label=algo)

    plt.yscale('log')   # 🔥 FIX SCALE
    plt.xlabel("Input Size (N)")
    plt.ylabel("Comparisons")
    plt.title(f"All Algorithms Comparisons vs N ({case_name.capitalize()} Case)")
    plt.legend()
    plt.grid()
    plt.savefig(f"all_comp_{case_name}.png")
    plt.close()