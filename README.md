# 2-layer Perzeptron

The simplest form of [Perzeptrons](https://en.wikipedia.org/wiki/Perceptron) also called single-layer perceptron, implemented in python, for a programming assignment of course ***Technical Neuroal Network***.
 
# Using Instruction

Simply import function "BiLayerPerzeptron" from BiLayerPerzeptron.py

	$ python
	from BiLayerPerzeptron import BiLayerPerzeptron
	
Now you can use this function with the following definition:

	TNN = BiLayerPerzeptron(N, M, Weights, Patterns, LearningRate, RandomSeed, MaxSteps, ErrThreshold)

### N

Number of Inputs (Unsigned Integer).

### M 

Number of Outputs (Unsigned Integer).

### Weights(including BIAS): Initial weights

A list consist of M lists, each one contains N+1 real number which are weights of each input of an output neuron.
**Alternatively**, source direction of a .dat file in which you must put weights of each input of every output neuron followed by weights of next output neuron (lines with # consider as a comment).
**Alternatively**, '' or [] to initialize weights with a random value between -0.5 and 0.5.

### Patterns

A list of P patterns used to train the perzeptron in the form of tuples in which the first element is a list containing N inputs and the second one is a list containing M outputs.
**Alternatively**, source direction of  a .dat file in which for each training pattern you must put the inputs(without BIAS) followed by outputs followed by next patterns (lines with # consider as a comment).

### LearningRate

The learning rate used to control how much each weight can change.

### RandomSeed

A random seed used for random initializing and shuffling, to be able to reproduce results.

### MaxSteps

The maximum number of iterations in which the model can train.

### ErrThreshold

A threshold on error(sum of mean squared error of model for all patterns).

### TNN

A function which is a Two-Layer perzeptron neural network with calculated weights, with the following definition:

	Y = TNN(X)
	
**X**: a list of containing N values as input
**Y**: a list containing M values as output

BiLayerPerzeptron will also prints the calculated weights in the given order for argument *Weights*.

# Example:

	>>> OR = BiLayerPerzeptron(2, 1, [], [([0, 0], [0]), ([1, 0], [1]), ([0, 1], [1]), ([1, 1], [1])])
	Weights :
	[-0.08536651160045094, 0.11185216306896206, 0.3103302158747886]
	>>> OR([1, 1])
	[1]

*Please check "BiLayerPerzeptron-Test.py" for more examples.*

# Authors 

	Ali Mohammadi
	Rozhin Bayati


*Best Regards*