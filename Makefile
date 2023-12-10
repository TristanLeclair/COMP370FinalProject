run-tests:
	@echo "Running tests..."
	@echo
	@python -m unittest

run-collect: ./scripts/python/collect_articles.py
	@echo "Collecting articles..."
	@echo
	@python -m scripts.python.collect_articles

run-collect_deep: ./scripts/python/collect_articles.py
	@echo "Collecting articles..."
	@echo
	@python -m scripts.python.collect_articles --deep

run-collect-help: ./scripts/python/collect_articles.py
	@python -m scripts.python.collect_articles -h

venv/bin/activate: requirements.txt
	@echo "Creating virtual environment..."
	@python -m venv venv
	./venv/bin/pip install -r requirements.txt
