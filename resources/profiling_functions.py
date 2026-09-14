import time
import matplotlib.pyplot as plt
import numpy as np


def core_operation():
    x = 0
    for i in range(100):
        x += i

    return x


def short_run():
    return core_operation()


def long_run():
    for _ in range(1000):
        core_operation()


def profile_runs(function_to_profile, number_of_runs=1000, warmup_runs=20):
    times = []

    # Warm-up run to reduce one-off startup effects in the measured sample.
    for _ in range(warmup_runs):
        function_to_profile()

    for _ in range(number_of_runs):
        start_time = time.perf_counter()
        function_to_profile()
        end_time = time.perf_counter()
        times.append(end_time - start_time)

    times = np.array(times)

    mean_time = np.mean(times)
    sd_time = np.std(times, ddof=1)
    rsd_percent = (sd_time / mean_time) * 100
    max_time = np.max(times)
    min_time = np.min(times)

    plt.hist(times, bins=100)
    plt.xlabel("Execution Time (seconds)")
    plt.ylabel("Frequency")
    plt.title(f"{function_to_profile.__name__}: runtime distribution")

    print(f"{function_to_profile.__name__}")
    print(f"  n={len(times)}")
    print(f"  mean={mean_time:.8f}s")
    print(f"  standard deviation={sd_time:.8f}s")
    print(f"  relative standard deviation={rsd_percent:.8f}%")
    print(f"  max={max_time:.8f}s")
    print(f"  min={min_time:.8f}s")
    plt.show()


if __name__ == "__main__":
    profile_runs(short_run)
    profile_runs(long_run)

