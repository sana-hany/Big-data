import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
import subprocess

def kmean(df_cleaned):

    df_cleaned["Marital_Status"].unique()
    df_cleaned["Education_Level"].unique()

    #create new_df which has the selected features to be used in k mean classification
    new_df = df_cleaned[["Age", "Marital_Status", "Education_Level"]]

    #transform the categorical features to numerical 
    label_encoder = LabelEncoder()
    new_df["Education_Level"] = label_encoder.fit_transform(new_df["Education_Level"])
    new_df["Marital_Status"] = label_encoder.fit_transform(new_df["Marital_Status"])

    #applying k mean algorithm
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(new_df)

    #extract the labels of the clusters
    labels = kmeans.labels_

    new_df['cluster'] = labels
    rowsForClusters = new_df['cluster'].value_counts()

    file = open("k.txt", "w")
    i = 1
    for element in rowsForClusters:
        file.write("Number of records in cluster "+str(i)+" :"+str(element) + "\n")
        i+=1
    file.close()

    # sending the cleaned data   
    df = df_cleaned.to_json(orient="split")
    try:
        subprocess.run(["python3", "vis.py"], input=df, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

df_json = input()
df_cleaned = pd.read_json(df_json, orient="split")
kmean(df_cleaned)

