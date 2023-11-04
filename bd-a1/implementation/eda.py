import pandas as pd
import numpy as np
import subprocess

def eda(df_cleaned):
    # Perform data exploration and generate insights
    insights = []

    # Insight 1: Calculate the number of rows and columns
    insight1 = f"Number of rows: {len(df_cleaned)}\nNumber of columns: {len(df_cleaned.columns)}"
    insights.append(insight1)

    # Insight 2: Calculate the mean and standard deviation of a numerical column
    numeric_column = 'Age'  # Replace with an actual numerical column name
    mean_age = np.mean(df_cleaned[numeric_column])
    std_age = np.std(df_cleaned[numeric_column])
    insight2 = f"Mean {numeric_column}: {mean_age:.2f}\nStd Deviation {numeric_column}: {std_age:.2f}"
    insights.append(insight2)

    # Insight 3: Identify the unique categories in a categorical column
    categorical_column = 'Education_Level'  # Replace with an actual categorical column name
    unique_categories = df_cleaned[categorical_column].unique()
    insight3 = f"Unique categories in {categorical_column}: {', '.join(unique_categories)}"
    insights.append(insight3)

    # Save insights as text files
    for i, insight in enumerate(insights, 1):
        with open(f'eda-in-{i}.txt', 'w') as f:
            f.write(insight)

    # sending the cleaned data   
    df = df_cleaned.to_json(orient="split")
    try:
        subprocess.run(["python3", "model.py"], input=df, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

df_json = input()
df_cleaned = pd.read_json(df_json, orient="split")
eda(df_cleaned)
