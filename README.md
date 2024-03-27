# Rice-Root-Cell-Type-Prediction-Tool

## Overview
Rice-Root-Cell-Type-Prediction-Tool is a machine learning based approach to predict cell type of cells in root of rice

Current version: 22 November 2023 v0.1
### Supported Species and reference genomes

Oryza Sativa: [Os-Nipponbare-Reference-IRGSP-1.0]

Rice-Root-Cell-Type-Prediction-Tool pipeline : 

![image](https://github.com/dongwei-2023/Rice-Root-Cell-Type-Prediction-Tool/blob/main/img/model.png)

Application of our model to new rice root data : 

![image](https://github.com/dongwei-2023/Rice-Root-Cell-Type-Prediction-Tool/blob/main/img/predict_new_cellType.png)

## System Requirements
### Hardware Requirements
A computer with the following specs:

RAM : 16 + GB

CPU : 8 + cores

### Software Requirements
This tool we developed and tested on linux.

Linux : CentOS 7.6 and Ubuntu 22.04.4 LTS

Python (v3.8 or more; Developed and tested version : Python 3.8.13)

Scanpy : 1.9.5

optuna : 3.4.0

sklearn : 1.0.2

catboost : 1.2.2


## Example : 
Input : Input of expression matrix, including "barcodes.tsv.gz"  "features.tsv.gz"  "matrix.mtx.gz" files.

Output ： The output is a text file of the cell's barcode and Predicted Label
``` Bash
python predict_cellType.py -i "./matrix" -o "./out" -m "./Rice-Root-Cell-Type-Prediction-Tool_Best_Model.pkl"
```
Questions and errors
If you have a question, error, bug, or problem, please use the [Github issue page](https://github.com/dongwei-2023/Rice-Root-Cell-Type-Prediction-Tool/issues).
