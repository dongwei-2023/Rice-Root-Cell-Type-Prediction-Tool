# Rice-Root-Cell-Type-Prediction-Tool

## **Overview**
Rice-Root-Cell-Type-Prediction-Tool is a machine learning based approach to predict cell type of cells in root of rice.

Current version: 22 November 2023 v0.1

## **Methods**
To construct root single cell annotation (RSCA) model, we integrated our data and recently published two rice root scRNA-seq datasets using harmony with the default parameters. Each cell was annotated according to its cell type from the literature. The raw data was standardized before serving as input for the modeling. Followed a previous method and using scanpy package, we normalized the data using scanpy.pp.normalize_total with target_sum set at 1e4, log-transformed through scanpy.pp.log1p, and identified highly variable genes using scanpy.pp.highly_variable_genes, and scaled data feature with scanpy.pp.scale. For cell types that contains more than 5,000 cells, we randomly selected 5,000 cells to represent that particular cell type. To build a multi-classifier, we utilized the CatBoost algorithm, which can effectively reduce overfitting and improve the accuracy and generalization ability of the model. Initially, the processed data were split into an 80% as training set and a 20% as test set. We performed ten-fold cross-validation to optimize the model parameters and selected the best ones. The best model was trained using the training set and evaluated using the test set. We used area under the receiver operating characteristic curve (AUROC) to evaluate the model performance on the test set. To the end this model was used for automated cell type annotation.

### Supported Species and reference genomes

>  Oryza Sativa: [Os-Nipponbare-Reference-IRGSP-1.0]

Rice-Root-Cell-Type-Prediction-Tool pipeline : 

![image](https://github.com/dongwei-2023/Rice-Root-Cell-Type-Prediction-Tool/blob/main/img/model.png)

Application of our model to new rice root data : 

![image](https://github.com/dongwei-2023/Rice-Root-Cell-Type-Prediction-Tool/blob/main/img/predict_new_cellType.png)

## **System Requirements**
### Hardware Requirements
A computer with the following specs:

>  RAM : 16 + GB

>  CPU : 8 + cores

### Software Requirements
This tool we developed and tested on linux.

>  Linux : CentOS 7.6 and Ubuntu 22.04.4 LTS

>  Python (v3.8 or more; Developed and tested version : Python 3.8.13)

>  Scanpy : 1.9.5

>  optuna : 3.4.0

>  sklearn : 1.0.2

>  catboost : 1.2.2


## **Example :** 
>  Input : Input of expression matrix, including "barcodes.tsv.gz"  "features.tsv.gz"  "matrix.mtx.gz" files.

>  Output ： The output is a text file of the cell's barcode and Predicted Label.
``` Bash
python predict_cellType.py -i "./matrix" -o "./out" -m "./Rice-Root-Cell-Type-Prediction-Tool_Best_Model.pkl"
```
## Questions and errors
If you have a question, error, bug, or problem, please use the [Github issue page](https://github.com/dongwei-2023/Rice-Root-Cell-Type-Prediction-Tool/issues).
