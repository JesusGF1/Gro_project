# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:26:22 2021

@author: jesus
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

column_name = ["Time", "Cell_number", "cell_type"]
data2_7 = pd.read_csv("Data_division_2_7.csv", header= None)
data2_7.columns = column_name
sb.scatterplot(data = data2_7, x="Time", y="Cell_number", hue="cell_type")

data3 = pd.read_csv("Data_division_3.csv", header= None)
data3.columns = column_name
sb.scatterplot(data = data3, x="Time", y="Cell_number", hue="cell_type")

data3_3 = pd.read_csv("Data_division_3_3.csv", header= None)
data3_3.columns = column_name
sb.scatterplot(data = data3_3, x="Time", y="Cell_number", hue="cell_type")

data3_6 = pd.read_csv("Data_division_3_6.csv", header= None)
data3_6.columns = column_name
sb.scatterplot(data = data3_6, x="Time", y="Cell_number", hue="cell_type")

data4_2 = pd.read_csv("Data_division_4_2.csv", header= None)
data4_2.columns = column_name
sb.scatterplot(data = data4_2, x="Time", y="Cell_number", hue="cell_type")

data4_5 = pd.read_csv("Data_division_4_5.csv", header= None)
data4_5.columns = column_name
sb.scatterplot(data = data4_5, x="Time", y="Cell_number", hue="cell_type")

data35 = pd.read_csv("Data_division_4_2_35.csv", header= None)
data35.columns = column_name
sb.scatterplot(data = data35, x="Time", y="Cell_number", hue="cell_type")