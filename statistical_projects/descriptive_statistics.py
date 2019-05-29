#importing libraries
import pandas as pd
from pandas import DataFrame
from sklearn.datasets import load_iris

iris_obj = load_iris()
print(iris_obj.data)

print(iris_obj.feature_names)

print(iris_obj.target)

