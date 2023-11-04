import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def vis(df_cleaned):
    
    sns.pairplot(df_cleaned)

    selected_data = df_cleaned.loc[:200, ['Gender', 'Income_Category']]
    x = selected_data['Gender']
    y = selected_data['Income_Category']

    # Define custom colors for each category
    colors = ['orange', 'purple']

    # Create a bar chart
    plt.figure(figsize=(10, 10))
    bars = plt.bar(x, y, color=colors)
    plt.xlabel('Gender')
    plt.ylabel('Income_Category')
    plt.title('Income_Category by Gender Category')

    # Create a legend
    category_names = ['Low Income', 'High Income']  # Replace with your category names
    legend_labels = [f'{category}: {color}' for category, color in zip(category_names, colors)]
    plt.legend(bars, legend_labels)

    # Save the visualization as vis.png
    plt.savefig('vis.png')

    # Display the chart (optional)
    plt.show()

    #sending the data to model.py

df_json = input()
df_cleaned = pd.read_json(df_json, orient="split")
vis(df_cleaned)


