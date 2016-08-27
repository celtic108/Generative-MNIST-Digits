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
		entry = input("Which number to display?")
		for item in win.items[:]:
			item.undraw()

main()