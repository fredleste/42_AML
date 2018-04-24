#!/sgoinfre/goinfre/Perso/fleste-l/anaconda3/bin/python

import pandas as pd

data = pd.read_csv('ftlr_data1.csv')

data['kmfs'] = (data['km'] - min(data['km'])) / (max(data['km']) - min(data['km']))
data['pricefs'] = (data['price'] - min(data['price'])) / (max(data['price']) - min(data['price']))

X = data['kmfs'].values
y = data['pricefs'].values

def predict(X, theta):
    return theta[0] + theta[1] * X

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

theta = [0.93931892944579276, -1.0035757423865808]
kmfs = (km - min(data['km'])) / (max(data['km']) - min(data['km']))
resfs = theta[0] + (theta[1] * kmfs)
if resfs == 0:
	print("The car price is 0 euro")
else:
	res = (resfs * (max(data['price']) - min(data['price']))) + min(data['price'])
	print("The car price is", int(res),"euros")
