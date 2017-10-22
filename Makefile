build:
	@ make build_nlu
	@ make build_dm

build_nlu:
	python3 train_nlu.py

build_dm:
	python3 train_dm.py
	
run:
	python3 run.py
