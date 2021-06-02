import pandas as pd
import os

combine = pd.DataFrame()
for file in os.listdir("../Original_Excel_Files"):
    df = pd.read_excel("../Original_Excel_Files/"+file)
    df = df[["LCC", "Yr.","Title"]]
    print(file)
    print(len(df.columns))
    print(df.columns)
    combine = combine.append(df)
combine.to_csv("../goalData/original.csv", index=False)
    

