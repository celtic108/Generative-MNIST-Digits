"""convert_data_source_unknown.py
~~~~~~~~~~~~~~~~~~

*****NEVERMIND*****
The original set of test data only includes the integer value of the 
image label. It doesn't need to have an additional element added, that
is done by the mnist_loader program.


Modify the original MNIST training set to include an 11th element of
the label to indicate digits that are unknown. This could give different
results for the entries in the database that are not clear (examples 
given on neuralnetworksanddeeplearning.com. 

The main reason for making this change is to start appending the data
set with generated images from the gradient decent solver. This is to 
set up something of an adversarial network between the original network
and the solver.

Note that this program is memory intensive, and may not run on small
systems.

"""

from __future__ import print_function

#### Libraries

# Standard library
import cPickle
import gzip
import os.path
import random

# Third-party libraries
import numpy as np

print("Revising the MNIST training set")



f = gzip.open("../data/mnist.pkl.gz", 'rb')
training_data, validation_data, test_data = cPickle.load(f)
f.close()


revised_training_pairs = []
for x, y in zip(training_data[0], training_data[1]):
	revised_training_pairs.append(x, y)
	
	
revised_validation_pairs = []
for x, y in zip(validation_data[0], validation_data[1]):
	revised_validation_pairs.append(x, y)
	
	
revised_test_pairs = []
for x, y in zip(test_data[0], test_data[1]):
	revised_test_pairs.append(x, y)


revised_training_data = [list(d) for d in zip(*revised_training_pairs)]
revised_validation_data = [list(d) for d in zip(*revised_validation_pairs)]
revised_test_data = [list(d) for d in zip(*revised_test_pairs)]
print("Saving expanded data. This may take a few minutes.")
f = gzip.open("../data/revised-mnist.pkl.gz", "w")
cPickle.dump((revised_training_data, revised_validation_data, revised_test_data), f)
f.close()