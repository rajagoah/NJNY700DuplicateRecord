import pandas as pd

#reading the cdv file
df = pd.read_csv("/Users/aakarsh.rajagopalan/Personal documents/Python projects/NJNY700DuplicateRecords/NJNY700DuplicateRecords.csv")

#initializing a list. This list will be then used to assign values to a new indicator column in the above data frame
ind_c1 = []

#iterator to access each element
for i in range(len(df)):

    #validation to check if any items have the value of NJ or NY
    if df["C1"][i:i+1].to_list()[0] == 'NJ' or df["C1"][i:i+1].to_list()[0] == 'NY':

        #Assigning value to the list
        ind_c1.append(1)
    else:

        #Assigning value to the list
        ind_c1.append(0)

#assigning the values in the list to the new indicator column in the above data frame
df["ind_c1"]=ind_c1

#printing out only those records that have indicator value 1
print(df[df["ind_c1"] != 1])

