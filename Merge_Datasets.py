import pandas as pd

# --------------------------
# Read both CSV files
# --------------------------

ligands = pd.read_csv(r"C:\Users\anush\OneDrive\Desktop\Docking_project\Ligand_Dataset.csv")
ligands = ligands.drop_duplicates(subset = "CID", keep="first")


docking = pd.read_csv(r"C:\Users\anush\OneDrive\Desktop\Docking_project\Docking_Summary.csv")



# --------------------------
# Make CID datatype same
# --------------------------

ligands["CID"] = ligands["CID"].astype(str)
docking["CID"] = docking["CID"].astype(str)

print("Total ligand rows:", len(ligands))
print("Unique CID:", ligands["CID"].nunique())

duplicates = ligands[ligands.duplicated(subset = "CID", keep=False)]

# --------------------------
# Merge using CID
# --------------------------

merged = pd.merge(docking,ligands,on="CID",how="left")

# --------------------------
# Save
# --------------------------

merged.to_csv(r"C:\Users\anush\OneDrive\Desktop\Docking_project\ML_Dataset.csv",index=False)

print("Done!")
print("Rows :", len(merged))
print(merged.head())






