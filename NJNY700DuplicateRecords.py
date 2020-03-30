import pandas as pd

df = pd.read_csv("/Users/aakarsh.rajagopalan/Personal documents/Python projects/NJNY700DuplicateRecords/NJNY700DuplicateRecords.csv")
ind_c1 = []
ind_c2 = []

for i in range(len(df)):
    if df["C1"][i:i+1].to_list()[0] == 'NJ' or df["C1"][i:i+1].to_list()[0] == 'NY':
        ind_c1.append(1)
    else:
        ind_c1.append(0)

df["ind_c1"]=ind_c1

print(df[df["ind_c1"] != 1])

