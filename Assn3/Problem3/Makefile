#################################
# PH 20 Assignment 3, problem 3 #
#############################################################
# Note: The say command is a Mac command. It’s too much fun #
# to replace with echo, but if you want to run it, you can  #
# do so.                                                    #
#############################################################

PY = python
P  = ph20-3-1-3.py
P2 = graphErrors.py
x0 = 1
v0 = 20

problem3:
	#say Problem three initiated. Calculating variable inputs now…
	$(PY) $(P) 2500 0.004 $(x0) $(v0)
	$(PY) $(P) 5000 0.002 $(x0) $(v0)
	$(PY) $(P) 10000 0.001 $(x0) $(v0)
	$(PY) $(P) 20000 0.0005 $(x0) $(v0)
	$(PY) $(P) 40000 0.00025 $(x0) $(v0)
	$(PY) $(P) 80000 0.000125 $(x0) $(v0)
	$(PY) $(P) 160000 0.0000625 $(x0) $(v0)
	#say Graphing Sequence Initiated…
	$(PY) $(P2)
	#say Thank you come again
	make clean
clean:
	rm -f Errors.txt