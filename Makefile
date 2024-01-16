deps:
	pip-compile requirenments.in 
	pip-sync requirenments.txt
