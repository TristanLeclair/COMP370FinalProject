run-tests:
	@echo "Running tests..."
	@echo
	@python -m unittest

run-all: run-collect run-extract

run-all_deep: run-collect_deep run-extract_deep

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

run-extract: ./scripts/python/extract_movies.py
	@echo "Extracting movies..."
	@echo
	@python -m scripts.python.extract_movies -i $(articles_path)

run-extract-help: ./scripts/python/extract_movies.py
	@python -m scripts.python.extract_movies -h

run-extract_deep: ./scripts/python/prepare_data.py
	@echo "Extracting movies..."
	@echo
	@python -m scripts.python.extract_movies -i $(articles_path) --deep

venv/bin/activate: requirements.txt
	@echo "Creating virtual environment..."
	@python -m venv venv
	./venv/bin/pip install -r requirements.txt
