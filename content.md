In this example, we will run a piece of code 1000 times and examine the statistics of the time taken for each run. You don't need to worry about the details of the code itself.

This example uses Python, but you don't need to understand the Python code in order to follow the concepts being demonstrated.

Run the code cell below. It may take up to a couple of minutes to run.

```py-cell
from profiling_functions import profile_run

profile_run()
```

# Observations

You should be able to see from the output that the amount of time it takes to run the code varies significantly from run to run. This demonstrates the inherent variability in execution time, even for the same piece of code.