import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv(r"C:\Users\dell\Downloads\E-commerce purchasing behavior analysis.csv") 
df['Gender'] = df['Gender'].str.title() 
gender_counts = df['Gender'].value_counts() 
plt.figure(figsize=(6,4)) 
ax = gender_counts.plot(kind='bar', color='green') 
plt.title('Number of Customers by Gender') 
plt.xlabel('Gender') 
plt.ylabel('Number of Customers') 
plt.show() 
