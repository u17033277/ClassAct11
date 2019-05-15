import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

data = pd.read_csv('tips.csv')

data["tip_percentage"] = data["tip"] / data["total_bill"] * 100

print(data)

print("** Tips Less than 10%: **")
print(data[data["tip_percentage"] < 10])

print("** Correlation Coefficient between Total Bill and Size of table: **")
print(np.corrcoef(data["total_bill"],data["size"]))

sat = data[data.day == 'Sat']
satTotal = sat['total_bill'].sum()
fri = data[data.day == 'Fri']
friTotal = fri['total_bill'].sum()
sun = data[data.day == 'Sun']
sunTotal = sun['total_bill'].sum()


x_axis = ['Friday','Saturday','Sunday']
y_axis = [friTotal,satTotal,sunTotal]

ind = np.arange(len(x_axis))

plt.bar(ind, y_axis,color=['black', 'red', 'yellow'])
plt.ylabel('Total Bills (R)')
plt.xlabel('Day of The Weekend')
plt.title('Total Bills per Each Day of Weekend')
plt.xticks(ind, x_axis)
plt.show()