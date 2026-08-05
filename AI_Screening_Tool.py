import pandas as pd
import joblib

# -------------------------------------
# Load trained Random Forest model
# -------------------------------------

model = joblib.load(r"C:\Users\anush\OneDrive\Desktop\Docking_project\RandomForest_Model.pkl")

print("Random Forest Model Loaded Successfully!\n")

# -------------------------------------
# Read new ligand descriptors
# -------------------------------------

new_data = pd.read_csv(r"C:\Users\anush\OneDrive\Desktop\Docking_project\New_Ligands.csv")

print("Total New Ligands :", len(new_data))

# -------------------------------------
# Features
# -------------------------------------

X_new = new_data[["Molecular Weight","LogP","TPSA","HBA","HBD","Rotatable Bonds","Aromatic Rings","Heavy Atoms"]]

# -------------------------------------
# Predict Affinity
# -------------------------------------

new_data["Predicted_Affinity"] = model.predict(X_new)

# -------------------------------------
# Rank Ligands
# -------------------------------------

new_data = new_data.sort_values(by="Predicted_Affinity")

new_data["Rank"] = range(1, len(new_data)+1)

# -------------------------------------
# Priority
# -------------------------------------

priority = []

for rank in new_data["Rank"]:

    if rank <= 20:
        priority.append("High")

    elif rank <= 60:
        priority.append("Medium")

    else:
        priority.append("Low")

new_data["Priority"] = priority

# -------------------------------------
# Save
# -------------------------------------

new_data.to_csv(r"C:\Users\anush\OneDrive\Desktop\Docking_project\AI_Screening_Results.csv",index=False)

print("\nTop 20 Predicted Ligands\n")

print(new_data.head(20))

print("\nAI Screening Completed Successfully!")