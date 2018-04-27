#!/sgoinfre/goinfre/Perso/fleste-l/anaconda3/bin/python

import pandas as pd
import pickle

data = pd.read_csv('ftlr_data1.csv')
data['kmfs'] = (data['km'] - min(data['km'])) / (max(data['km']) - min(data['km']))
data['pricefs'] = (data['price'] - min(data['price'])) / (max(data['price']) - min(data['price']))

X = data['kmfs'].values
y = data['pricefs'].values

try:
	with open('theta_file', 'rb') as theta_bck:
		theta_pck = pickle.Unpickler(theta_bck)
		theta = theta_pck.load()
except:
	theta = [0., 0.]
	with open('theta_file', 'wb') as theta_bck:
		theta_pck = pickle.Pickler(theta_bck)
		theta_pck.dump(theta)
def predict(X, theta):
	return theta[0] + theta[1] * X

def main():
	km = -1
	while km < 0:
		km = input("Enter the car mileage (km) :\n")
		try:
			km = int(km)
		except ValueError:
			print("Nothing entered")
			km = -1
			continue
		if km < 0:
			print("Negative mileage")
	kmfs = (km - min(data['km'])) / (max(data['km']) - min(data['km']))
	resfs = theta[0] + (theta[1] * kmfs)
	if resfs == 0:
		print("The car price is 0 €")
	else:
		res = (resfs * (max(data['price']) - min(data['price']))) + min(data['price'])
		if res < 0:
			res = 0
		print("The car price is", int(res),"€")

if __name__ == "__main__":
	main()
