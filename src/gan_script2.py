import mnist_loader_alt
import network
import graphical_output
import csv
import numpy as np
import gzip
import cPickle
import re

def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

def classify_digit(biases, weights, a):
    count = 0
    for b, w in zip(biases, weights):
        if count <3:
            a = sigmoid(np.dot(w, a)+b)
        count +=1
    return a

training_data, validation_data, test_data = mnist_loader_alt.load_data_wrapper()

net = network.Network([784, 97, 37, 5, 37, 97, 784])
#net.SGD(training_data, 50, 50, 3.0)
net.SGD(training_data, 1, 1, 3.0)

with open('document.csv', 'w') as csvfile:
    digitwriter = csv.writer(csvfile, delimiter = ',')
    digitwriter.writerows(net.biases)
    digitwriter.writerows(net.weights)

#print "Biases"
#print len(net.biases)
#print len(net.biases[0])
#print len(net.biases[1])
#print len(net.biases[0][0])

#print "Weights"
#print len(net.weights)
#print len(net.weights[0])
#print len(net.weights[1])
#print len(net.weights[0][0])

new_parameters = []

with open('document.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    #row_count = sum(1 for row in reader)
    #print row_count
    for row in reader:
        new_parameters.append([float(i.strip("[]")) for i in row])

biases = zip(new_parameters[0], new_parameters[1], new_parameters[2], new_parameters[3], new_parameters[4], new_parameters[5])
weights = zip(new_parameters[6], new_parameters[7], new_parameters[8], new_parameters[9], new_parameters[10], new_parameters[11])

#for number in validation_data:
#    temp = np.asarray(number[0])
#    new_validation_data.append((number, classify_digit(net.biases, net.weights, temp)))
#b = np.asarray(new_validation_data)
#np.savetxt("document.csv", b, delimiter=",")

#digit = net.feedforward(test_data[0][0])

#win = graphical_output.draw_new_number(test_data[0][0], 10)

#for i in range(10):
#    graphical_output.update_number(digit, 10, win)
#    digit = net.feedforward(test_data[i+10][0])
#    win.getMouse()
#    graphical_output.draw_new_number(test_data[i+10][0], 10)

print classify_digit(net.biases, net.weights, training_data[0][0])
print classify_digit(biases, weights, training_data[0][0])

