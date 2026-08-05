import os
import subprocess
from natsort import natsorted


# Folder containing the SDF files
input_folder = r"C:\Users\anush\OneDrive\Desktop\Docking_project\Ligands_sdf"

# Folder where pdbqt files will be saved
output_folder = r"C:\Users\anush\OneDrive\Desktop\Docking_project\Ligands_pdbqt"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

#Loop through all sdf files
files = natsorted(os.listdir(input_folder))
for file in files:
    if file.endswith(".sdf"):
        input_file_path = os.path.join(input_folder, file)
        output_file_name = os.path.splitext(file)[0] + ".pdbqt"
        output_file_path = os.path.join(output_folder, output_file_name)

        # Command to convert SDF to PDBQT using Open Babel
        command = f' obabel "{input_file_path}" -O "{output_file_path}" -h'
        
        # Execute the command
        subprocess.run(command, shell=True, check=True )

        print(f"Converted {file} to {output_file_name}")
print("All SDF files have been converted successfully to PDBQT format.")



