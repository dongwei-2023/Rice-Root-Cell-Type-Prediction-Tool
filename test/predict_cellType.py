#!/usr/bin/env python

import os
import argparse
import sys
import subprocess
import re
import glob
import scanpy as sc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import collections
import warnings
warnings.filterwarnings('ignore')

def get_parsed_args():

    parser = argparse.ArgumentParser(description="Rice-Root-Cell-Type-Prediction-Tool prepare data")
    
    
    parser.add_argument('-i', dest= 'input_directory', help='Input of expression matrix, including "barcodes.tsv.gz"  "features.tsv.gz"  "matrix.mtx.gz" files.'
                                              'Please make sure the refence genome is MSU7 of Os ID.')

    parser.add_argument("-o", dest='output_directory', default="./", help="Output directory to store the output files."
                                                                    "Default: ./ ")
                                                                    
    parser.add_argument('-m', dest='model_path', help='The path of model used for prediction.')
    

    args = parser.parse_args()
    return args



def preprocessing_test(adataPath, hvgs_names):
    adata = sc.read_10x_mtx(adataPath,var_names= 'gene_symbols',cache = False)
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    intersection_genes = list(set(adata.var_names) & set(hvgs_names))
    adata = adata[:, intersection_genes]
    # Scale
    sc.pp.scale(adata, max_value=10)
    X_df = pd.DataFrame(adata.X, index=adata.obs_names, columns=adata.var_names)
    complement_gene = list(set(hvgs_names) - set(X_df.columns))  
    final_df = X_df.assign(**{col: 0 for col in complement_gene})
    print("The count of model features is: ", len(hvgs_names))
    print("The count of genes that intersect with the model features in the new dataset is: ", len(list(set(hvgs_names) & set(X_df.columns))))
    print(type(final_df), final_df.shape)
    return final_df


def main(argv=None):
    if argv is None:
        argv = sys.argv
    args = get_parsed_args()

    input_directory = args.input_directory
    output_directory = args.output_directory
    model_path = args.model_path
    
    best_model = pickle.load(open(model_path, "rb"))
    highly_variable_genes = best_model.feature_names_

    test_data = preprocessing_test(adataPath = input_directory,
                             hvgs_names = highly_variable_genes)

    predicted_labels_mpos = best_model.predict(test_data) 

    result_df_mpos = pd.DataFrame({'Predicted_Label': predicted_labels_mpos.flatten()}, index=test_data.index)

    output_path = os.path.join(output_directory, 'result.csv')
    result_df_mpos.to_csv(output_path)
    print(result_df_mpos)


if __name__ == "__main__":
    main()
