import mnist_loader_with_unknowns
from graphics import *
import graphical_output
import cPickle
import gzip
import random
import network
import numpy as np
from network import sigmoid
from network import sigmoid_prime
from graphical_output import update_number

def main():
	training_data, validation_data, test_data = mnist_loader_with_unknowns.load_data_wrapper()
	size = 10
	print len(training_data)
	hidden_neurons = 30 #input("Enter the number of hidden neurons:")
	net = network.Network([784, hidden_neurons, 11])
	num_of_epochs = 20 #input("Enter the number of epochs:")
	min_batch_size = 50 #input("Enter the mini-batch size:")
	net.SGD(training_data, num_of_epochs, min_batch_size, 3.0)#, test_data=test_data)
	win = GraphWin('Number', size*28, size*28) # give title and dimensions
	entry = input("Which number to display?")
	while entry <> 0:
		graphical_output.update_number(training_data[entry][0],size,win)
		counter = 0
		answer = 0
		#print("counter", counter)
		for numeral in training_data[entry][1]:
			#print ("numeral", numeral)
			if numeral == 1:
				answer = counter
			counter +=1
			#print("answer", answer)
			#print("counter", counter)
		if answer == 10:
			answer = "unknown"
		#print("answer", answer)
		print ("This is supposed to be a ", answer)
		activations = []
		for layer1 in range(hidden_neurons):
			#activation = sigmoid(np.dot(net.weights[0][layer1], np.transpose(new_number)))
			activation = sigmoid(np.dot(net.weights[0][layer1], training_data[entry][0]))
			activations.append(activation)
		outputs=[]
		for output_neuron in range(11):
			output = sigmoid(np.dot(net.weights[1][output_neuron], activations))
			outputs.append(output)
		#print outputs
		counter = 0
		for digit in outputs:
			print(counter, " ", "|"*int(digit*100))
			counter +=1
		entry = input("Which number to display?")
		for item in win.items[:]:
			item.undraw()

main()