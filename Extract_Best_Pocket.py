import os
import pandas as pd

# ==========================
# Folder containing P2Rank results
# ==========================

p2rank_output = r"C:\Users\anush\OneDrive\Desktop\Docking_project\P2Rank_Output"

summary = []

# ==========================
# Search all protein folders
# ==========================

for protein in os.listdir(p2rank_output):

    protein_folder = os.path.join(p2rank_output, protein)

    if os.path.isdir(protein_folder):

        for file in os.listdir(protein_folder):

            if file.endswith("_predictions.csv"):

                csv_path = os.path.join(protein_folder, file)

                df = pd.read_csv(csv_path)
                df.columns = df.columns.str.strip()

                best = df.iloc[0]

                summary.append({

                    "Protein": protein,

                    "Rank": best["rank"],

                    "Score": best["score"],

                    "Probability": best["probability"],

                    "Center_X": best["center_x"],

                    "Center_Y": best["center_y"],

                    "Center_Z": best["center_z"],

                    "Residues": best["residue_ids"]})

summary_df = pd.DataFrame(summary)

summary_df.to_csv("Best_Pockets.csv", index=False)

print(summary_df)

print("\nBest_Pockets.csv created successfully!")




