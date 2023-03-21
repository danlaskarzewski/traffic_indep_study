import pandas as pd

for i in range (0, 14):
    df = pd.read_csv("ML_Results/ML_Results_Raw_10m_" + str(i) +".csv")
    d = df.groupby('Classifier', as_index=False).mean()
    d.to_csv("ML_Results/ML_Results_Avg_10m_" + str(i)+".csv")

df = pd.DataFrame()
for i in range (0, 14):
    df = pd.concat([df, pd.read_csv("ML_Results/ML_Results_Avg_10m_" + str(i) +".csv")])

d = df.groupby('Classifier', as_index=False).mean()
d.to_csv("ML_Results/ML_Results_Avg_10m.csv")