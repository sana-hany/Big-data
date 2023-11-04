import pandas as pd
import subprocess
import json
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler

def clean_data(df):
    # Data Cleaning
    # Task 1: Handling Missing Values
    df.dropna(inplace=True)

    # Task 2: Removing Duplicates
    df.drop_duplicates(inplace=True)

    df_cleaned = df[(df['Education_Level'] != 'Unknown') & (df['Marital_Status'] != 'Unknown') & (df['Income_Category'] != 'Unknown')]
    # Data Transformation
    # Task 1: Feature Scaling (e.g., Min-Max Scaling)
    scaler = MinMaxScaler()
    df_cleaned[['Total_Amt_Chng_Q4_Q1', 'Total_Ct_Chng_Q4_Q1']] = scaler.fit_transform(df_cleaned[['Total_Amt_Chng_Q4_Q1', 'Total_Ct_Chng_Q4_Q1']])       

    # Task 2: One-Hot Encoding (if categorical variables exist)
    df_cleaned = pd.get_dummies(df_cleaned, columns=['Card_Category'])

    # Data Reduction
    # Task 1: Dimensionality Reduction (e.g., Principal Component Analysis - PCA)
    pca = PCA(n_components=2)
    df_pca = pca.fit_transform(df_cleaned[['Age', 'Months_on_book']])

    # Data Discretization
    # Task 1: Binning Numeric Data
    df_cleaned['BinnedFeature'] = pd.cut(df_cleaned['Avg_Open_To_Buy'], bins=3, labels=['Low', 'Medium', 'High'])
    
    # Task 2: Converting Continuous to Ordinal
    df_cleaned['OrdinalFeature'] = pd.qcut(df_cleaned['Age'], q=3, labels=['Low', 'Medium', 'High'])

    df_cleaned.to_csv('res_dpre.csv', index=False)

    df_cleaned = df_cleaned.to_json(orient="split")
    try:
        subprocess.run(["python3", "eda.py"], input=df_cleaned, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

df_json = input()
df = pd.read_json(df_json, orient="split")
clean_data(df)