import os
import subprocess

input_folder = r"C:\Users\anush\OneDrive\Desktop\Docking_project\Enzymes_pdb"
output_folder = r"C:\Users\anush\OneDrive\Desktop\Docking_project\Enzymes_pdbqt"
os.makedirs(output_folder, exist_ok=True)


for file in os.listdir(input_folder):
    if file.endswith(".pdb"):
        input_file = os.path.join(input_folder, file)
        output_file = os.path.join(output_folder,os.path.splitext(file)[0]+ ".pdbqt")


        output_basename = os.path.splitext(output_file)[0]

        command = ["py","-m","meeko.cli.mk_prepare_receptor","--read_pdb",input_file,"-o",output_basename,"-p"]
        print(f"\nPreparing receptor: {file}")
        result = subprocess.run(command,capture_output=True,text=True)

        print(result.stdout)

        if result.stderr:
            print(result.stderr)

print("\nAll protein receptors have been prepared successfully!")





