#!/sgoinfre/goinfre/Perso/fleste-l/anaconda3/bin/python
import pandas as pd
import pickle
import matplotlib.pyplot as plt

data = pd.read_csv('ftlr_data1.csv')
data['kmfs'] = (data['km'] - min(data['km'])) / (max(data['km']) - min(data['km']))
data['pricefs'] = (data['price'] - min(data['price'])) / (max(data['price']) - min(data['price']))

with open('theta_file', 'rb') as theta_bck:
	theta_pck = pickle.Unpickler(theta_bck)
	theta = theta_pck.load()

def visualize(theta):
    fig = plt.figure(figsize = (12, 8))
    ax = plt.axes()
    ax.set_xlim([15000,250000])
    ax.set_ylim([3100, 8500])
    ax.scatter(data['km'], data['price'])
    plt.xlabel('km',fontsize='14', fontweight='bold')
    plt.ylabel('price', fontsize='14', fontweight='bold')
    ax.set_title('linear regression', fontsize='16', fontweight='bold')
    xx = data['kmfs'].values
    line_x = data['km'].values
    res = theta[0] + theta[1] * xx
    line_y = (res * (max(data['price']) - min(data['price']))) + min(data['price'])
    ax.plot(line_x, line_y, color='orange')
    plt.show()

visualize(theta)
