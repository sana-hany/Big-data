import pandas as pd
import sys
import subprocess
import json

#filename = sys.argv[1]
df = pd.read_csv("customers.csv")
df_json = df.to_json(orient="split")


try:
    subprocess.run(["python3", "dpre.py"], input=df_json, text=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")