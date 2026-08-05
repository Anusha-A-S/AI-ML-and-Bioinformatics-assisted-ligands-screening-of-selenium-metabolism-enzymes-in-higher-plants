# AI-ML-and-Bioinformatics-assisted-ligands-screening-of-selenium-metabolism-enzymes-in-higher-plants

NAME: ANUSHA ASHOK SANNINGAPPANAVR
PROJECT TYPE: STATUP PROJECT INTERNSHIP
PROJECT ORGANIZATION: BVVS BASAWESHWAR ENGINEERING COLLEGE BAGALKOT
DEPARTMENT: BEC- BIOTECHNOLOGY
STARTUP CENTRE: POMLA NATURALS BEC STEP BAGLKOT
INTERNSHIP DURATION: 29 MAY 2026 - 28 JULY 2026
ACADEMIC GUIDE: Dr. JAYACHANDRA S. YARADODDI

## PROJECT OVERVIEW:
This project develops an AI & bioinformatics assisted virtual screening pipeline to identify ligands with enhance selenium uptake and assimilation by targeting the selenium metabolism enzymes ATP sulfurylase (APS1) and APS reductase (APR) in higher plants. This workflow integrates KEGG, UniProt/NCBI, Pfam/InterPro, BRENDA/CheMBL, PDB or AlphaFold/PubChem for pathway analysis and data collection. it further combines AutoDockToolS, Open Babel, P2Rank, AutoDock Vina, Python automation and Random Forest machine learning to predict ligand binding affinity, rank candidate compounds and identify key molecular descriptors influencing protein ligand interactions.

## OBJECTIVE:
• Selenium metabolism pathway analysis to identify the key enzymes involved in selenium uptake.
• Selection of target proteins (APS1 & APR) for virtual screening.
• Collection of ligands related to uptake response.
• Preparation of protein and ligand structures for molecular docking.
• Predict active binding pocket of target proteins using P2Rank.
• Automated virtual high throughput batch docking.
• Analyzation, extraction and ranking of ligands based on the binding score.
• Generate an integrated machine learning dataset.
• Random Forest regression model development and feature importance analysis.
• Model performance evaluation.
• AI screening tool development for new ligand prioritization.

## WORKFLOW/ PIPELINE:
1. Review research articles and understand the selenium metabolism
2. Pathway analysis by KEGG to approach all the metabolism enzymes
3. Download protein structure (APS1 & APR) from PDB OR AlphaFold
4. Protein preparation by using ADT with python script (PDB -> PDBQT)
5. Prediction active binding pocket by P2Rank with python script
6. Extraction of best pocket coordinated (.csv) by using python script
7. Collect ligands structure (SDF format) from PubChem
8. Ligands dataset descriptor (.csv)
9. Ligand Preparation using python automation with Open Babel (SDF ->PDBQT)
10. Automated batch docking of 120 ligands to both APS & APR(Python + AutoDock Vina)
11. Docking results extraction along with ranking (.csv), (Python script)
12. Create machine learning dataset(.csv) by using molecular descriptors of ligands and docking results (Python script)
13. Create machine learning dataset(.csv) by using molecular descriptors of ligands and docking results (Python script)
14. Random Forest machine learning model training
15. Model performance evaluation (MAE, MSE and R² metrics)
16. Feature importance analysis of molecular descriptor (Python script)
17. Development of AI screening tool
18. Prediction and prioritization of new ligands binding affinity for future experimental validation before the docking

## DATABASES USED:
KEGG
UniPort
NCBI 
Pfam
BRENDA
ChEMBL
Protein Data Base (PDB)
AlphaFold Protein Structure Database
PubChem

## SOFWARES AND TOOLS USED:
AutoDockTools (ADT)
Open Babel
P2Rank
AutoDock Vina
Python
Visual Studio Code (VS Code)

## PYTHON LIBRARIES AND MODULES USED:
Pandas
NumPy
Matplotlib
Scikit-learn
Joblib
natsort
RDKit
PubChemPy
os
re
subprocessor

## MACHINE LEARNING:
Random Forest Regression
feature importance
MAE, MSE and R² evaluation metrics 

## RESULTS:
Found best ligand by virtual python batch docking by using AutoDock Vina.
Developed integrated machine learning dataset.
Trained Rand Forest Regression model to predict ligand binding affinity.
Achieved high predictive performance with:
• Mean absolute error (MAE) = 0.288
• Mean squared error (MSE) = 0.1106
• Coefficient of Determination (R²) = 0.961
Identified the most influential molecular descriptors using feature importance analysis.
Developed an AI-assisted screening tool for predicting the binding affinity of new ligands before molecular docking.

## OUTPUT FILES:
[Docking_Summary.csv](https://github.com/user-attachments/files/30758441/Docking_Summary.csv)
[ML_Dataset.csv](https://github.com/user-attachments/files/30758570/ML_Dataset.csv)
[RandomForest_FeatureImportance.py](https://github.com/user-attachments/files/30760857/RandomForest_FeatureImportance.py)
RandomForest_Model.pkl – Trained Random Forest model for binding affinity prediction
[Feature_Importance.csv](https://github.com/user-attachments/files/30760893/Feature_Importance.csv)
<img width="2400" height="1500" alt="Image" src="https://github.com/user-attachments/assets/b9d3884d-c79f-438d-9bc7-389dcba501aa" />


















