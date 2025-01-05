# Unemployment Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data_path_unemployment = 'Unemployment_Rate_upto_11_2020.csv'
unemployment_df = pd.read_csv(data_path_unemployment)

# Display the first few rows
print("\nUnemployment Dataset Preview:")
print(unemployment_df.head())

# Strip spaces from column names
unemployment_df.columns = unemployment_df.columns.str.strip()

# Preprocessing: Strip whitespace and parse dates
unemployment_df['Date'] = pd.to_datetime(unemployment_df['Date'].str.strip(), format='%d-%m-%Y')
unemployment_df = unemployment_df.dropna()

# Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(data=unemployment_df, x='Date', y='Estimated Unemployment Rate (%)', hue='Region')
plt.title('Unemployment Rate Over Time by Region')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.legend(title='Region')
plt.tight_layout()
plt.show()
