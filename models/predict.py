import pandas as pd
from train import LinearRegression

def predict_price(theta0, theta1, x):
	return theta0 + (theta1 * x)

def predict():
	try:
		mileage = input("Enter the mileage: ")
		mileage = float(mileage)
		t = pd.read_csv('../csv/theta.csv')
		p = pd.read_csv('../csv/data.csv')

		km = [p.km.min(), p.km.max()]
		pm = [p.price.min(), p.price.max()]

		theta0 = t.theta0[0]
		theta1 = t.theta1[0]

		y_pred = theta0 + theta1 * mileage
		m_normalized = (mileage - km[0]) / (km[1] - km[0])
		pp_normalized = predict_price(theta0, theta1, m_normalized)
		pp = pp_normalized * (pm[1] - pm[0]) + pm[0]
		print(f"value is {pp}")
	except Exception as e:
		print(f"Error: {e}")

if __name__ == '__main__':
	predict()