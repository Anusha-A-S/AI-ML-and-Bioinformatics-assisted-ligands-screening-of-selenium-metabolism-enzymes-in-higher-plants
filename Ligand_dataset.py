# Import Libraries

import os
import re
import pandas as pd
import pubchempy as pcp
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Lipinski
from rdkit.Chem import rdMolDescriptors
from rdkit.Chem import Crippen
from natsort import natsorted

# SDF reader

folder = r"C:\Users\anush\OneDrive\Desktop\Docking_project\Ligands_sdf"
data = []
files = natsorted(os.listdir(folder),
key=lambda x: int(x.split()[0]))
for file in files:
    if file.endswith(".sdf"):
        file_path = os.path.join(folder, file)
        print (f"Processing:{file}")
        # ======================================
        #Extracting CID from the file name
        # ======================================
        match = re.search(r'CID_(\d+)', file)
        if match:
            cid = int (match.group(1))
        else:
            cid = ""

        supplier = Chem.SDMolSupplier(file_path)
        mol = supplier[0]
        if mol is None:
            print ('cannot read molecule')
            
            
        # =======================================
        # SMILES
        # =======================================
        smiles = Chem.MolToSmiles(mol)


        # ======================================
        # Molecular Descriptors
        # ======================================
        molecular_weight = round(Descriptors.MolWt(mol), 2)
        logP = round(Crippen.MolLogP(mol), 2)
        tpsa = round(rdMolDescriptors.CalcTPSA(mol), 2)
        hba = Lipinski.NumHAcceptors(mol)
        hbd = Lipinski.NumHDonors(mol)
        rotatable_bonds = Lipinski.NumRotatableBonds(mol)
        aromatic_rings = rdMolDescriptors.CalcNumAromaticRings(mol)
        heavy_atoms = mol.GetNumHeavyAtoms()


        # ==========================================
        # Getting ligand name from PubChem using CID
        # ==========================================
        try:
            compound = pcp.Compound.from_cid(cid)
            if compound.iupac_name:
                ligand_name = compound.iupac_name
            else:
                ligand_name = "Not available"

        except:
            ligand_name = "Not Found"

        # =========================================
        # Save data
        # =========================================
        data.append([ligand_name, cid, smiles, molecular_weight, logP, tpsa, hba, hbd, rotatable_bonds, aromatic_rings, heavy_atoms])

# =========================================
# Create DataFrame
# =========================================
df = pd.DataFrame(data, columns=['Ligand Name', 'CID', 'SMILES', 'Molecular Weight', 'LogP', 'TPSA', 'HBA', 'HBD', 'Rotatable Bonds', 'Aromatic Rings', 'Heavy Atoms'])

# ========================================
# Save CSV file
# ========================================
df.to_csv('Ligand_Dataset.csv', index=False)
print()

print("Finished Successfully!")
print("Ligand_Dataset.csv Created Successfully!")









