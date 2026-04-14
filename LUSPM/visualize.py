import matplotlib.pyplot as plt
import os

# Create graphs folder if not exists
os.makedirs("graphs", exist_ok=True)

algorithms = ['LUSPMb (Naive)', 'LUSPMe (Optimized)']

runtime = [1.886, 0.038]
candidates = [1048576, 782]
patterns = [411, 411]
memory = [26, 9]

# --- Runtime ---
plt.figure()
plt.bar(algorithms, runtime)
plt.title("Runtime Comparison")
plt.ylabel("Time (seconds)")
plt.savefig("graphs/runtime.png")
plt.close()

# --- Candidates ---
plt.figure()
plt.bar(algorithms, candidates)
plt.title("Candidate Count Comparison")
plt.ylabel("Number of Candidates")
plt.yscale('log')
plt.savefig("graphs/candidates.png")
plt.close()

# --- Memory ---
plt.figure()
plt.bar(algorithms, memory)
plt.title("Memory Usage Comparison")
plt.ylabel("Memory (MB)")
plt.savefig("graphs/memory.png")
plt.close()

print("Graphs saved in 'graphs/' folder ✅")