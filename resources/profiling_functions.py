import time
import matplotlib.pyplot as plt
import numpy as np


def run_workload():
    total = 0
    for _ in range(1000):
        for i in range(100):
            total += i

    return total


def profile_run(number_of_runs=1000, warmup_runs=20):
    times = []

    # Warm-up runs are intentionally silent to avoid extra status noise.
    for _ in range(warmup_runs):
        run_workload()

    for _ in range(1, number_of_runs + 1):
        start_time = time.perf_counter()
        run_workload()
        end_time = time.perf_counter()
        times.append(end_time - start_time)

    times = np.array(times)

    mean_time = np.mean(times)
    sd_time = np.std(times, ddof=1)
    max_time = np.max(times)
    min_time = np.min(times)

    plt.hist(times, bins=10)
    plt.xlabel("Execution Time (seconds)")
    plt.ylabel("Frequency")
    plt.title("Runtime Distribution")

    print(f"  n={len(times)}")
    print(f"  mean={mean_time:.4f}s")
    print(f"  standard deviation={sd_time:.5f}s")
    print(f"  max={max_time:.4f}s")
    print(f"  min={min_time:.4f}s")


if __name__ == "__main__":
    profile_run()

