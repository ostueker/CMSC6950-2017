# Makefile to process datafiles, generate a plot and build LaTeX report.
#
# Variable with list of files with raw data:
DATA=data/data1.txt data/data2.txt data/data3.txt

report.pdf:  report.tex  figure1.svg
	latexmk -pdf -pdflatex='pdflatex -shell-escape'

figure1.svg:  plot_data.py  tempdir/processed_data.csv
	python plot_data.py  -i tempdir/processed_data.csv  -o figure1.svg

tempdir/processed_data.csv:  process_data.py  $(DATA)
	python process_data.py  $(DATA)  -o tempdir/processed_data.csv

.PHONY:  clean  almost_clean

clean:  almost_clean
	rm report.pdf
	rm figure1.svg

almost_clean:
	latexmk -c
	rm tempdir/processed_data.csv
	rm *.pyg
