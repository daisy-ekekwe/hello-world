import numpy as np
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenue = [145, 760, 861, 917, 805, 810, 114, 976, 103, 143, 107, 154]
expenses = [120, 569, 123, 120, 865, 840, 328, 582, 697, 166, 100, 380]
np_revenue = np.array(revenue)
np_expenses = np.array(expenses)
np_months = np.array(months)
np_profit = np_revenue - np_expenses
profit = np_profit.tolist()
keys = months
values = profit
Fin_status = dict(zip(keys, values))
print(Fin_status)
print(profit);
