#Note for installing matplot library run this command in terminal : pip install pandas 
import pandas as pd
data=pd.read_excel("dataf.xlsx")
print(data)
print(data['Column1'].sum())
print(data['Column2'].mean())
print(data['Column3'].max())
print(data['Column4'].min())