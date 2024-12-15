#Jessica Andryani F55123051

import random
from time import perf_counter as time
import matplotlib.pyplot as plt

random.seed(42)

def is_unique(arr):
    
    return len(arr) == len(set(arr))

def generate_worst_case(size):
    return [1] * size

def generate_average_case(size, max_value):
    
    return [random.randint(0, max_value) for _ in range(size)]

def experiment(size, max_value, iterations=1000):
    
    worst_times = []
    avg_times = []

    # Pengukuran Worst Case
    for _ in range(iterations):
        arr = generate_worst_case(size)
        start_time = time()
        is_unique(arr)
        end_time = time()
        worst_times.append(end_time - start_time)

    # Pengukuran Average Case
    for _ in range(iterations):
        arr = generate_average_case(size, max_value)
        start_time = time()
        is_unique(arr)
        end_time = time()
        avg_times.append(end_time - start_time)

  
    return max(worst_times), sum(avg_times) / len(avg_times)

# Ukuran array yang akan diuji
sizes = [100, 150, 200, 250, 300, 350, 400, 500]
max_value = 199  # Sesuai dengan NIM 250-51

results = []


for size in sizes:
    worst, avg = experiment(size, max_value)
    results.append((size, worst, avg))
    print(f"Size: {size}, Worst Case: {worst:.6f} s, Average Case: {avg:.6f} s")

# Menyimpan hasil ke file teks
with open("worst_avg.txt", "w") as f:
    f.write("Nama: Jessica Andryani\n")
    f.write("NIM: 051\n")
    f.write("Kelas: B - PAA\n\n")
    for size, worst, avg in results:
        f.write(f"Size: {size}, Worst case: {worst:.6f}, Average case: {avg:.6f}\n")

# Membuat plot
sizes, worst_cases, avg_cases = zip(*results)

plt.figure(figsize=(12, 6))
plt.plot(sizes, worst_cases, label="Worst Case", linestyle='-', marker='o')
plt.plot(sizes, avg_cases, label="Average Case", linestyle='-', marker='o')
plt.xlabel("Ukuran Array")
plt.ylabel("Waktu Eksekusi (s)")
plt.title("Worst Case vs Average Case")
plt.legend()
plt.grid()
plt.savefig("plot.pdf")
plt.show()
