.PHONY: test build nlu dm run run nlu install_graph graph

test:
	python3 test_nlu.py

install_graph:
	apt-get install graphviz libgraphviz-dev
	pip3 install pygraphviz --install-option="--include-path=/usr/share/graphviz" --install-option="--library-path=/usr/share/graphviz/"

graph:
	python3 -m rasa_core.visualize -s stories.md -o graph.png -d domain.yml

build:
	@ make nlu
	@ make dm
	@ make run

nlu:
	python3 train_nlu.py

dm:
	python3 train_dm.py
	
run:
	python3 run.py

run_nlu:
	python -m rasa_nlu.server -c rasa_musicplayer/nlu/config.json
