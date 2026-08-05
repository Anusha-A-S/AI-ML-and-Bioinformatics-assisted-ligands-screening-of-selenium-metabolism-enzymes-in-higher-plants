import os
import subprocess
import pandas as pd
from natsort import natsorted

vina = r"C:\Users\anush\OneDrive\Desktop\Docking_project\vina.exe"
protein_folder = r"C:\Users\anush\OneDrive\Desktop\Docking_project\Enzymes_pdbqt"
ligand_folder = r"C:\Users\anush\OneDrive\Desktop\Docking_project\Ligands_pdbqt"
csv_file = r"C:\Users\anush\OneDrive\Desktop\Docking_project\Best_Pockets.csv"
output_folder = r"C:\Users\anush\OneDrive\Desktop\Docking_project\Docking_Results"


size_x = 24
size_y = 24
size_z = 24

df = pd.read_csv(csv_file)
print(df)

# Loop through each protein
for index, row in df.iterrows():
    protein = row["Protein"]

    center_x = row["Center_X"]
    center_y = row["Center_Y"]
    center_z = row["Center_Z"]
    protein_file = os.path.join(protein_folder, protein + ".pdbqt")
    print("\n=================================================")
    print("protein:",protein)
    print("protein_file:",protein_file)
    print("Center:",center_x,center_y,center_z)
    print("Size:",size_x,size_y,size_z)
    print("===================================================")
    
    # Creating output folder
    protein_output = os.path.join(output_folder, protein)
    os.makedirs(protein_output, exist_ok=True)
    
    # Loop through all ligands
    for i, ligand_file in enumerate(natsorted(os.listdir(ligand_folder)), start=1):
        if ligand_file.endswith(".pdbqt"):
            ligand_path = os.path.join(ligand_folder, ligand_file)
            output_file = os.path.join(protein_output,ligand_file.replace(".pdbqt","_out.pdbqt"))
            log_file = os.path.join(protein_output,ligand_file.replace(".pdbqt","_log.txt"))
        
        
            print(f"\n[{i}] Docking : {ligand_file}")

            print("Ligand File:",ligand_path)
            print("Output File:",output_file)
            print("Log File:",log_file)
            
            
            # vina command to run AutoDock Vina
            command = [vina,"--receptor", protein_file, "--ligand", ligand_path, "--center_x",str(center_x), "--center_y",str(center_y), "--center_z",str(center_z), "--size_x",str(size_x), "--size_y",str(size_y), "--size_z",str(size_z), "--out", output_file]
            print("\nRunning Command:")
            print(" ".join(command))
            result = subprocess.run(command, capture_output=True, text=True)

            print(result.stdout)

            if result.stderr:
                print(result.stderr)





