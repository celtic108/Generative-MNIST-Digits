import mnist_loader_alt
import graphical_output
import csv
import numpy as np
import re

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

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
    
def generate_digit(biases, weights, a):
    count = 0
    for b, w in zip(biases, weights):
        if count >2:
            a = sigmoid(np.dot(w, a)+b)
        count +=1
    return a


training_data, validation_data, test_data = mnist_loader_alt.load_data_wrapper()
    
new_parameters = []

with open('document.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        new_parameters.append(row)
        
biases = []
for i in range(6):
    placeholder=[]
    for entry in new_parameters[i]:
        placeholder.append(np.asarray(float(entry[1:-1])))
    placeholder2 = np.asarray(placeholder)
    placeholder2.shape = (len(placeholder2),1)
    biases.append(placeholder2)

weights = []
for i in range(6):
    placeholder=[]
    count = 0
    for entry in new_parameters[i+6]:
        placeholderinner = []
        for number in re.split('[||\s|\n|]',entry[1:-1]):
            if is_number(number):
                placeholderinner.append(float(number))
        placeholder.append(np.asarray(placeholderinner))
    weights.append(np.asarray(placeholder))
    
#win = graphical_output.draw_new_number(test_data[0][0], 10)
#print test_data[0][1]

classifier_list = []

for number in test_data:
    five_digit = np.rint(classify_digit(biases, weights, number[0]))
    classifier_list.append([number[1], five_digit])

pattern = np.random.rand(5,1)
win = graphical_output.draw_new_number(generate_digit(biases, weights, pattern), 10)
for i in range(60):
    pattern = np.random.rand(5,1)
    graphical_output.update_number(generate_digit(biases, weights, pattern), 10, win)
    
    
final_list=[]
    
#for a in range(2):
#    for b in range(2):
#        for c in range(2):
#            for d in range(2):
#                for e in range(2):
#                    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#                    pattern = np.asarray([[a], [b], [c], [d], [e]])
#                    for element in classifier_list:
#                        if np.array_equal(element[1], pattern):
#                            count[element[0]] +=1
#                    final_list.append([pattern, count])
                    #win = graphical_output.draw_new_number(generate_digit(biases, weights, pattern), 10)
print final_list