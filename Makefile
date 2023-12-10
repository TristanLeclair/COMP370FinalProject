run-tests:
	@echo "Running tests..."
	@python3 -m unittest

venv/bin/activate: requirements.txt
	@echo "Creating virtual environment..."
	@python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
