In this example, we will compare three different profiling runs of different lengths. All runs perform do similar things, but the longer runs have longer tasks to do. You don't need to worry about the tasks that are being completed.

In each case, the task will be completed 1000 times, and statistics of the time taken to run the task, along with a histogram of run times will be produced.

This example uses Python, but you don't need to understand the Python code in order to follow the concepts being demonstrated.

# Short Run

```py-cell
from profiling_functions import profile_runs, short_run

profile_runs(short_run)
```

# Medium

```py-cell
from profiling_functions import profile_runs, medium_run

profile_runs(medium_run)
```

# Long Run

This run may take up to a couple of minutes.

```py-cell
from profiling_functions import profile_runs, long_run

profile_runs(long_run)
```

# Comparison

What you should have seen in the above runs is that as the run length increased, the relative standard deviation of the execution time decreased. This demonstrates that longer runs tend to provide more stable and reliable profiling results, reducing the impact of random fluctuations in individual run times.