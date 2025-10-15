# Makefile for Workspace Booking Project
# --------------------------------------
# Mirrors GitHub Actions CI steps for consistent local development

PYTHON := python3
VENV := venv
ACT_EXISTS := $(shell command -v act 2> /dev/null)

.PHONY: help setup install lint test ci clean

help:
	@echo ""
	@echo "🧰 Available commands:"
	@echo "  make setup     → Create venv & install dependencies"
	@echo "  make install   → Install dependencies in existing venv"
	@echo "  make lint      → Run Ruff linter"
	@echo "  make test      → Run pytest with Django settings"
	@echo "  make ci        → Simulate GitHub CI pipeline locally (requires act)"
	@echo "  make clean     → Remove venv and temporary files"
	@echo ""

setup:
	@echo "🔧 Creating Python virtual environment..."
	$(PYTHON) -m venv $(VENV)
	@$(MAKE) install
	@echo "✅ Setup complete."

install:
	@echo "📦 Installing dependencies..."
	. $(VENV)/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@echo "✅ Dependencies installed."

lint:
	@echo "🧹 Running Ruff linter..."
	@if [ -n "$(ACT_EXISTS)" ]; then \
		echo "Running via act (GitHub Action simulation)..."; \
		act -j test --reuse; \
	else \
		. $(VENV)/bin/activate && ruff check . --exit-zero; \
	fi
	@echo "✅ Linting done."

test:
	@echo "🧪 Running Django tests with pytest..."
	@if [ -n "$(ACT_EXISTS)" ]; then \
		echo "Running via act (GitHub Action simulation)..."; \
		act -j test --reuse; \
	else \
		. $(VENV)/bin/activate && \
		export DJANGO_SETTINGS_MODULE=config.settings && \
		pytest --maxfail=1 --disable-warnings -q; \
	fi
	@echo "✅ Tests completed."

ci:
	@echo "🚀 Running full CI pipeline locally..."
	@if [ -n "$(ACT_EXISTS)" ]; then \
		act; \
	else \
		echo "act not found, running lint + test locally..."; \
		make lint && make test; \
	fi
	@echo "✅ Local CI simulation done."

clean:
	@echo "🧹 Cleaning environment..."
	rm -rf $(VENV) __pycache__ .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "✅ Cleanup complete."

run:
	@echo "🚀 Running Django development server..."
	. $(VENV)/bin/activate && export DJANGO_SETTINGS_MODULE=config.settings && python manage.py runserver