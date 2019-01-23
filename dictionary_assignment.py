import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import OrderedDict
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenue = [145, 760, 861, 917, 805, 810, 114, 976, 103, 143, 107, 154]
expenses = [120, 569, 123, 120, 865, 840, 328, 582, 697, 166, 100, 380]
profit = np.array(revenue) - np.array(expenses)
Fin_status = OrderedDict(zip(months, profit))
print(Fin_status);
