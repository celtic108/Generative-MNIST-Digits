import numpy as np
import mnist_loader
import csv

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
with open('generative_data.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerows(training_data)