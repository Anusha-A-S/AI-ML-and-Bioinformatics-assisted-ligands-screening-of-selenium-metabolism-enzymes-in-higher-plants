import os
import re
import pandas as pd

# -------------------------------
# Folder containing docking results
# -------------------------------
docking_folder = r"C:\Users\anush\OneDrive\Desktop\Docking_project\Docking_Results"

results = []

# -------------------------------
# Loop through each protein folder
# -------------------------------
for protein in os.listdir(docking_folder):

    protein_path = os.path.join(docking_folder, protein)

    if not os.path.isdir(protein_path):
        continue

    print(f"\nProcessing Protein: {protein}")

    # -------------------------------
    # Read every docking output file
    # -------------------------------
    for file in os.listdir(protein_path):

        if file.endswith("_out.pdbqt"):

            file_path = os.path.join(protein_path, file)

            print("Reading:", file)

            # -------------------------------
            # Extract CID from filename
            # -------------------------------
            cid_match = re.search(r'CID_(\d+)', file)

            if cid_match:
                cid = cid_match.group(1)
            else:
                cid = "Unknown"

            affinity = None

            # -------------------------------
            # Read docking output
            # -------------------------------
            with open(file_path, "r") as f:

                for line in f:

                    # Look for:
                    # REMARK VINA RESULT: -8.847 ...
                    if line.startswith("REMARK VINA RESULT:"):

                        affinity = float(line.split()[3])
                        break

            # -------------------------------
            # Store result
            # -------------------------------
            results.append({"Protein": protein,"Ligand_File": file,"CID": cid,"Best_Affinity": affinity})


# -------------------------------
# Convert to DataFrame
# -------------------------------
df = pd.DataFrame(results)
final_df = []

# Process one protein at a time
for protein in df["Protein"].unique():

    temp = df[df["Protein"] == protein].copy()

    # Sort only this protein by affinity
    temp = temp.sort_values(by="Best_Affinity", ascending=True)

    # Give ranking within this protein
    temp["Rank"] = range(1, len(temp)+1)

    final_df.append(temp)

# Merge back together
df = pd.concat(final_df)

# Arrange columns
df = df[["Protein","Rank","Ligand_File","CID","Best_Affinity"]]

# Save
output_csv = r"C:\Users\anush\OneDrive\Desktop\Docking_project\Docking_Summary.csv"

df.to_csv(output_csv,index=False)

