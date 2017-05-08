
report.pdf: report.tex figure1.svg
	latexmk -pdf -pdflatex='pdflatex -shell-escape'

tempdir/processed_data.csv: data/data1.txt data/data2.txt data/data3.txt
	python process_data.py  $^  -o tempdir/processed_data.csv

figure1.svg: tempdir/processed_data.csv
	python plot_data.py  -i tempdir/processed_data.csv  -o figure1.svg

.PHONY: clean almost_clean

clean: almost_clean
	rm report.pdf
	rm figure1.svg

almost_clean:
	latexmk -c
	rm tempdir/processed_data.csv

