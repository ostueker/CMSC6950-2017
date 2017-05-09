#!/bin/env/python3
import argparse
import os
import numpy as np
import pandas as pd

# use argparse package for processing command line arguments
parser = argparse.ArgumentParser(description='Process some data files.')
parser.add_argument('infiles', metavar='FILE.TXT', type=str, nargs='+',
                    help='name of data file')
parser.add_argument('-o', dest='outfile', metavar='OUTFILE.CSV',
                    default="tempdir/processed_data.csv",
                    help='name of the output file')
args = parser.parse_args()

# load all inputfiles and store arrays in dict
data = {}
for arg in args.infiles:
    dat = np.loadtxt(arg)
    name = arg.split('/')[-1].split('.')[0]
    data[name]=dat

# create dataframe from dict
df = pd.DataFrame(data)

# do some 'fancy' processing ;-)
df['prod'] = df['data1'] * df['data2'] + df['data3']

# create temp dir
if not os.path.exists('tempdir'):
    os.mkdir('tempdir')

# export processed data
df.to_csv(args.outfile, index=False)
