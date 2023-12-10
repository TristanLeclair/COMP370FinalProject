run-tests:
	@echo "Running tests..."
	@python -m unittest

run-collect: ./scripts/python/collect_articles.py
	@echo "Collecting articles..."
	@python -m scripts.python.collect_articles

run-collect-help: ./scripts/python/collect_articles.py
	@python -m scripts.python.collect_articles -h

venv/bin/activate: requirements.txt
	@echo "Creating virtual environment..."
	@python -m venv venv
	./venv/bin/pip install -r requirements.txt
