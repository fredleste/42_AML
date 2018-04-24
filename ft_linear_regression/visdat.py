#!/sgoinfre/goinfre/Perso/fleste-l/anaconda3/bin/python

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('ftlr_data1.csv')

plt.figure(figsize = (12, 8))
plt.scatter(data['km'], data['price'], marker = 'o')
plt.xlabel('km',fontsize='14', fontweight='bold')
plt.ylabel('price', fontsize='14', fontweight='bold')
plt.show()
