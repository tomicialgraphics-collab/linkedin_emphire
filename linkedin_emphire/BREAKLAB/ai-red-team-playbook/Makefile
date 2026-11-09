.PHONY: all validate render check coverage example clean

all: validate render

validate:
	python3 tools/validate.py

render:
	python3 tools/render.py

check:
	python3 tools/validate.py
	python3 tools/render.py --check
	python3 tools/coverage.py examples/status-example.json -o /dev/null
	python3 tools/wilson.py 3 20

coverage:
	python3 tools/coverage.py examples/status-example.json

clean:
	rm -rf out __pycache__ tools/__pycache__
