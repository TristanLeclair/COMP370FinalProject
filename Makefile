run-tests:
	@echo "Running tests..."
	@python -m unittest

run-collect: ./scripts/python/collect_movies.py
	@echo "Collecting movies..."
	@python -m scripts.python.collect_movies

run-collect-help: ./scripts/python/collect_movies.py
	@echo "Collecting movies..."
	@python -m scripts.python.collect_movies -h

venv/bin/activate: requirements.txt
	@echo "Creating virtual environment..."
	@python -m venv venv
	./venv/bin/pip install -r requirements.txt
