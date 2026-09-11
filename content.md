In this example, we will compare two different profiling runs, one of a short run and one of a longer run. Both runs perform the same core operation, but the long run repeats it many more times. We will observe how the run length affects the variability of the profiling results.

In each case, the statistics of the runs, along with a histogram of run times will be produced.

This example uses Python, but you don't need to understand the Python code in order to follow the concepts being demonstrated.

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