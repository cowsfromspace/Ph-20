file = basic

setup:
	@#Sets up the .tex file named file
	@printf "\documentclass[a4paper,12pt]{article}\
	\n\usepackage{graphicx}\n\\\begin{document}\n" >> $(file).tex
	@#Does the middle part; actual content
	@make content
	@printf "\end{document}\n" >> $(file).tex
	@pdflatex $(file).tex


header:
	@#I now relate to xkcd.com/1638/
	@printf "Jake Mattinson \hfill Ph20 Assn 3\\\\\\ \\\\\\ \n" >> $(file).tex


content:
	@make header
	@printf "Nothing right now.\n" >> $(file).tex

clean:
	@rm -rf *.log *.aux
