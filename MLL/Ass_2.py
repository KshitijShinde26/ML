
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load Dataset
df = pd.read_csv("Salary_dataset.csv")

# Select X and Y
X = df[['YearsExperience']]
Y = df['Salary']

# Split Data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train Model
model = LinearRegression()
model.fit(X_train, Y_train)

# Predict
Y_pred = model.predict(X_test)



# Graph
plt.scatter(X, Y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression")
plt.legend()
plt.show()
mse = mean_squared_error(Y_test, Y_pred)
print("\nEvaluation Metrics")
print("MAE:", mean_absolute_error(Y_test, Y_pred))
print("MSE:", mse)
print("R2 Score:", r2_score(Y_test, Y_pred))