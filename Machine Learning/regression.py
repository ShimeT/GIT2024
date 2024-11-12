import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_splitpip install numpy
#Import excel data
boston=pd.read_excel("Boston_Dataset.xlsx",index_col=[0])
print(boston.head)