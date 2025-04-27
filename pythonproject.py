import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv(r"C:\Users\itspr\OneDrive\Desktop\Python Project\Mental_Health_Care_in_the_Last_4_Weeks (1).csv")

# Show initial data info
print("Initial Data Info:")
print(data.info())

# Drop duplicates
data = data.drop_duplicates()

# Drop rows only if 'Value' is missing
data = data.dropna(subset=['Value'])

# Check cleaned data info
print("\nCleaned Data Info:")
print(data.info())

#section 2
# Filter for medication data
med_data = data[data['Indicator'] == 'Took Prescription Medication for Mental Health, Last 4 Weeks']

# Filter for demographic data
demo_data = med_data[med_data['Group'].isin(['By Age', 'By Sex', 'By Race/Hispanic ethnicity'])]

# Create a simple bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Subgroup', y='Value', hue='Group', data=demo_data)

plt.title('Mental Health Medication Usage by Demographics (Aug 2020)')
plt.xlabel('Demographic Group')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Print the top 3 groups with highest medication usage
print("Groups with highest medication usage:")
print(demo_data.sort_values('Value', ascending=False)[['Group', 'Subgroup', 'Value']].head(3))
#section 3 

# Filter for medication data by state
state_data = data[(data['Indicator'] == 'Took Prescription Medication for Mental Health, Last 4 Weeks') & 
                 (data['Group'] == 'By State')]

# Get top and bottom 5 states
top_states = state_data.nlargest(5, 'Value')
bottom_states = state_data.nsmallest(5, 'Value')

# Create a simple bar chart
plt.figure(figsize=(10, 6))

# Plot top 5 states
plt.subplot(1, 2, 1)
plt.bar(top_states['State'], top_states['Value'], color='darkblue')
plt.title('Top 5 States - Medication Usage')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Percentage (%)')

# Plot bottom 5 states
plt.subplot(1, 2, 2)
plt.bar(bottom_states['State'], bottom_states['Value'], color='lightblue')
plt.title('Bottom 5 States - Medication Usage')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Percentage (%)')

plt.tight_layout()
plt.show()

# Print summary statistics
print(f"National average: {state_data['Value'].mean():.1f}%")
print(f"Highest state: {top_states.iloc[0]['State']} ({top_states.iloc[0]['Value']:.1f}%)")
print(f"Lowest state: {bottom_states.iloc[0]['State']} ({bottom_states.iloc[0]['Value']:.1f}%)")


#section 4

# Create boxplot for 'Value' column
plt.boxplot(data['Value'].dropna())
plt.title('Boxplot of Value')
plt.ylabel('Percentage')
plt.grid(True)
plt.show()
# Section 5 
print("\n📊 Descriptive Analysis:")
print("\nGrouped Mean Values by Indicator and Subgroup:")
summary = data.groupby(['Indicator', 'Subgroup'])['Value'].mean()
print(summary)
