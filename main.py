import numpy as np                                # Load the numpy for more advanced mathamatics
import pandas as pd                               # Load the pandas for preprocessing data
import matplotlib.pyplot as plt                   # Load Matplotlib for graphying and plotting
import copy                                       # Load copy for deep copying data
from sklearn.linear_model import LinearRegression # Load scikit learn for the Linear Regression model
from sklearn.model_selection import train_test_split
import time

# Preprocess the data
df = pd.read_csv('~/Code/ClimateChangePredictionProject/data2.csv')    # Load the data.csv
df = df.drop(["J-D", "D-N", "DJF", "MAM", "JJA", "SON"], axis=1)
df = df.ffill()
df.set_index('Year', inplace=True)
df.head()

columns = df.columns
# Make a for loop so it will graph the present data from the data.csv
for i in columns:
    plt.figure()
    plt.plot(df[i])
    plt.title(f"{i}")
    # Un comment this line of code if you want all the graphs on your computer.: plt.savefig(f"chart_{i}.png")

model = LinearRegression()

for i in columns:
    month = i
    
    # Prepare the data for the chosen month
    X = df.index.values.reshape(-1, 1)  # Years as features
    y = df[month].values                # Temperatures for the selected month

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model.fit(X_train, y_train)
    
    future_years = np.arange(df.index[-1] + 1, df.index[-1] + 11).reshape(-1, 1)  # Next 10 years
    future_predictions = model.predict(future_years)

    # Plot actual data and future predictions
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df[month], label=f'Actual {month} Temperature', color='blue', marker='o', linestyle="-")
    plt.plot(future_years, future_predictions, label=f'Predicted {month} Temperature (Future)', color='red', linestyle='-')

    # Plot styling
    plt.title(f'Temperature Prediction for {month} (Including Future Predictions)')
    plt.xlabel('Year')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    #plt.show()

    # Un comment this line of code if you want all the graphs on your computer. : 
    plt.savefig(f"{i}.png")

    # Clear the plt for the next figure
    plt.clf()
    time.sleep(0.2)
    plt.close()
