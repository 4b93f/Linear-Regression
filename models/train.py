import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

def normalize(data):
    return (data - data.min()) / (data.max() - data.min())

def denormalize(data_normalized, data_min, data_max):
    return data_normalized * (data_max - data_min) + data_min

class LinearRegression():
	def __init__(self, p, learning_rate=0.1, num_iterations=1000):
		self.theta0 = 0
		self.theta1 = 0
		self.x = p.km
		self.y = p.price
		self.learning_rate = learning_rate
		self.num_iterations = num_iterations

	def gradient_descent(self):
		m = len(self.y)
		for _ in range(self.num_iterations):
			y_pred = self.theta0 + self.theta1 * self.x
			d_theta0 = (-2/m) * sum(self.y - y_pred)
			d_theta1 = (-2/m) * sum(self.x * (self.y - y_pred))
			self.theta0 = self.theta0 - self.learning_rate * d_theta0
			self.theta1 = self.theta1 - self.learning_rate * d_theta1

	def plotting(self, y_pred):
		plt.scatter(self.x, self.y)
		plt.plot(self.x, y_pred, color = "g")
		plt.xlabel('km')
		plt.ylabel('price')
		plt.show()

	def predict(self, x):
		return self.theta0 + (self.theta1 * x)
	
	def write_on_csv(self):
		with open('../csv/theta.csv', 'w') as f:
			f.write(f'theta0,theta1\n{self.theta0},{self.theta1}')

def linear(path):
	try:
		print(path)
		p = pd.read_csv(path)

		p.km = normalize(p.km)
		p.price = normalize(p.price)

		lr = LinearRegression(p)
		lr.gradient_descent()
		lr.write_on_csv()
		print("Training done")
	except Exception as e:
		print(e)

if __name__ == '__main__':
	path = sys.argv[1:2][0]
	linear(path)