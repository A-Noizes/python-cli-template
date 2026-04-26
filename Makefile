PYTHON=python
ENV_FILE=environment.yml

.PHONY: env-create env-update install test run

env-create:
	conda env create -f $(ENV_FILE)

env-update:
	conda env update -f $(ENV_FILE) --prune

install:
	$(PYTHON) -m pip install -e .

test:
	pytest -q

run:
	$(PYTHON) -m python_cli
