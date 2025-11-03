# ==================================================
#             Data analysis of population
#          NCFE Level 2 certificate homework
#                 Michael Everett
# ==================================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

worldPop = pd.read_csv("worldPop.csv", header = 0, sep = ",")
worldPop.dropna(axis = 1, inplace = True) # remove any columns with a NaN

xData = worldPop["Country"]
yData = worldPop["Population"]
totalPop = np.sum(yData)
#print(totalPop)

pieExplode = []
popArray = []

for x in xData :
    capitalise = x.capitalize() # capitalises all the country names
    popArray.append(capitalise)
    pieExplode.append(0.05)

print(popArray)

def popInt(pop) :
    x = int(np.round(pop/100000000.*totalPop)) # divide by 100 million - divide by a million to get a percentage, then another 100 to convert
    return x

print(xData, yData)
print(worldPop)

plt.title(f"Fig 1.0: Highest global populations by country\nin millions")
plt.pie(yData, labels = popArray, autopct = popInt, explode = pieExplode) # the popInt function iterates through all the labelled countries
plt.show()