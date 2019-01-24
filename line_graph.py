import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import OrderedDict
months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV' 'DEC']
revenue = [145, 760, 861, 917, 805, 810, 114, 976, 103, 143, 107, 154]
expenses = [120, 569, 123, 120, 865, 840, 328, 582, 697, 166, 100, 380]
profit = np.array(revenue) - np.array(expenses)
Fin_status = OrderedDict(zip(months, profit))
pd_Fin_status = pd.Series(Fin_status)
pd_Fin_status.plot()
plt.title('Profit Per Month')
plt.xlabel('Months')
plt.ylabel('Profit')
plt.show()
