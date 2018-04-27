#!/sgoinfre/goinfre/Perso/fleste-l/anaconda3/bin/python

import pandas as pd
import matplotlib.pyplot as plt
from linreg import predict
import pickle

data = pd.read_csv('ftlr_data1.csv')

data['kmfs'] = (data['km'] - min(data['km'])) / (max(data['km']) - min(data['km']))
data['pricefs'] = (data['price'] - min(data['price'])) / (max(data['price']) - min(data['price']))

X = data['kmfs'].values
y = data['pricefs'].values
J_history = []

def cost(X, y, theta):
    m = len(X)
    h = predict(X, theta)
    J = (1/(2 * m)) * (sum((h - y)**2))
    return J

def fit(X, y, theta, alpha, num_iters):
    m = len(X)
    for i in range(num_iters):
        h = predict(X, theta) - y
        theta[0] = theta[0] - (alpha / m) * sum(h)
        theta[1] = theta[1] - (alpha / m) * sum(h * X)
        J_history.append(cost(X,y,theta))
    return theta, J_history

def error_rate():
    plt.figure(figsize = (12, 8))
    ax = plt.axes()
    ax.plot(J_history)
    plt.xlabel('training iteration',fontsize='14', fontweight='bold')
    plt.ylabel('mean squared error', fontsize='14', fontweight='bold')
    ax.set_title('error rate', fontsize='16', fontweight='bold')
    plt.show()

def main():
    theta = [0., 0.]
    theta, J_history = fit(X, y, theta, 1, 200)
    error_rate()
    with open('theta_file', 'wb') as theta_bck:
    	theta_pck = pickle.Pickler(theta_bck)
    	theta_pck.dump(theta)

if __name__ == "__main__":
	main()
