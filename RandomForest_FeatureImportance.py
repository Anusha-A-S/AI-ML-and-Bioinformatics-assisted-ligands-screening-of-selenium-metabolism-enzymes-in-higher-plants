import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

import joblib

dataset = r"C:\Users\anush\OneDrive\Desktop\Docking_project\ML_Dataset.csv"
df = pd.read_csv(dataset)
print(df.head())
print("\nRows :",len(df))

X = df[["Molecular Weight", "LogP", "TPSA", "HBA","HBD", "Rotatable Bonds", "Aromatic Rings", "Heavy Atoms"]]
y = df["Best_Affinity"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 42)

model = RandomForestRegressor(n_estimators = 200, random_state = 42)
model.fit(X_train, y_train)
print("Model Training Completed")

joblib.dump(model, r"C:\Users\anush\OneDrive\Desktop\Docking_project\RandomForest_Model.pkl")
print("Model Saved")

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print()
print("MAE:", mae)
print("MSE:", mse)
print("R2:", r2)

importance = model.feature_importances_
importance_df = pd.DataFrame({"Feature":X.columns, "Importance":importance})
importance_df = importance_df.sort_values(by="Importance", ascending = False)
print(importance_df)
importance_df.to_csv(r"C:\Users\anush\OneDrive\Desktop\Docking_project\Feature_Importance.csv",index=False)

plt.figure(figsize = (8,5))
plt.bar(importance_df["Feature"],importance_df["Importance"])
plt.xticks(rotation = 45)
plt.ylabel("Importance")
plt.title("Feature importance")
plt.tight_layout()
plt.savefig(r"C:\Users\anush\OneDrive\Desktop\Docking_project\Feature_Importance.png", dpi = 300)
plt.show()








