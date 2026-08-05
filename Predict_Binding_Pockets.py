import os
import subprocess

protein_folder = r"C:\Users\anush\OneDrive\Desktop\Docking_project\Enzymes_pdb"
output_folder = r"C:\Users\anush\OneDrive\Desktop\Docking_project\P2Rank_Output"
p2rank_folder = r"C:\Users\anush\OneDrive\Desktop\p2rank_2.5\p2rank_2.5"
prank = os.path.join(p2rank_folder, "prank.bat")
os.makedirs(output_folder, exist_ok=True)


for file in os.listdir(protein_folder):
    if file.endswith(".pdb"):
        protein_path = os.path.join(protein_folder, file)
        protein_name = os.path.splitext(file)[0]
        protein_output = os.path.join(output_folder, protein_name)
        os.makedirs(protein_output, exist_ok=True)
        print(f"\nPredicting binding pockets for:{protein_name}")
        command = [prank,"predict","-f", protein_path,"-o",protein_output]
        subprocess.run(command)

print("\nAll proteins processed successfully!")