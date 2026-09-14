In this example, we will compare two different profiling runs, one of a short run and one of a longer run. Both runs perform the same core operation, but the long run repeats it many more times. We will observe how the run length affects the variability of the profiling results.

In each case, the statistics of the runs, along with a histogram of run times will be produced.

This example uses Python, but you don't need to understand the Python code in order to follow the concepts being demonstrated. You also don't need to worry about what the core operation being performed is.

# Short Run

```py-cell
from profiling_functions import profile_runs, short_run

profile_runs(short_run)
```

# Long Run

```py-cell
from profiling_functions import profile_runs, long_run

profile_runs(long_run)
```

# Even Longer Run

This run may take up to a couple of minutes.

```py-cell
from profiling_functions import profile_runs, even_longer_run

profile_runs(even_longer_run)
```

# Comparison

What you should have seen in the above runs is that as the run length increased, the relative standard deviation of the execution time decreased. This demonstrates that longer runs tend to provide more stable and reliable profiling results, reducing the impact of random fluctuations in individual run times.