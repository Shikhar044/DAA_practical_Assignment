# 🚀 Sorting Algorithms Benchmark (CS253 DAA Assignment)

A comprehensive experimental study of sorting algorithms implemented in C, analyzing their real-world performance across different input types and sizes.

### 📌 Description

This project focuses on comparing the theoretical complexity of sorting algorithms with their actual runtime performance.

It evaluates:

⏱ Execution Time
🔢 Number of Comparisons
📊 Performance across different input types

The analysis is supported by multiple experimental runs, data averaging, and graphical visualization.

# ✨ Features
🔹 Implementation of 9 sorting algorithms
🔹 Performance comparison using:
Execution Time
Number of Comparisons
🔹 Supports multiple input types:
Random (Average Case)
Sorted (Best Case)
Reverse Sorted (Worst Case)
🔹 Multiple runs for accurate results
🔹 Automated CSV data generation
🔹 Graph plotting using Python (Matplotlib)
🔹 Logarithmic scale visualization
🔹 QuickSort pivot strategy comparison
# 🧠 Algorithms Implemented
Selection Sort
Bubble Sort
Insertion Sort
Merge Sort
Quick Sort (First Pivot)
Quick Sort (Random Pivot)
Quick Sort (Median Pivot)
Heap Sort
Radix Sort
# ⚙️ Installation
1. Clone the repository
git clone <your-repo-link>
2. Navigate to project directory
cd CS253_DAA
3. Ensure the following are installed:
GCC (C Compiler)
Python 3
Required Python libraries:
pip install pandas matplotlib
# ▶️ Usage
### Step 1: Compile the C program
gcc main.c -o sort
### Step 2: Run the program
./sort

This generates:

results_run1.csv → results_run5.csv
### Step 3: Compute average results
python average.py

Output:

result_avg.csv
### Step 4: Generate graphs
python plot.py
# 📁 Project Structure
CS253_DAA/
│
├── main.c              # Sorting algorithm implementations
├── plot.py             # Graph generation
├── average.py          # Average calculation
│
├── results_run1.csv
├── results_run2.csv
├── results_run3.csv
├── results_run4.csv
├── results_run5.csv
│
├── result_avg.csv      # Final processed dataset
└── README.md
# 🧪 Experimental Setup
### 📥 Input Sizes
1000 → 10000
### 📂 Input Types
🔹 Random (Average Case)
🔹 Sorted (Best Case)
🔹 Reverse Sorted (Worst Case)
### 🔁 Methodology
Each experiment is executed multiple times
Results are averaged to reduce system noise
# 📊 Analysis & Graphs

Graphs generated include:

📈 Time vs Input Size
📉 Comparisons vs Input Size
⚡ QuickSort Pivot Comparison
🔗 Comparisons vs Time Correlation
# 🧠 Lessons Learned
⚠️ Practical performance may differ from theoretical complexity
📊 Input type significantly affects algorithm behavior
🎯 Pivot selection plays a crucial role in QuickSort
🔁 Averaging improves accuracy of results
📉 Log scale is necessary for meaningful visualization
# 👨‍💻 Authors
Shikhar (241CS153)
Ganesh Shinde (241CS125)
# 🎓 Acknowledgements
Instructor: Ms. Vani M
Course: CS253 – Design and Analysis of Algorithms
Institute: NITK Surathkal
# ❓ FAQ
### Q1: 
Why are some lines not visible in graphs?

### Answer:
Due to large variation in values, logarithmic scale is used, which compresses smaller values.

### Q2: 
Why is Radix Sort faster?

### Answer:
Radix Sort is a non-comparison-based algorithm with near linear complexity.

### Q3: 
Why are multiple runs performed?

### Answer:
To reduce system fluctuations and obtain more reliable average results.

# ⭐ Final Note

This project demonstrates a complete pipeline:

Implementation → Data Collection → Analysis → Visualization → Insight

💡 This project is not just an assignment — it's a strong foundation for understanding algorithm performance in real-world scenarios.
