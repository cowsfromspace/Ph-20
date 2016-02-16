py = python
p = Assn3.py

compile: basic.tex 
	@# Compiles the .tex and removes all of the extra files
	@pdflatex Basic.tex
	make clean
	make noPics
	@echo "Completed" 

basic.tex:
	@# Will create every graph
	@make problem1_1
	@make problem1_2
	

problem1_1: 
	@$(py) $(p) 1000 0.01 0 1 1
	@$(py) $(p) 100 0.1 0 1 1
	@$(py) $(p) 10000 0.0001 10 10 1
	
problem1_2: 
	@$(py) $(p) 1000 0.01 0 1 2
	@$(py) $(p) 100 0.1 0 1 2
	@$(py) $(p) 10000 0.0001 10 10 2
	
clean:
	@rm -rf *.log *.aux

noPics:
	rm -rf *.png
