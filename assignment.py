import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

data = load_wine()
df = pd.DataFrame(data.data,columns = data.feature_names)
df['class'] = data.target
print(df)

avg_value = df.groupby('class').mean()
print(avg_value)

