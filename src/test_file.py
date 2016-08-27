from network import sigmoid
from network import sigmoid_prime
import numpy as np
test = np.array([-6, -4, -2, 0, 2, 4, 6])
vsigmoid = np.vectorize(sigmoid)
vsigmoid_prime = np.vectorize(sigmoid_prime)

print vsigmoid(test)
print vsigmoid_prime(test)