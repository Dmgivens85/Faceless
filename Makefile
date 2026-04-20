.PHONY: run bootstrap

bootstrap:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

run:
	./run.sh
