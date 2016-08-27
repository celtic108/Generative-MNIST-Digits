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

#def change_to_number(pass_tuple):
#	output_array = []
#	for x in pass_tuple:
#		count = 0
#		for y in x:
#			if y == 1:
#				answer = count
#			count += 1
#		output_array.append(answer)
#	return output_array

def prime(z):
	return (z*(z-1))
vprime = np.vectorize(prime)

def main():
	training_data, validation_data, test_data = mnist_loader_with_unknowns.load_data_wrapper()
	print len(training_data)
	#print len(validation_data)
	#print len(test_data)
	hidden_neurons = 100 #input("Enter the number of hidden neurons:")
	net = network.Network([784, hidden_neurons, 11])
	num_of_epochs = 20 #input("Enter the number of epochs:")
	min_batch_size = 50 #input("Enter the mini-batch size:")
	net.SGD(training_data, num_of_epochs, min_batch_size, 3.0)#, test_data=test_data)
	#graphical_output.draw_new_number(training_data[0][0], 10)
	#print training_data[0][1]
	
	size = 20
	win = GraphWin('Number', size*28, size*28) # give title and dimensions
	#print type(new_number)
	new_number=training_data[0][0]
	graphical_output.update_number(new_number,size,win)
	revised_training_pairs = []
	for new in range(10):
		new_number=training_data[new][0]
		target = new #random.randrange(0,10) #int(input("What number do you want to draw?:"))
		print "Target = ",target
		#nu2 = 20 #input("Input the learning rate:")
		#new_number = np.random.rand(784)
		for gradient in range(20):
			activations = []
			for layer1 in range(hidden_neurons):
				#activation = sigmoid(np.dot(net.weights[0][layer1], np.transpose(new_number)))
				activation = sigmoid(np.dot(net.weights[0][layer1], new_number))
				activations.append(activation)
			outputs=[]
			for output_neuron in range(11):
				output = sigmoid(np.dot(net.weights[1][output_neuron], activations))
				outputs.append(output)
			#print outputs
			cost = np.zeros(784)
			for edit_pixel in range(784):
				for output_neuron in range(11):
					level0weights = []
					for j in range(hidden_neurons):
						level0weights.append(net.weights[0][j][edit_pixel])
					#print level0weights
					#print vprime(activations)
					partial_derivative = np.multiply(level0weights, np.transpose(vprime(activations)))
					partial_output = prime(outputs[output_neuron])*np.dot(net.weights[1][output_neuron], np.transpose(partial_derivative))
					#print partial_output
					if output_neuron == target:
						cost[edit_pixel] = -2*(1-outputs[output_neuron])*partial_output
					else:
						cost[edit_pixel] = 2*outputs[output_neuron]*partial_output
			nu2 = 0.5/(np.amax(cost)-np.amin(cost))
			for edit_pixel in range(784):
				new_number[edit_pixel]=min(1,max(0,new_number[edit_pixel]-nu2*cost[edit_pixel]))
			for item in win.items[:]:
				item.undraw()
			update_number(new_number, size, win)
		revised_training_pairs.append((new_number, 10))
		for item in win.items[:]:
			item.undraw()
	#win = GraphWin('Number', size*28, size*28) # give title and dimensions
	#print len(revised_training_pairs[0][0])
	#print type(revised_training_pairs[0][0])
	#graphical_output.update_number(revised_training_pairs[0][0],size,win)
	#win.getMouse()
	#for x in range(10):
		#graphical_output.update_number(revised_training_pairs[x][0],size,win)
		#win.getMouse()
	#print outputs
	#e = np.zeros((11, 1))
	#e[10] = 1.0
	
	enter = 1 #input("Do you want to save this back to the MNIST data? (1=y/0=n):")
	if enter == 1:
		f = gzip.open('../data/revised-mnist.pkl.gz', 'rb')
		training_data, validation_data, test_data = cPickle.load(f)
		f.close()
		#print type(training_data[1])
		#print type(change_to_number(training_data[1]))
		#print len(change_to_number(training_data[1]))
		for x, y in zip(training_data[0], training_data[1]):
			revised_training_pairs.append((x, y))
		#revised_training_pairs.append((new_number, 10))	
		#revised_validation_pairs = []
		#for x, y in zip(validation_data[0], validation_data[1]):
		#	revised_validation_pairs.append((x, y))
		#revised_test_pairs = []
		#for x, y in zip(test_data[0], test_data[1]):
		#	revised_test_pairs.append((x, y))
		revised_training_data = [list(d) for d in zip(*revised_training_pairs)]
		#revised_validation_data = [list(d) for d in zip(*revised_validation_pairs)]
		#revised_test_data = [list(d) for d in zip(*revised_test_pairs)]
		#print len(revised_training_data)
		#print len(revised_validation_data)
		#print len(revised_test_data)
		print("Saving expanded data. This may take a few minutes.")
		f = gzip.open("../data/revised-mnist.pkl.gz", "w")
		cPickle.dump((revised_training_data, validation_data, test_data), f)
		f.close()

for looper in range(1):
	main()