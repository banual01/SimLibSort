import pandas as pd
import os

print(os.listdir("../Original_Excel_Files"))
for file in os.listdir("../Original_Excel_Files"):
    print(file)
    df = pd.read_excel("../Original_Excel_Files/"+file)
    print(df.head())

