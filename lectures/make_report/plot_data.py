#!/bin/env/python3
import argparse
import os
import pandas as pd

# use argparse package for processing command line arguments
parser = argparse.ArgumentParser(description='Plot a datafile.')
parser.add_argument('-i', dest='infile', metavar='INFILE.CSV', 
                    default="tempdir/processed_data.csv",
                    help='name of the data file')
parser.add_argument('-o', dest='outfile', metavar='PLOT.SVG',
                    default="figure.svg",
                    help='name of the output file')
args = parser.parse_args()

df = pd.read_csv(args.infile)

plot = df.plot(ylim=(-5,5))
plot.figure.savefig(args.outfile)
