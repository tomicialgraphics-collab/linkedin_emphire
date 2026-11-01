PY ?= python3

.PHONY: install test lint demo demo-fixed baseline clean

install:
	pip install -e ".[dev]"

test:
	$(PY) -m pytest -q

lint:
	ruff check .

demo:
	$(PY) -m gatecheck run --demo vulnerable --out .gatecheck/runs/demo

demo-fixed:
	$(PY) -m gatecheck run --demo fixed --out .gatecheck/runs/demo-fixed

baseline:
	$(PY) -m gatecheck run --demo vulnerable --out .gatecheck/runs/baseline --update-baseline

clean:
	rm -rf .gatecheck/runs .pytest_cache .ruff_cache
	find . -name __pycache__ -type d -not -path "./.venv/*" -exec rm -rf {} +
