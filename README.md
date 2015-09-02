# twodee
A small python module for theoretical functions to optimize server throughput 

```python
# import the twodee module
import twodee

# create a twodee graph object
gr = twodee.graph([0,1,2,3,4,5,6], [0,1,4,9,16,25,36])

# optimize with a skip value of 1.
print gr.optimize(1)
```
